# Generated from grammar/AgentDSL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,140,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,4,0,34,8,0,11,0,12,0,35,1,0,1,0,1,1,1,1,
        1,1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,
        55,8,2,1,3,1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,5,1,5,1,5,5,5,75,8,5,10,5,12,5,78,9,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,3,6,87,8,6,1,6,1,6,1,7,1,7,1,7,5,7,94,8,7,10,7,12,
        7,97,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,110,8,9,
        10,9,12,9,113,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,12,1,12,3,12,132,8,12,1,13,1,13,1,14,
        1,14,1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,0,3,1,0,16,21,1,0,10,13,2,0,14,15,30,32,134,0,33,1,0,0,0,2,
        39,1,0,0,0,4,54,1,0,0,0,6,56,1,0,0,0,8,66,1,0,0,0,10,71,1,0,0,0,
        12,81,1,0,0,0,14,90,1,0,0,0,16,100,1,0,0,0,18,106,1,0,0,0,20,116,
        1,0,0,0,22,125,1,0,0,0,24,131,1,0,0,0,26,133,1,0,0,0,28,135,1,0,
        0,0,30,137,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,35,1,0,0,0,35,
        33,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,5,0,0,1,38,1,1,0,0,
        0,39,40,5,1,0,0,40,41,5,33,0,0,41,45,5,26,0,0,42,44,3,4,2,0,43,42,
        1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,
        47,45,1,0,0,0,48,49,5,27,0,0,49,3,1,0,0,0,50,55,3,6,3,0,51,55,3,
        10,5,0,52,55,3,14,7,0,53,55,3,18,9,0,54,50,1,0,0,0,54,51,1,0,0,0,
        54,52,1,0,0,0,54,53,1,0,0,0,55,5,1,0,0,0,56,57,5,2,0,0,57,61,5,26,
        0,0,58,60,3,8,4,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,
        1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,27,0,0,65,7,1,0,0,0,
        66,67,5,33,0,0,67,68,5,23,0,0,68,69,3,28,14,0,69,70,5,24,0,0,70,
        9,1,0,0,0,71,72,5,3,0,0,72,76,5,26,0,0,73,75,3,12,6,0,74,73,1,0,
        0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,
        1,0,0,0,79,80,5,27,0,0,80,11,1,0,0,0,81,82,5,33,0,0,82,83,5,23,0,
        0,83,86,3,28,14,0,84,85,5,22,0,0,85,87,3,30,15,0,86,84,1,0,0,0,86,
        87,1,0,0,0,87,88,1,0,0,0,88,89,5,24,0,0,89,13,1,0,0,0,90,91,5,4,
        0,0,91,95,5,26,0,0,92,94,3,16,8,0,93,92,1,0,0,0,94,97,1,0,0,0,95,
        93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,5,27,
        0,0,99,15,1,0,0,0,100,101,5,5,0,0,101,102,5,33,0,0,102,103,5,28,
        0,0,103,104,5,29,0,0,104,105,5,24,0,0,105,17,1,0,0,0,106,107,5,6,
        0,0,107,111,5,26,0,0,108,110,3,20,10,0,109,108,1,0,0,0,110,113,1,
        0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,111,1,
        0,0,0,114,115,5,27,0,0,115,19,1,0,0,0,116,117,5,7,0,0,117,118,3,
        22,11,0,118,119,5,8,0,0,119,120,5,9,0,0,120,121,5,33,0,0,121,122,
        5,28,0,0,122,123,5,29,0,0,123,124,5,24,0,0,124,21,1,0,0,0,125,126,
        3,24,12,0,126,127,3,26,13,0,127,128,3,24,12,0,128,23,1,0,0,0,129,
        132,5,33,0,0,130,132,3,30,15,0,131,129,1,0,0,0,131,130,1,0,0,0,132,
        25,1,0,0,0,133,134,7,0,0,0,134,27,1,0,0,0,135,136,7,1,0,0,136,29,
        1,0,0,0,137,138,7,2,0,0,138,31,1,0,0,0,9,35,45,54,61,76,86,95,111,
        131
    ]

class AgentDSLParser ( Parser ):

    grammarFileName = "AgentDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'agent'", "'perceptions'", "'state'", 
                     "'actions'", "'action'", "'behavior'", "'if'", "'then'", 
                     "'do'", "'int'", "'float'", "'string'", "'bool'", "'true'", 
                     "'false'", "'>'", "'<'", "'=='", "'!='", "'>='", "'<='", 
                     "'='", "':'", "';'", "','", "'{'", "'}'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "AGENT", "PERCEPTIONS", "STATE", "ACTIONS", 
                      "ACTION", "BEHAVIOR", "IF", "THEN", "DO", "INT_TYPE", 
                      "FLOAT_TYPE", "STRING_TYPE", "BOOL_TYPE", "TRUE", 
                      "FALSE", "GT", "LT", "EQ", "NEQ", "GTE", "LTE", "ASSIGN", 
                      "COLON", "SEMI", "COMMA", "LBRACE", "RBRACE", "LPAREN", 
                      "RPAREN", "FLOAT", "INT", "STRING", "ID", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_agentDecl = 1
    RULE_section = 2
    RULE_perceptionsSection = 3
    RULE_perceptionDecl = 4
    RULE_stateSection = 5
    RULE_stateDecl = 6
    RULE_actionsSection = 7
    RULE_actionDecl = 8
    RULE_behaviorSection = 9
    RULE_ruleDecl = 10
    RULE_condition = 11
    RULE_expression = 12
    RULE_comparisonOperator = 13
    RULE_type = 14
    RULE_literal = 15

    ruleNames =  [ "program", "agentDecl", "section", "perceptionsSection", 
                   "perceptionDecl", "stateSection", "stateDecl", "actionsSection", 
                   "actionDecl", "behaviorSection", "ruleDecl", "condition", 
                   "expression", "comparisonOperator", "type", "literal" ]

    EOF = Token.EOF
    AGENT=1
    PERCEPTIONS=2
    STATE=3
    ACTIONS=4
    ACTION=5
    BEHAVIOR=6
    IF=7
    THEN=8
    DO=9
    INT_TYPE=10
    FLOAT_TYPE=11
    STRING_TYPE=12
    BOOL_TYPE=13
    TRUE=14
    FALSE=15
    GT=16
    LT=17
    EQ=18
    NEQ=19
    GTE=20
    LTE=21
    ASSIGN=22
    COLON=23
    SEMI=24
    COMMA=25
    LBRACE=26
    RBRACE=27
    LPAREN=28
    RPAREN=29
    FLOAT=30
    INT=31
    STRING=32
    ID=33
    WS=34
    COMMENT=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AgentDSLParser.EOF, 0)

        def agentDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentDSLParser.AgentDeclContext)
            else:
                return self.getTypedRuleContext(AgentDSLParser.AgentDeclContext,i)


        def getRuleIndex(self):
            return AgentDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AgentDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.agentDecl()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 37
            self.match(AgentDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGENT(self):
            return self.getToken(AgentDSLParser.AGENT, 0)

        def ID(self):
            return self.getToken(AgentDSLParser.ID, 0)

        def LBRACE(self):
            return self.getToken(AgentDSLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentDSLParser.RBRACE, 0)

        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentDSLParser.SectionContext)
            else:
                return self.getTypedRuleContext(AgentDSLParser.SectionContext,i)


        def getRuleIndex(self):
            return AgentDSLParser.RULE_agentDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentDecl" ):
                listener.enterAgentDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentDecl" ):
                listener.exitAgentDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentDecl" ):
                return visitor.visitAgentDecl(self)
            else:
                return visitor.visitChildren(self)




    def agentDecl(self):

        localctx = AgentDSLParser.AgentDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_agentDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(AgentDSLParser.AGENT)
            self.state = 40
            self.match(AgentDSLParser.ID)
            self.state = 41
            self.match(AgentDSLParser.LBRACE)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 92) != 0):
                self.state = 42
                self.section()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(AgentDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def perceptionsSection(self):
            return self.getTypedRuleContext(AgentDSLParser.PerceptionsSectionContext,0)


        def stateSection(self):
            return self.getTypedRuleContext(AgentDSLParser.StateSectionContext,0)


        def actionsSection(self):
            return self.getTypedRuleContext(AgentDSLParser.ActionsSectionContext,0)


        def behaviorSection(self):
            return self.getTypedRuleContext(AgentDSLParser.BehaviorSectionContext,0)


        def getRuleIndex(self):
            return AgentDSLParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection" ):
                return visitor.visitSection(self)
            else:
                return visitor.visitChildren(self)




    def section(self):

        localctx = AgentDSLParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_section)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.perceptionsSection()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.stateSection()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.actionsSection()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.behaviorSection()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PerceptionsSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERCEPTIONS(self):
            return self.getToken(AgentDSLParser.PERCEPTIONS, 0)

        def LBRACE(self):
            return self.getToken(AgentDSLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentDSLParser.RBRACE, 0)

        def perceptionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentDSLParser.PerceptionDeclContext)
            else:
                return self.getTypedRuleContext(AgentDSLParser.PerceptionDeclContext,i)


        def getRuleIndex(self):
            return AgentDSLParser.RULE_perceptionsSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPerceptionsSection" ):
                listener.enterPerceptionsSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPerceptionsSection" ):
                listener.exitPerceptionsSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPerceptionsSection" ):
                return visitor.visitPerceptionsSection(self)
            else:
                return visitor.visitChildren(self)




    def perceptionsSection(self):

        localctx = AgentDSLParser.PerceptionsSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_perceptionsSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(AgentDSLParser.PERCEPTIONS)
            self.state = 57
            self.match(AgentDSLParser.LBRACE)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 58
                self.perceptionDecl()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(AgentDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PerceptionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AgentDSLParser.ID, 0)

        def COLON(self):
            return self.getToken(AgentDSLParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(AgentDSLParser.TypeContext,0)


        def SEMI(self):
            return self.getToken(AgentDSLParser.SEMI, 0)

        def getRuleIndex(self):
            return AgentDSLParser.RULE_perceptionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPerceptionDecl" ):
                listener.enterPerceptionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPerceptionDecl" ):
                listener.exitPerceptionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPerceptionDecl" ):
                return visitor.visitPerceptionDecl(self)
            else:
                return visitor.visitChildren(self)




    def perceptionDecl(self):

        localctx = AgentDSLParser.PerceptionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_perceptionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(AgentDSLParser.ID)
            self.state = 67
            self.match(AgentDSLParser.COLON)
            self.state = 68
            self.type_()
            self.state = 69
            self.match(AgentDSLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATE(self):
            return self.getToken(AgentDSLParser.STATE, 0)

        def LBRACE(self):
            return self.getToken(AgentDSLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentDSLParser.RBRACE, 0)

        def stateDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentDSLParser.StateDeclContext)
            else:
                return self.getTypedRuleContext(AgentDSLParser.StateDeclContext,i)


        def getRuleIndex(self):
            return AgentDSLParser.RULE_stateSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateSection" ):
                listener.enterStateSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateSection" ):
                listener.exitStateSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateSection" ):
                return visitor.visitStateSection(self)
            else:
                return visitor.visitChildren(self)




    def stateSection(self):

        localctx = AgentDSLParser.StateSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stateSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(AgentDSLParser.STATE)
            self.state = 72
            self.match(AgentDSLParser.LBRACE)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 73
                self.stateDecl()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(AgentDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AgentDSLParser.ID, 0)

        def COLON(self):
            return self.getToken(AgentDSLParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(AgentDSLParser.TypeContext,0)


        def SEMI(self):
            return self.getToken(AgentDSLParser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(AgentDSLParser.ASSIGN, 0)

        def literal(self):
            return self.getTypedRuleContext(AgentDSLParser.LiteralContext,0)


        def getRuleIndex(self):
            return AgentDSLParser.RULE_stateDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateDecl" ):
                listener.enterStateDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateDecl" ):
                listener.exitStateDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateDecl" ):
                return visitor.visitStateDecl(self)
            else:
                return visitor.visitChildren(self)




    def stateDecl(self):

        localctx = AgentDSLParser.StateDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stateDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(AgentDSLParser.ID)
            self.state = 82
            self.match(AgentDSLParser.COLON)
            self.state = 83
            self.type_()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 84
                self.match(AgentDSLParser.ASSIGN)
                self.state = 85
                self.literal()


            self.state = 88
            self.match(AgentDSLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionsSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTIONS(self):
            return self.getToken(AgentDSLParser.ACTIONS, 0)

        def LBRACE(self):
            return self.getToken(AgentDSLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentDSLParser.RBRACE, 0)

        def actionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentDSLParser.ActionDeclContext)
            else:
                return self.getTypedRuleContext(AgentDSLParser.ActionDeclContext,i)


        def getRuleIndex(self):
            return AgentDSLParser.RULE_actionsSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionsSection" ):
                listener.enterActionsSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionsSection" ):
                listener.exitActionsSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionsSection" ):
                return visitor.visitActionsSection(self)
            else:
                return visitor.visitChildren(self)




    def actionsSection(self):

        localctx = AgentDSLParser.ActionsSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_actionsSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(AgentDSLParser.ACTIONS)
            self.state = 91
            self.match(AgentDSLParser.LBRACE)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 92
                self.actionDecl()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(AgentDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTION(self):
            return self.getToken(AgentDSLParser.ACTION, 0)

        def ID(self):
            return self.getToken(AgentDSLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(AgentDSLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AgentDSLParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(AgentDSLParser.SEMI, 0)

        def getRuleIndex(self):
            return AgentDSLParser.RULE_actionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionDecl" ):
                listener.enterActionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionDecl" ):
                listener.exitActionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionDecl" ):
                return visitor.visitActionDecl(self)
            else:
                return visitor.visitChildren(self)




    def actionDecl(self):

        localctx = AgentDSLParser.ActionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_actionDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(AgentDSLParser.ACTION)
            self.state = 101
            self.match(AgentDSLParser.ID)
            self.state = 102
            self.match(AgentDSLParser.LPAREN)
            self.state = 103
            self.match(AgentDSLParser.RPAREN)
            self.state = 104
            self.match(AgentDSLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BehaviorSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEHAVIOR(self):
            return self.getToken(AgentDSLParser.BEHAVIOR, 0)

        def LBRACE(self):
            return self.getToken(AgentDSLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AgentDSLParser.RBRACE, 0)

        def ruleDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentDSLParser.RuleDeclContext)
            else:
                return self.getTypedRuleContext(AgentDSLParser.RuleDeclContext,i)


        def getRuleIndex(self):
            return AgentDSLParser.RULE_behaviorSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBehaviorSection" ):
                listener.enterBehaviorSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBehaviorSection" ):
                listener.exitBehaviorSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBehaviorSection" ):
                return visitor.visitBehaviorSection(self)
            else:
                return visitor.visitChildren(self)




    def behaviorSection(self):

        localctx = AgentDSLParser.BehaviorSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_behaviorSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(AgentDSLParser.BEHAVIOR)
            self.state = 107
            self.match(AgentDSLParser.LBRACE)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 108
                self.ruleDecl()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(AgentDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(AgentDSLParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(AgentDSLParser.ConditionContext,0)


        def THEN(self):
            return self.getToken(AgentDSLParser.THEN, 0)

        def DO(self):
            return self.getToken(AgentDSLParser.DO, 0)

        def ID(self):
            return self.getToken(AgentDSLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(AgentDSLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AgentDSLParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(AgentDSLParser.SEMI, 0)

        def getRuleIndex(self):
            return AgentDSLParser.RULE_ruleDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleDecl" ):
                listener.enterRuleDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleDecl" ):
                listener.exitRuleDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleDecl" ):
                return visitor.visitRuleDecl(self)
            else:
                return visitor.visitChildren(self)




    def ruleDecl(self):

        localctx = AgentDSLParser.RuleDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ruleDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(AgentDSLParser.IF)
            self.state = 117
            self.condition()
            self.state = 118
            self.match(AgentDSLParser.THEN)
            self.state = 119
            self.match(AgentDSLParser.DO)
            self.state = 120
            self.match(AgentDSLParser.ID)
            self.state = 121
            self.match(AgentDSLParser.LPAREN)
            self.state = 122
            self.match(AgentDSLParser.RPAREN)
            self.state = 123
            self.match(AgentDSLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentDSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentDSLParser.ExpressionContext,i)


        def comparisonOperator(self):
            return self.getTypedRuleContext(AgentDSLParser.ComparisonOperatorContext,0)


        def getRuleIndex(self):
            return AgentDSLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = AgentDSLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.expression()
            self.state = 126
            self.comparisonOperator()
            self.state = 127
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AgentDSLParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(AgentDSLParser.LiteralContext,0)


        def getRuleIndex(self):
            return AgentDSLParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = AgentDSLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(AgentDSLParser.ID)
                pass
            elif token in [14, 15, 30, 31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(AgentDSLParser.GT, 0)

        def LT(self):
            return self.getToken(AgentDSLParser.LT, 0)

        def EQ(self):
            return self.getToken(AgentDSLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(AgentDSLParser.NEQ, 0)

        def GTE(self):
            return self.getToken(AgentDSLParser.GTE, 0)

        def LTE(self):
            return self.getToken(AgentDSLParser.LTE, 0)

        def getRuleIndex(self):
            return AgentDSLParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperator" ):
                return visitor.visitComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOperator(self):

        localctx = AgentDSLParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(AgentDSLParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(AgentDSLParser.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(AgentDSLParser.STRING_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(AgentDSLParser.BOOL_TYPE, 0)

        def getRuleIndex(self):
            return AgentDSLParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = AgentDSLParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(AgentDSLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(AgentDSLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(AgentDSLParser.STRING, 0)

        def TRUE(self):
            return self.getToken(AgentDSLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(AgentDSLParser.FALSE, 0)

        def getRuleIndex(self):
            return AgentDSLParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = AgentDSLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516241920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





