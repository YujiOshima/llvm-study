from ctypes import CFUNCTYPE, c_int

import llvmlite.ir as ll
import llvmlite.binding as llvm
import ast
import lexer


class CodeGen:
    def __init__(self):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        self.builder = ll.IRBuilder()
        self.variable_table = {}
        fntype = ll.FunctionType(ll.VoidType(), [])
        self.module = ll.Module()
        self.func = ll.Function(self.module, fntype, name='main')

    def generate_Statements(self, statement_list):
        bb_entry = self.func.append_basic_block()
        self.builder.position_at_end(bb_entry)
        for s in statement_list:
            self.generate_Statement(s)
        self.builder.ret_void()
        llvm_ir = str(self.module)
        llvm_ir_parsed = llvm.parse_assembly(llvm_ir)
        print("== LLVM IR ====================")
        print(llvm_ir_parsed)
        with open("main.ll", mode="w") as f:
            f.write(str(llvm_ir_parsed))

    def generate_Statement(self, statement):
        print(statement)
        if statement.get_ast_type() == ast.TYPE_STATEMENT:
            for s in statement.get_children():
                self.generate_Statement(s)

        elif statement.get_ast_type() == ast.TYPE_ASSIGNMENT:
            self.generate_assignment(statement)
        elif statement.get_ast_type() == ast.TYPE_PRINT:
            self.generate_print(statement)

    def generate_assignment(self, statement):
        ptr = self.builder.alloca(ll.IntType(32))
        if statement.right.get_ast_type() == ast.TYPE_NUMBER:
            self.builder.store(self.generate_number(statement.right), ptr)
        elif statement.right.get_ast_type() == ast.TYPE_VARIABLE:
            self.builder.store(self.generate_variable(statement.right), ptr)
        elif statement.right.get_ast_type() == ast.TYPE_BINARY:
            self.builder.store(self.generate_binaryexpr(statement.right), ptr)
        self.variable_table[statement.left.token.value] = ptr
        return

    def generate_binaryexpr(self, statement):
        childs = statement.get_children()
        childs_ptr = []
        for c in childs:
            if c.type == ast.TYPE_NUMBER:
                childs_ptr.append(self.generate_number(c))
            else:
                childs_ptr.append(self.generate_variable(c))
        op_value = statement.op.value
        if op_value == "+":
            indexp1 = self.builder.add(childs_ptr[0], childs_ptr[1])
        elif op_value == "-":
            indexp1 = self.builder.sub(childs_ptr[0], childs_ptr[1])
        return indexp1

    def generate_print(self, statement):
        fmt = "%d\n\0"
        try:
            printf = self.module.get_global('printnum')
        except KeyError:
            ty = ll.IntType(32)
            printf_ty = ll.FunctionType(
                ll.IntType(32), [ty], var_arg=True)
            printf = ll.Function(self.module, printf_ty, name="printnum")

        # print(".args.token.type: {}".format(.args.token.type))
        if statement.args.get_ast_type() == ast.TYPE_BINARY:
            p_value = self.generate_binaryexpr(statement.args)
        else:
            if statement.args.token.type == lexer.ID:
                p_value = self.generate_variable(statement.args)

            elif statement.args.token.type == lexer.DIGIT:
                p_value = ll.Constant(ll.IntType(
                    32), statement.args.token.value)

        #print("print {}".format(arg))
        #self.builder.call(printf, [self.fmt_arg, p_value])
        self.builder.call(printf, [p_value])
        return

    def generate_number(self, statement):
        return ll.Constant(ll.IntType(32), statement.token.value)

    def generate_variable(self, statement):
        return self.builder.load(self.variable_table[statement.token.value])
