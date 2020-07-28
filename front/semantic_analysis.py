import ast
import sys

class SemanticAnalyzer(object):
    def __init_(self):
        self.variable_table = set()

    def check_declear(self, statement):
        if statement.get_ast_type == ast.TYPE_ASSIGMENT:
            self.variable_table.append(statement.left)
        elif statement.get_ast_type == ast.TYPE_VARIABLE:
            if statement.val not in self.variable_table:
                print("parse error")
                sys.exit(1)
    def check(self, statement):
        self.check_declear(statement)

    def visit_ast(self, statement):
        self.check(statement)
        childs = statement.get_childs()
        if len(childs)==0:
            return statement
        else:
            for c in childs:
                self.visit_ast(c)
    def analyse_statement_list(self, statement_list):
        for s in statement_list:
            self.visit_ast(s)
