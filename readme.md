# Agent DSL

Proyecto de analisis sintactico y semantico para un DSL de agentes.

## Estructura

- `grammar/AgentDSL.g4`: gramatica ANTLR.
- `src/generated/`: archivos generados por ANTLR.
- `src/main.py`: entrada principal del analizador.
- `src/semantic_analyzer.py`: validaciones semanticas.
- `src/symbol_table.py`: tabla de simbolos para percepciones, estados y acciones.
- `src/semantic_error.py`: formato comun para errores semanticos.
- `examples/`: programas de prueba del DSL.

## Que valida

- Declaraciones duplicadas de variables y acciones.
- Uso de variables no declaradas en condiciones.
- Uso de acciones no declaradas en reglas `do`.
- Compatibilidad de tipos en valores iniciales.
- Compatibilidad de tipos en comparaciones.
- Advertencias para declaraciones que nunca se usan.

## Regenerar parser/lexer

Desde la raiz del proyecto:

```powershell
antlr4 -Dlanguage=Python3 -visitor -o src\generated -Xexact-output-dir grammar\AgentDSL.g4
```

## Ejecutar ejemplos

```powershell
python src\main.py
```
