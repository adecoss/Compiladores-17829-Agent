# 🤖 AgentDSL

> Lenguaje declarativo de dominio específico para definir agentes inteligentes basados en percepción y acción.

[![ANTLR4](https://img.shields.io/badge/ANTLR-4-red)](https://www.antlr.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![UPC](https://img.shields.io/badge/UPC-Teoría%20de%20Compiladores-green)](https://www.upc.edu.pe/)

---

## 📌 Tabla de contenidos

- [Motivación](#-motivación)
- [¿Qué es AgentDSL?](#-qué-es-agentdsl)
- [Ejemplo rápido](#-ejemplo-rápido)
- [Arquitectura del lenguaje](#-arquitectura-del-lenguaje)
- [Características](#-características)
- [Validaciones semánticas](#-validaciones-semánticas)
- [Gramática completa](#-gramática-completa)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Instalación y uso](#-instalación-y-uso)
- [Ejemplos adicionales](#-ejemplos-adicionales)
- [Roadmap](#-roadmap)
- [Equipo](#-equipo)

---

## 💡 Motivación

El desarrollo de agentes inteligentes actualmente requiere lenguajes de propósito general como Python o Java, donde la **lógica de comportamiento** se mezcla con **detalles técnicos** de implementación: clases, métodos, estructuras de control anidadas y manejo de estado explícito.

### El problema

| Aspecto | Con lenguajes tradicionales | Con AgentDSL |
|---|---|---|
| Legibilidad | Lógica enterrada en código técnico | Secciones claras y predecibles |
| Curva de aprendizaje | Requiere dominar un lenguaje completo | Solo la sintaxis del agente |
| Público objetivo | Solo programadores | Programadores + especialistas de dominio |
| Mantenimiento | Difícil al escalar | Estructura modular por diseño |

### ¿Por qué no usar lo que ya existe?

Frameworks como **JADE** o los **behavior trees** de motores de videojuegos son bibliotecas sobre lenguajes existentes, no lenguajes independientes. Requieren entornos complejos, conocimiento previo del lenguaje base y una curva de aprendizaje considerable.

---

## 🧠 ¿Qué es AgentDSL?

AgentDSL es un lenguaje diseñado para describir agentes inteligentes en términos de:

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

Cada agente sigue un ciclo continuo de **percepción → decisión → acción**, y la sintaxis del lenguaje refleja exactamente esa estructura.

---

## 🚀 Ejemplo rápido

```
agent Bodeguero {
  perceptions {
    stock : int;
    hora : int;
  }
  state {
    alertLevel : int = 0;
  }
  actions {
    action restock();
    action close();
  }
  behavior {
    if stock < 10 then do restock();
    if hora > 22 then do close();
  }
}
```

**¿Qué hace este agente?** El `Bodeguero` percibe el nivel de stock y la hora actual. Si el stock baja de 10 unidades, repone inventario. Si pasan las 10 PM, cierra la tienda. Sin clases, sin imports, sin boilerplate.

---

## 🏗 Arquitectura del lenguaje

```
                    ┌──────────┐
                    │ Programa │
                    └────┬─────┘
                         │ contiene 1..*
                 ┌───────┴───────┐
                 │    Agente     │
                 └───────┬───────┘
                         │ se compone de
          ┌──────┬───────┼────────┬──────┐
          │      │       │        │      │
          ▼      ▼       ▼        ▼      │
     ┌────────┐┌─────┐┌───────┐┌────────┐│
     │Percep- ││State││Actions││Behavior││
     │tions   ││     ││       ││        ││
     └────────┘└─────┘└───────┘└────────┘│
                                         │
     Ciclo: Percibir → Decidir → Actuar ◄┘
```

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

---

## ✨ Características

### Tipos de datos soportados

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| `int` | Enteros | `stock : int;` |
| `float` | Decimales | `temperatura : float;` |
| `string` | Cadenas de texto | `nombre : string;` |
| `bool` | Booleanos | `activo : bool;` |

### Operadores de comparación

| Operador | Significado |
|----------|-------------|
| `>` | Mayor que |
| `<` | Menor que |
| `==` | Igual a |
| `!=` | Diferente de |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |

### Secciones del agente

- **`perceptions {}`** — Variables que el agente percibe del entorno externo.
- **`state {}`** — Variables internas con valor inicial opcional.
- **`actions {}`** — Acciones que el agente puede ejecutar.
- **`behavior {}`** — Reglas condicionales con formato `if <condición> then do <acción>();`.

---

## 🔍 Validaciones semánticas

El analizador semántico verifica que un programa sintácticamente correcto también sea lógicamente válido:

| Validación | Tipo | Ejemplo detectado |
|---|---|---|
| Declaración duplicada | ❌ Error | `stock : int;` declarado dos veces |
| Variable no declarada | ❌ Error | Usar `precio` en behavior sin declararlo |
| Acción no declarada | ❌ Error | `do enviar();` sin declararla en actions |
| Tipo incompatible en asignación | ❌ Error | `count : int = "hola";` |
| Tipo incompatible en comparación | ❌ Error | `if nombre > 10 then ...` |
| Variable sin usar | ⚠️ Advertencia | Declarar `nivel` pero nunca referenciarlo |

---

## 📜 Gramática completa

La gramática formal está implementada en ANTLR4 y se encuentra en `grammar/AgentDSL.g4`:

```antlr
grammar AgentDSL;

// ─── Reglas del Parser ───────────────────────────

program         : agentDecl+ EOF ;

agentDecl       : AGENT ID LBRACE section* RBRACE ;

section         : perceptionsSection
                | stateSection
                | actionsSection
                | behaviorSection ;

perceptionsSection : PERCEPTIONS LBRACE perceptionDecl* RBRACE ;
perceptionDecl    : ID COLON type SEMI ;

stateSection    : STATE LBRACE stateDecl* RBRACE ;
stateDecl       : ID COLON type (ASSIGN literal)? SEMI ;

actionsSection  : ACTIONS LBRACE actionDecl* RBRACE ;
actionDecl      : ACTION ID LPAREN RPAREN SEMI ;

behaviorSection : BEHAVIOR LBRACE ruleDecl* RBRACE ;
ruleDecl        : IF condition THEN DO ID LPAREN RPAREN SEMI ;

condition       : expression comparisonOperator expression ;
expression      : ID | literal ;
comparisonOperator : GT | LT | EQ | NEQ | GTE | LTE ;

type            : INT_TYPE | FLOAT_TYPE | STRING_TYPE | BOOL_TYPE ;
literal         : INT | FLOAT | STRING | TRUE | FALSE ;

// ─── Reglas del Lexer ────────────────────────────

AGENT       : 'agent';
PERCEPTIONS : 'perceptions';
STATE       : 'state';
ACTIONS     : 'actions';
ACTION      : 'action';
BEHAVIOR    : 'behavior';
IF          : 'if';
THEN        : 'then';
DO          : 'do';

INT_TYPE    : 'int';
FLOAT_TYPE  : 'float';
STRING_TYPE : 'string';
BOOL_TYPE   : 'bool';

TRUE  : 'true';
FALSE : 'false';

GT : '>';   LT  : '<';
EQ : '==';  NEQ : '!=';
GTE: '>=';  LTE : '<=';

ASSIGN : '=';  COLON : ':';
SEMI   : ';';  COMMA : ',';
LBRACE : '{';  RBRACE : '}';
LPAREN : '(';  RPAREN : ')';

FLOAT  : [0-9]+ '.' [0-9]+ ;
INT    : [0-9]+ ;
STRING : '"' (~["\\] | '\\' .)* '"' ;
ID     : [a-zA-Z_][a-zA-Z0-9_]* ;

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
```

---

## 📁 Estructura del proyecto

```
AgentDSL/
├── grammar/
│   └── AgentDSL.g4              # Gramática ANTLR4
├── src/
│   ├── generated/               # Archivos generados por ANTLR (no editar)
│   │   ├── AgentDSLLexer.py
│   │   ├── AgentDSLParser.py
│   │   └── AgentDSLVisitor.py
│   ├── main.py                  # Punto de entrada principal
│   ├── semantic_analyzer.py     # Visitor que realiza validaciones semánticas
│   ├── symbol_table.py          # Tabla de símbolos (percepciones, estados, acciones)
│   └── semantic_error.py        # Clase para formatear errores semánticos
└── examples/                    # Programas de prueba en AgentDSL
    ├── bodeguero.adsl
    └── ...
```

---

## ⚙ Instalación y uso

### Prerrequisitos

- Python 3.10+
- Java Runtime (para ANTLR4)
- ANTLR4 tool ([instrucciones de instalación](https://www.antlr.org/))

### Instalar dependencias

```bash
pip install antlr4-python3-runtime
```

### Regenerar parser y lexer

Ejecutar desde la raíz del proyecto cada vez que se modifique `AgentDSL.g4`:

```powershell
antlr4 -Dlanguage=Python3 -visitor -o src\generated -Xexact-output-dir grammar\AgentDSL.g4
```

### Ejecutar el analizador

```powershell
python src\main.py
```

El programa procesará los archivos de ejemplo y mostrará errores semánticos y advertencias encontrados.

---

## 📝 Ejemplos adicionales

### Agente con múltiples reglas

```
agent Guardia {
  perceptions {
    movimiento : bool;
    horaActual : int;
    temperatura : float;
  }
  state {
    alerta : bool = false;
    turno : string = "noche";
  }
  actions {
    action activarAlarma();
    action llamarRefuerzo();
    action registrarEvento();
  }
  behavior {
    if movimiento == true then do activarAlarma();
    if horaActual > 23 then do llamarRefuerzo();
    if temperatura > 45.0 then do registrarEvento();
  }
}
```

### Programa con múltiples agentes

```
agent Sensor {
  perceptions {
    humedad : float;
  }
  state {
    umbral : float = 80.0;
  }
  actions {
    action alertar();
  }
  behavior {
    if humedad > 80.0 then do alertar();
  }
}

agent Controlador {
  perceptions {
    alertaActiva : bool;
  }
  state {
    modo : string = "auto";
  }
  actions {
    action apagarSistema();
  }
  behavior {
    if alertaActiva == true then do apagarSistema();
  }
}
```

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
