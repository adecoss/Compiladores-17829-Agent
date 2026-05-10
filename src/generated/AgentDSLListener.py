# Generated from grammar/AgentDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AgentDSLParser import AgentDSLParser
else:
    from AgentDSLParser import AgentDSLParser

# This class defines a complete listener for a parse tree produced by AgentDSLParser.
class AgentDSLListener(ParseTreeListener):

    # Enter a parse tree produced by AgentDSLParser#program.
    def enterProgram(self, ctx:AgentDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#program.
    def exitProgram(self, ctx:AgentDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#agentDecl.
    def enterAgentDecl(self, ctx:AgentDSLParser.AgentDeclContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#agentDecl.
    def exitAgentDecl(self, ctx:AgentDSLParser.AgentDeclContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#section.
    def enterSection(self, ctx:AgentDSLParser.SectionContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#section.
    def exitSection(self, ctx:AgentDSLParser.SectionContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#perceptionsSection.
    def enterPerceptionsSection(self, ctx:AgentDSLParser.PerceptionsSectionContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#perceptionsSection.
    def exitPerceptionsSection(self, ctx:AgentDSLParser.PerceptionsSectionContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#perceptionDecl.
    def enterPerceptionDecl(self, ctx:AgentDSLParser.PerceptionDeclContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#perceptionDecl.
    def exitPerceptionDecl(self, ctx:AgentDSLParser.PerceptionDeclContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#stateSection.
    def enterStateSection(self, ctx:AgentDSLParser.StateSectionContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#stateSection.
    def exitStateSection(self, ctx:AgentDSLParser.StateSectionContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#stateDecl.
    def enterStateDecl(self, ctx:AgentDSLParser.StateDeclContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#stateDecl.
    def exitStateDecl(self, ctx:AgentDSLParser.StateDeclContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#actionsSection.
    def enterActionsSection(self, ctx:AgentDSLParser.ActionsSectionContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#actionsSection.
    def exitActionsSection(self, ctx:AgentDSLParser.ActionsSectionContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#actionDecl.
    def enterActionDecl(self, ctx:AgentDSLParser.ActionDeclContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#actionDecl.
    def exitActionDecl(self, ctx:AgentDSLParser.ActionDeclContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#behaviorSection.
    def enterBehaviorSection(self, ctx:AgentDSLParser.BehaviorSectionContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#behaviorSection.
    def exitBehaviorSection(self, ctx:AgentDSLParser.BehaviorSectionContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#ruleDecl.
    def enterRuleDecl(self, ctx:AgentDSLParser.RuleDeclContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#ruleDecl.
    def exitRuleDecl(self, ctx:AgentDSLParser.RuleDeclContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#condition.
    def enterCondition(self, ctx:AgentDSLParser.ConditionContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#condition.
    def exitCondition(self, ctx:AgentDSLParser.ConditionContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#expression.
    def enterExpression(self, ctx:AgentDSLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#expression.
    def exitExpression(self, ctx:AgentDSLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:AgentDSLParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:AgentDSLParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#type.
    def enterType(self, ctx:AgentDSLParser.TypeContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#type.
    def exitType(self, ctx:AgentDSLParser.TypeContext):
        pass


    # Enter a parse tree produced by AgentDSLParser#literal.
    def enterLiteral(self, ctx:AgentDSLParser.LiteralContext):
        pass

    # Exit a parse tree produced by AgentDSLParser#literal.
    def exitLiteral(self, ctx:AgentDSLParser.LiteralContext):
        pass



del AgentDSLParser