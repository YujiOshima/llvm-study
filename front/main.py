from lexer import LEXER
from parser import Parser
lex = LEXER()
t_lists = lex.parse("main")
parser = Parser()
s_list = parser.parse(t_lists)
