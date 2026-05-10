# Generated from grammar/AgentDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AgentDSLParser import AgentDSLParser
else:
    from AgentDSLParser import AgentDSLParser

# This class defines a complete generic visitor for a parse tree produced by AgentDSLParser.

class AgentDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AgentDSLParser#program.
    def visitProgram(self, ctx:AgentDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#agentDecl.
    def visitAgentDecl(self, ctx:AgentDSLParser.AgentDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#section.
    def visitSection(self, ctx:AgentDSLParser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#perceptionsSection.
    def visitPerceptionsSection(self, ctx:AgentDSLParser.PerceptionsSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#perceptionDecl.
    def visitPerceptionDecl(self, ctx:AgentDSLParser.PerceptionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#stateSection.
    def visitStateSection(self, ctx:AgentDSLParser.StateSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#stateDecl.
    def visitStateDecl(self, ctx:AgentDSLParser.StateDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#actionsSection.
    def visitActionsSection(self, ctx:AgentDSLParser.ActionsSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#actionDecl.
    def visitActionDecl(self, ctx:AgentDSLParser.ActionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#behaviorSection.
    def visitBehaviorSection(self, ctx:AgentDSLParser.BehaviorSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#ruleDecl.
    def visitRuleDecl(self, ctx:AgentDSLParser.RuleDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#condition.
    def visitCondition(self, ctx:AgentDSLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#expression.
    def visitExpression(self, ctx:AgentDSLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:AgentDSLParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#type.
    def visitType(self, ctx:AgentDSLParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentDSLParser#literal.
    def visitLiteral(self, ctx:AgentDSLParser.LiteralContext):
        return self.visitChildren(ctx)



del AgentDSLParser