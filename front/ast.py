TYPE_ASSIGMENT="assignment"
TYPE_STATEMENT="statement"
TYPE_BINAEY="binary"
TYPE_PRINT="print"
TYPE_NUMBER="number"
TYPE_VARIABLE="variable"

PRINT = "print"
EQUAL = "="
SYMBOL = ["-","+"]
DIGIT  = ["0","1","2","3","4","5","6","7","8","9"]

class BASE_AST(object):
    def __init__(self, ast_type):
        self.type=ast_type
    def get_ast_type(self):
        return self.type
    def get_childs(self):
        return []

class STATEMENT_AST(BASE_AST):
    def __init__(self):
        super().__init__(TYPE_STATEMENT)
        self.statement=None

    def __repr__(self):
        return "type {} statement ({})".format(TYPE_STATEMENT, self.statement)
    def get_childs(self):
        return [self.statement]

class ASSIGNMENT_AST(BASE_AST):
    def __init__(self, left, right):
        super().__init__(TYPE_ASSIGMENT)
        self.left = left
        self.right = right
    
    def __repr__(self):
        return "type {} left ({}) right ({})".format(TYPE_ASSIGMENT, 
                self.left,
                self.right,
                )
    def get_childs(self):
        return [self.left, self.right]

class BINARY_EXPR_AST(BASE_AST):
    def __init__(self, op, left, right):
        super().__init__(TYPE_BINAEY)
        self.op=op
        self.left=left
        self.right=right
    def __repr__(self):
        return "type {} operation ({}) left ({})right ({})".format(
                TYPE_BINAEY, 
                self.op,
                self.left,
                self.right,
                )
    def get_childs(self):
        return [self.left, self.right]

class PRINT_AST(BASE_AST):
    def __init__(self, args):
        super().__init__(TYPE_PRINT)
        self.args=args
    def __repr__(self):
        return "type {} args ({})".format(
                TYPE_PRINT,
                self.args,
                )
    def get_childs(self):
        return [self.args]

class NUMBER_AST(BASE_AST):
    def __init__(self, val):
        super().__init__(TYPE_NUMBER)
        self.token=val
    def __repr__(self):
        return "type {} token ({})".format(
                TYPE_NUMBER,
                self.token,
                )

class VARIABLE_AST(BASE_AST):
    def __init__(self, val):
        super().__init__(TYPE_VARIABLE)
        self.token=val
    def __repr__(self):
        return "type {} token ({})".format(
                TYPE_VARIABLE,
                self.token,
                )
