class SemanticError(Exception):
    """Representa un error semantico con numero de linea.

    Usamos una clase propia para que todos los errores tengan el mismo formato
    y sea facil mostrarlos desde `main.py`.
    """

    def __init__(self, message: str, line: int = 0):
        super().__init__(f"[Error semantico, linea {line}] {message}")
        self.line = line
