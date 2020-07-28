SYMBOL="SYMBOL"
PRINT="PRINT"
DIGIT="DIGIT"
ID="ID"

class Token:
    type=""
    value=""
    def __init__(self, t_type, value):
        self.type = t_type
        self.value = value
    def __repr__(self):
        return "TokenType: {} Value: {}".format(self.type, self.value)

def appendToken(ttype, value, token_list):
    if ttype!="" and value !="":
        if value == "print":
            ttype=PRINT
        token_list.append(Token(ttype, value)) 
    return
class LEXER(object):
    def parse(self, file_name):
        with open(file_name) as f:
            #lines = f.readlines()
            t_lists=[]

            for l in f:
                begin = True
                cur_token=""
                ttype=""
                t_lists.append([])
                l=l.strip()
                for lc in l:
                    if lc.isdigit() and (begin or ttype==DIGIT):
                        cur_token+=lc
                        ttype=DIGIT
                        begin=False
                    elif lc in ["+", "-", "="]:
                        appendToken(ttype, cur_token, t_lists[-1])
                        appendToken(SYMBOL, lc, t_lists[-1])
                        begin=True
                        cur_token=""
                    elif lc.isspace():
                        appendToken(ttype, cur_token, t_lists[-1])
                        begin=True
                        cur_token=""
                    else:
                        ttype=ID
                        cur_token+=lc
                        begin=False
                if ttype==DIGIT:
                    cur_token = int(cur_token)
                appendToken(ttype, cur_token, t_lists[-1])
        print(t_lists)
        return t_lists
