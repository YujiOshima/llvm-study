import lexer
import ast
import sys

class Parser(object):
    def parse(self, token_lists):
        statement_list = []
        for t_list in token_lists:
            statement_list.append(self.parse_statement(t_list))
        print(statement_list)
        return statement_list

    def ret_dig_or_val(self, token):
        if token.type == lexer.DIGIT:
            return ast.NUMBER_AST(token)
        elif token.type == lexer.ID:
            return ast.VARIABLE_AST(token)

    def parse_statement(self, token_list):
        statement=ast.STATEMENT_AST()
        if token_list[0].type == lexer.PRINT:
            arg=None
            if len(token_list) == 2:
                arg = self.ret_dig_or_val(token_list[1])
            elif len(token_list) == 4:
                arg_left = self.ret_dig_or_val(token_list[1])
                arg_right = self.ret_dig_or_val(token_list[3])
                arg = ast.BINARY_EXPR_AST(token_list[2], arg_left, arg_right)
            statement.statement = ast.PRINT_AST(arg)
        elif token_list[0].type == lexer.ID and len(token_list) == 3:
            statement.statement = ast.ASSIGNMENT_AST(
                        ast.VARIABLE_AST(
                            token_list[0],
                            ),
                        self.ret_dig_or_val(
                            token_list[2],
                            ),
                        )

        return statement
