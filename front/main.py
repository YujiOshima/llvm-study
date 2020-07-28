from lexer import LEXER
from parser import Parser
from semantic_analysis import SemanticAnalyzer
from codegen import CodeGen
lex = LEXER()
t_lists = lex.parse("main")
parser = Parser()
s_list = parser.parse(t_lists)
#sm_a = SemanticAnalyzer()
#sm_a.analyse_statement_list(s_list)
cg = CodeGen()
cg.generate_Statements(s_list)
