# 🤖 AgentDSL

> Lenguaje declarativo de dominio específico para definir agentes inteligentes basados en percepción y acción.

[![ANTLR4](https://img.shields.io/badge/ANTLR-4-red)](https://www.antlr.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![UPC](https://img.shields.io/badge/UPC-Teoría%20de%20Compiladores-green)](https://www.upc.edu.pe/)

---

## 📌 Tabla de contenidos

- [Motivación](#-motivación)
- [¿Qué es AgentDSL?](#-qué-es-agentdsl)
- [Arquitectura del lenguaje](#-arquitectura-del-lenguaje)
- [Características](#-características)
- [Validaciones semánticas](#-validaciones-semánticas)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Instalación y uso](#-instalación-y-uso)
- [Roadmap](#-roadmap)
- [Equipo](#-equipo)

---

## 💡 Motivación

El desarrollo de agentes inteligentes actualmente requiere lenguajes de propósito general como Python o Java, donde la lógica de comportamiento se mezcla con detalles técnicos de implementación: clases, métodos, estructuras de control anidadas y manejo de estado explícito.

| Aspecto | Con lenguajes tradicionales | Con AgentDSL |
|---|---|---|
| Legibilidad | Lógica enterrada en código técnico | Secciones claras y predecibles |
| Curva de aprendizaje | Requiere dominar un lenguaje completo | Solo la sintaxis del agente |
| Público objetivo | Solo programadores | Programadores + especialistas de dominio |
| Mantenimiento | Difícil al escalar | Estructura modular por diseño |

Frameworks como **JADE** o los **behavior trees** de motores de videojuegos son bibliotecas sobre lenguajes existentes, no lenguajes independientes. Requieren entornos complejos, conocimiento previo del lenguaje base y una curva de aprendizaje considerable. AgentDSL propone una alternativa independiente y accesible.

---

## 🧠 ¿Qué es AgentDSL?

AgentDSL es un lenguaje diseñado para describir agentes inteligentes en términos de lo que perciben, el estado en que se encuentran y las acciones que ejecutan. Cada agente se define mediante cuatro secciones obligatorias:

```
┌─────────────────────────────────────────┐
│              agent MiAgente             │
├─────────────┬───────────────────────────┤
│ perceptions │ Lo que percibe del entorno│
├─────────────┼───────────────────────────┤
│ state       │ Su estado interno         │
├─────────────┼───────────────────────────┤
│ actions     │ Lo que puede hacer        │
├─────────────┼───────────────────────────┤
│ behavior    │ Reglas de decisión        │
└─────────────┴───────────────────────────┘
```

Cada agente sigue un ciclo continuo de **percepción → decisión → acción**, y la sintaxis del lenguaje refleja exactamente esa estructura. Ver los programas de ejemplo en `examples/` para entender la sintaxis en la práctica.

---

## 🏗 Arquitectura del lenguaje

### Pipeline del compilador

```
Código fuente (.adsl)
       │
       ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Lexer       │────▶│  Parser      │────▶│  Análisis    │
│  (Tokens)    │     │  (AST)       │     │  Semántico   │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                  │
                                          ┌───────▼───────┐
                                          │  Generación   │
                                          │  de código    │
                                          │  (futuro)     │
                                          └───────────────┘
```

La gramática formal está definida en `grammar/AgentDSL.g4` con reglas de parser (estructura sintáctica) y reglas de lexer (tokens reconocidos).

---

## ✨ Características

### Tipos de datos soportados

| Tipo | Descripción | Uso típico |
|------|-------------|------------|
| `int` | Enteros | Contadores, niveles, horas |
| `float` | Decimales | Temperaturas, umbrales |
| `string` | Cadenas de texto | Nombres, modos, etiquetas |
| `bool` | Booleanos | Flags, estados on/off |

### Operadores de comparación

| Operador | Significado |
|----------|-------------|
| `>` `<` | Mayor / menor que |
| `==` `!=` | Igual / diferente |
| `>=` `<=` | Mayor o igual / menor o igual |

### Secciones del agente

- **`perceptions`** — Variables que el agente percibe del entorno externo.
- **`state`** — Variables internas con valor inicial opcional.
- **`actions`** — Acciones que el agente puede ejecutar.
- **`behavior`** — Reglas condicionales con formato `if <condición> then do <acción>()`.

---

## 🔍 Validaciones semánticas

El analizador semántico verifica que un programa sintácticamente correcto también sea lógicamente válido:

| Validación | Tipo | Ejemplo detectado |
|---|---|---|
| Declaración duplicada | ❌ Error | Una variable declarada dos veces en el mismo scope |
| Variable no declarada | ❌ Error | Usar una variable en behavior sin declararla en perceptions/state |
| Acción no declarada | ❌ Error | Invocar una acción en behavior sin declararla en actions |
| Tipo incompatible en asignación | ❌ Error | Asignar un string a una variable declarada como int |
| Tipo incompatible en comparación | ❌ Error | Comparar un string con un int en una condición |
| Variable sin usar | ⚠️ Advertencia | Declarar una variable que nunca se referencia en behavior |

La implementación se encuentra en `src/semantic_analyzer.py` con soporte de `src/symbol_table.py`.

---

## 📁 Estructura del proyecto

```
AgentDSL/
├── grammar/
│   └── AgentDSL.g4              # Gramática ANTLR4 (lexer + parser)
├── src/
│   ├── generated/               # Archivos generados por ANTLR (no editar)
│   ├── main.py                  # Punto de entrada principal
│   ├── semantic_analyzer.py     # Visitor con validaciones semánticas
│   ├── symbol_table.py          # Tabla de símbolos (percepciones, estados, acciones)
│   └── semantic_error.py        # Clase para formatear errores semánticos
└── examples/                    # Programas de prueba en AgentDSL
```

---

## ⚙ Instalación y uso

### Prerrequisitos

- Python 3.10+
- Java Runtime (para ANTLR4)
- ANTLR4 tool ([instrucciones](https://www.antlr.org/))
- `pip install antlr4-python3-runtime`

### Regenerar parser y lexer

Ejecutar desde la raíz del proyecto cada vez que se modifique la gramática:

```powershell
antlr4 -Dlanguage=Python3 -visitor -o src\generated -Xexact-output-dir grammar\AgentDSL.g4
```

### Ejecutar el analizador

```powershell
python src\main.py
```

El programa procesará los archivos de ejemplo y mostrará errores semánticos y advertencias encontrados.

---

## 🗺 Roadmap

- [x] Diseño de la gramática formal en ANTLR4
- [x] Implementación del lexer y parser
- [x] Análisis semántico (tipos, scopes, declaraciones)
- [ ] Generación de código intermedio (LLVM IR)
- [ ] Compilación a código ejecutable
- [ ] Soporte para parámetros en acciones
- [ ] Operadores lógicos (`and`, `or`, `not`) en condiciones
- [ ] Bloques `else` y `elif` en behavior
- [ ] Soporte para múltiples archivos / imports

---

## 👥 Equipo

| Nombre | Código |
|--------|--------|
| Cielo Luwidka Chavez Merino | U20191E443 |
| Alvaro Manuel De Cossio Velasquez | U20221F812 |
| Loana Colleen Rodriguez Matos | U202115571 |
| Joaquin Sebastian Ruiz Ramirez | U20201F678 |

**Docente:** Jose Luis Soncco Alvarez
**Curso:** Teoría de Compiladores — Ciencias de la Computación, UPC
**Fecha:** Mayo 2026

---

## 📄 Licencia

Proyecto académico desarrollado para el curso de Teoría de Compiladores, UPC.
