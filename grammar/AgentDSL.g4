grammar AgentDSL;

// ========== REGLAS DEL PARSER ==========

// Punto de entrada: un archivo puede contener uno o mas agentes.
program
    : agentDecl+ EOF
    ;

// Un agente agrupa sus percepciones, estado, acciones y comportamiento.
agentDecl
    : AGENT ID LBRACE section* RBRACE
    ;

// Cada seccion representa una parte del agente.
section
    : perceptionsSection
    | stateSection
    | actionsSection
    | behaviorSection
    ;

// Percepciones: datos que el agente recibe del entorno.
perceptionsSection
    : PERCEPTIONS LBRACE perceptionDecl* RBRACE
    ;

// Ejemplo: stock : int;
perceptionDecl
    : ID COLON type SEMI
    ;

// Estado interno: variables propias del agente.
stateSection
    : STATE LBRACE stateDecl* RBRACE
    ;

// Ejemplo: alertLevel : int = 0;
stateDecl
    : ID COLON type (ASSIGN literal)? SEMI
    ;

// Acciones disponibles para ejecutar desde las reglas.
actionsSection
    : ACTIONS LBRACE actionDecl* RBRACE
    ;

// Ejemplo: action restock();
actionDecl
    : ACTION ID LPAREN RPAREN SEMI
    ;

// Comportamiento: lista de reglas condicion -> accion.
behaviorSection
    : BEHAVIOR LBRACE ruleDecl* RBRACE
    ;

// Ejemplo: if stock < 10 then do restock();
ruleDecl
    : IF condition THEN DO ID LPAREN RPAREN SEMI
    ;

// Una condicion compara dos expresiones simples.
condition
    : expression comparisonOperator expression
    ;

// Las expresiones pueden ser variables declaradas o literales.
expression
    : ID
    | literal
    ;

// Operadores permitidos dentro de una condicion.
comparisonOperator
    : GT
    | LT
    | EQ
    | NEQ
    | GTE
    | LTE
    ;

// Tipos soportados por el DSL.
type
    : INT_TYPE
    | FLOAT_TYPE
    | STRING_TYPE
    | BOOL_TYPE
    ;

// Valores escritos directamente en el codigo fuente.
literal
    : INT
    | FLOAT
    | STRING
    | TRUE
    | FALSE
    ;

// ========== REGLAS DEL LEXER ==========

// Palabras clave. Van antes que ID para que ANTLR no las lea como nombres.
AGENT : 'agent';
PERCEPTIONS : 'perceptions';
STATE : 'state';
ACTIONS : 'actions';
ACTION : 'action';
BEHAVIOR : 'behavior';
IF : 'if';
THEN : 'then';
DO : 'do';

// Tipos de datos.
INT_TYPE : 'int';
FLOAT_TYPE : 'float';
STRING_TYPE : 'string';
BOOL_TYPE : 'bool';

// Literales booleanos.
TRUE : 'true';
FALSE : 'false';

// Operadores de comparacion.
GT : '>';
LT : '<';
EQ : '==';
NEQ : '!=';
GTE : '>=';
LTE : '<=';

// Simbolos de puntuacion y asignacion.
ASSIGN : '=';
COLON : ':';
SEMI : ';';
COMMA : ',';

LBRACE : '{';
RBRACE : '}';
LPAREN : '(';
RPAREN : ')';

// Literales numericos. FLOAT va antes que INT para reconocer 3.14 completo.
FLOAT : [0-9]+ '.' [0-9]+;
INT : [0-9]+;

// Literal de texto entre comillas.
STRING : '"' (~["\\] | '\\' .)* '"';

// Identificadores definidos por el usuario.
ID : [a-zA-Z_][a-zA-Z0-9_]*;

// Espacios y comentarios de linea se ignoran.
WS : [ \t\r\n]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip;
