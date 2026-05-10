from generated.AgentDSLVisitor import AgentDSLVisitor
from semantic_error import SemanticError
from symbol_table import SymbolTable


NUMERIC_TYPES = {"int", "float"}


class SemanticAnalyzer(AgentDSLVisitor):
    """Recorre el arbol generado por ANTLR y valida reglas semanticas.

    El parser solo comprueba que el texto tenga la forma correcta. Este visitante
    revisa reglas de significado: identificadores declarados, tipos compatibles,
    acciones existentes y declaraciones duplicadas.
    """

    def __init__(self):
        self.symtab = SymbolTable()
        self.errors: list[SemanticError] = []

    def _add_error(self, message: str, ctx):
        """Agrega un error usando la linea del nodo del arbol sintactico."""
        self.errors.append(SemanticError(message, ctx.start.line))
        return "error"

    def visitProgram(self, ctx):
        """Punto de entrada del analisis semantico."""
        for agent in ctx.agentDecl():
            self.visit(agent)

        return self.errors

    def visitAgentDecl(self, ctx):
        """Analiza todas las secciones declaradas dentro de un agente."""
        for section in ctx.section():
            self.visit(section)

    def visitPerceptionDecl(self, ctx):
        """Registra una percepcion disponible para las reglas `if`."""
        name = ctx.ID().getText()
        var_type = ctx.type_().getText()

        try:
            self.symtab.declare_variable(
                name=name,
                type_=var_type,
                category="percepcion",
                line=ctx.start.line,
            )
        except SemanticError as error:
            self.errors.append(error)

    def visitStateDecl(self, ctx):
        """Registra una variable de estado y valida su valor inicial."""
        name = ctx.ID().getText()
        var_type = ctx.type_().getText()

        try:
            self.symtab.declare_variable(
                name=name,
                type_=var_type,
                category="estado",
                line=ctx.start.line,
            )
        except SemanticError as error:
            self.errors.append(error)
            return

        # Si la declaracion trae valor inicial, debe coincidir con el tipo.
        if ctx.literal():
            literal_type = self.visit(ctx.literal())
            if not self._is_assignable(var_type, literal_type):
                self._add_error(
                    f"No se puede inicializar '{name}' de tipo '{var_type}' "
                    f"con un valor '{literal_type}'",
                    ctx,
                )

    def visitActionDecl(self, ctx):
        """Registra una accion que luego puede ser llamada desde `behavior`."""
        action_name = ctx.ID().getText()

        try:
            self.symtab.declare_action(action_name, ctx.start.line)
        except SemanticError as error:
            self.errors.append(error)

    def visitRuleDecl(self, ctx):
        """Valida una regla: condicion correcta y accion existente."""
        self.visit(ctx.condition())

        action_name = ctx.ID().getText()
        action = self.symtab.lookup_action(action_name)

        if action is None:
            self._add_error(f"La accion '{action_name}' no fue declarada", ctx)
            return

        action.used = True

    def visitCondition(self, ctx):
        """Comprueba que ambos lados de una comparacion sean compatibles."""
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))

        if "error" in (left_type, right_type):
            return "error"

        operator = ctx.comparisonOperator().getText()

        if operator in {">", "<", ">=", "<="}:
            if left_type not in NUMERIC_TYPES or right_type not in NUMERIC_TYPES:
                return self._add_error(
                    f"El operador '{operator}' solo acepta valores numericos",
                    ctx,
                )
            return "bool"

        if not self._are_comparable(left_type, right_type):
            return self._add_error(
                f"No se puede comparar '{left_type}' con '{right_type}'",
                ctx,
            )

        return "bool"

    def visitExpression(self, ctx):
        """Devuelve el tipo de una expresion simple: identificador o literal."""
        if ctx.literal():
            return self.visit(ctx.literal())

        name = ctx.ID().getText()
        symbol = self.symtab.lookup_variable(name)

        if symbol is None:
            return self._add_error(f"La variable '{name}' no fue declarada", ctx)

        symbol.used = True
        return symbol.type_

    def visitLiteral(self, ctx):
        """Mapea cada literal del DSL a su tipo semantico."""
        if ctx.INT():
            return "int"
        if ctx.FLOAT():
            return "float"
        if ctx.STRING():
            return "string"
        if ctx.TRUE() or ctx.FALSE():
            return "bool"

        return "error"

    def _is_assignable(self, target_type: str, value_type: str) -> bool:
        """Permite asignacion exacta y conversion segura de int a float."""
        return target_type == value_type or (
            target_type == "float" and value_type == "int"
        )

    def _are_comparable(self, left_type: str, right_type: str) -> bool:
        """Define que tipos pueden compararse con == o !=."""
        return left_type == right_type or (
            left_type in NUMERIC_TYPES and right_type in NUMERIC_TYPES
        )
