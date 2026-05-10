from semantic_error import SemanticError


class Symbol:
    """Guarda la informacion semantica de un identificador del DSL."""

    def __init__(self, name: str, type_: str, category: str, line: int):
        self.name = name
        self.type_ = type_
        self.category = category
        self.line = line
        self.used = False


class SymbolTable:
    """Tabla de simbolos para percepciones, estados y acciones.

    En este DSL no tenemos bloques anidados como en un lenguaje general, pero si
    tenemos tres "espacios" de nombres importantes:
    - variables: percepciones y estados, usados en condiciones.
    - acciones: funciones que pueden ejecutarse con `do`.
    """

    def __init__(self):
        self.variables: dict[str, Symbol] = {}
        self.actions: dict[str, Symbol] = {}

    def declare_variable(self, name: str, type_: str, category: str, line: int):
        """Registra una percepcion o estado y evita declaraciones duplicadas."""
        if name in self.variables:
            previous = self.variables[name]
            raise SemanticError(
                f"'{name}' ya fue declarado como {previous.category} en la linea {previous.line}",
                line,
            )

        self.variables[name] = Symbol(name, type_, category, line)

    def declare_action(self, name: str, line: int):
        """Registra una accion disponible para las reglas de comportamiento."""
        if name in self.actions:
            previous = self.actions[name]
            raise SemanticError(
                f"La accion '{name}' ya fue declarada en la linea {previous.line}",
                line,
            )

        self.actions[name] = Symbol(name, "action", "accion", line)

    def lookup_variable(self, name: str) -> Symbol | None:
        return self.variables.get(name)

    def lookup_action(self, name: str) -> Symbol | None:
        return self.actions.get(name)

    def unused_warnings(self) -> list[str]:
        """Genera advertencias para declaraciones que nunca se usan."""
        warnings = []

        for symbol in self.variables.values():
            if not symbol.used:
                warnings.append(
                    f"[Advertencia, linea {symbol.line}] "
                    f"'{symbol.name}' fue declarado como {symbol.category}, pero nunca se uso."
                )

        for symbol in self.actions.values():
            if not symbol.used:
                warnings.append(
                    f"[Advertencia, linea {symbol.line}] "
                    f"La accion '{symbol.name}' fue declarada, pero nunca se ejecuto."
                )

        return warnings
