import sys
from pathlib import Path

from antlr4 import CommonTokenStream, FileStream

from generated.AgentDSLLexer import AgentDSLLexer
from generated.AgentDSLParser import AgentDSLParser
from semantic_analyzer import SemanticAnalyzer


# Ruta base del proyecto. Se calcula desde este archivo para que el programa
# funcione tanto si se ejecuta desde la raiz como desde la carpeta `src`.
BASE_DIR = Path(__file__).resolve().parent.parent


def analyze_file(path):
    """Ejecuta analisis lexico, sintactico y semantico para un archivo."""
    path = Path(path)

    print("=" * 60)
    print(f"Analizando archivo: {path}")
    print("=" * 60)

    # ANTLR lee el archivo como flujo de caracteres.
    input_stream = FileStream(str(path), encoding="utf-8")

    # El lexer transforma caracteres en tokens.
    lexer = AgentDSLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # El parser transforma tokens en un arbol sintactico.
    parser = AgentDSLParser(token_stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Se encontraron errores sintacticos. No se ejecuta el analisis semantico.")
        return

    print("Analisis sintactico correcto.\n")

    # El visitante semantico recorre el arbol y revisa reglas de significado.
    analyzer = SemanticAnalyzer()
    errors = analyzer.visit(tree)

    if len(errors) == 0:
        print("Analisis semantico correcto.")
    else:
        print("Errores semanticos encontrados:\n")
        for err in errors:
            print(err)

    warnings = analyzer.symtab.unused_warnings()
    if warnings:
        print("\nAdvertencias:\n")
        for warning in warnings:
            print(warning)


if __name__ == "__main__":
    # Si el usuario pasa archivos por consola, se analizan esos archivos.
    # Si no pasa nada, se ejecutan los ejemplos del proyecto.
    files = [Path(arg) for arg in sys.argv[1:]]

    if not files:
        files = [
            BASE_DIR / "examples" / "valid_warehouse.agent",
            BASE_DIR / "examples" / "valid_minimarket.agent",
            BASE_DIR / "examples" / "semantic_error_duplicate.agent",
            BASE_DIR / "examples" / "semantic_error_undefined.agent",
            BASE_DIR / "examples" / "semantic_error_type.agent",
        ]

    for file in files:
        analyze_file(file)
        print()
