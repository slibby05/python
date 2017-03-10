import midterm2 as m
total = 0

tand  = {(False, False) : False, \
         (False, True) :  False, \
         (True,  False) : False, \
         (True,  True)  : True}
tor   = {(False, False) : False, \
         (False, True) :  True, \
         (True,  False) : True, \
         (True,  True)  : True}
teq   = {(False, False) : True, \
         (False, True) :  False, \
         (True,  False) : False, \
         (True,  True)  : True}
txor  = {(False, False) : False, \
         (False, True) :  True, \
         (True,  False) : True, \
         (True,  True)  : False}
tnand = {(False, False) : True, \
         (False, True) :  True, \
         (True,  False) : True, \
         (True,  True)  : False}

l1 = (1,"Int",1)
l0 = (0,"Int",0)
x = ("x","Var","x")

class Token:
    _type = ""
    def __init__(self,t):
        _type = t
    def isNum(self):
        return False
    def isVar(self):
        return False

class TNum(Token):
    val = 0
    def __init__(self, n):
        self.val = n
    def isNum(self):
        return True

class TVar(Token):
    name = 0
    def __init__(self, n):
        self.name = n
    def isVar(self):
        return True

ADD = Token("+")
SUB = Token("-")
MUL = Token("*")
DIV = Token("//")
MOD = Token("%")
LPAREN = Token("lparen")
RPAREN = Token("rparen")

def lex(string):
    if string == "": return []
    c = string[0]
    if c in " \t\r\n":        return lex(string[1:])
    if c == "+":              return [ADD]    + lex(string[1:])
    if c == "-":              return [SUB]    + lex(string[1:])
    if c == "*":              return [MUL]    + lex(string[1:])
    if c == "%":              return [MOD]    + lex(string[1:])
    if c == "(":              return [LPAREN] + lex(string[1:])
    if c == ")":              return [RPAREN] + lex(string[1:])
    if string[:2] == "//":    return [DIV] + lex(string[2:])
    if "a" <= c and c <= "z": return [TVar(c)] + lex(string[1:])
    if c in "0123456789":
        (num,rest) = lexNum(string)
        return [TNum(num)] + lex(rest)
    raise Exception

def lexNum(string):
    i = 0
    while i < len(string) and string[i] in "0123456789":
        i += 1
    return (int(string[:i]), string[i:])

def expr(tokens):
    (e,tokens) = term(tokens)
    while tokens != [] and tokens[0] in [ADD,SUB]:
        op = tokens[0]
        (t,tokens) = term(tokens[1:])
        if op == ADD: e = (e,"+",t)
        if op == SUB: e = (e,"-",t)
    return (e,tokens)

def term(tokens):
    (t,tokens) = factor(tokens)
    while tokens != [] and tokens[0] in [MUL,DIV]:
        op = tokens[0]
        (f,tokens) = factor(tokens[1:])
        if op == MUL: t = (t,"*",f)
        if op == DIV: t = (t,"//",f)
    return (t,tokens)

def factor(tokens):
    if tokens[0].isNum():
        n = tokens[0].val
        return ((n,"Int",n), tokens[1:])

    if tokens[0].isVar():
        x = tokens[0].name
        return ((x,"Var",x), tokens[1:])

    if tokens[0] == LPAREN:
        (e,tokens) = expr(tokens[1:])
        if tokens[0] == RPAREN:
            return (e,tokens[1:])

    raise Exception


def parse(string):
    #try:
        (e,ts) = expr(lex(string))
        if ts == []:
            return e

        raise Exception
    #except Exception:
    #    print(str(Exception))
    #    print("Error; %s isn't a valid expression" % string)

def show(e):
    (e1,op,e2) = e
    if op == "Int":
        return str(e1)
    if op == "Var":
        return e1
    if op in ["+","-"]:
        return show(e1) + op + show(e2)
    if op in ["*","//"]:
        se1 = show(e1)
        se2 = show(e2)
        if e1[1] == "+": se1 = "("+se1+")"
        if e2[1] == "+": se2 = "("+se2+")"
        return se1 + op + se2

def runTests(f, tests):
    global total
    out = ""
    passed = 0
    for (i,o) in tests:
        if f(i) == o:
            print("test \"%s\" passed:" % str(i))
            passed += 1
        else:
            print("test \"%s\" failed: you said \"%s\", it should have been \"%s\"" % (str(i), f(i), o))
    total += passed
    print("passed %d/5\n" % passed)


def iso(a,b):
    for x in a:
        if x not in b:
            return False
    for x in b:
        if x not in a:
            return False
    return True

def runTestsIso(f, tests):
    global total
    out = ""
    passed = 0
    for (i,o) in tests:
        if iso(f(i), o):
            print("test \"%s\" passed:" % str(i))
            passed += 1
        else:
            print("test \"%s\" failed: you said \"%s\", it should have been \"%s\"" % (str(i), f(i), o))
    total += passed
    print("passed %d/5\n" % passed)
def runTestsf(f, tests):
    global total
    out = ""
    passed = 0
    for ((i,n),o) in tests:
        if f(i) == o:
            print("test \"%s\" passed:" % n)
            passed += 1
        else:
            print("test \"%s\" failed: you said \"%s\", it should have been \"%s\"" % (n, f(i), o))
    total += passed
    print("passed %d/5\n" % passed)

def runTestsExpr(f, tests):
    global total
    out = ""
    passed = 0
    for (i,o) in tests:
        if f(i) == o:
            print("test \"%s\" passed:" % show(i))
            passed += 1
        else:
            print("test \"%s\" failed: you said \"%s\", it should have been \"%s\"" % (show(i), show(f(i)), show(o)))
    total += passed
    print("passed %d/5\n" % passed)

def runTests2(f, tests):
    global total
    out = ""
    passed = 0
    for ((i1,i2),o) in tests:
        if f(i1,i2) == o:
            print("test %s passed:" % str((i1,i2)))
            passed += 1
        else:
            print("test %s failed: you said \"%s\", it should have been \"%s\"" % (str((i1,i2)), f(i1,i2), o))
    total += passed
    print("passed %d/5\n" % passed)

def runTests3f(f, tests):
    global total
    out = ""
    passed = 0
    for ((i1,n,i2,i3),o) in tests:
        if f(i1,i2,i3) == o:
            print("test %s passed:" % str((n,i2,i3)))
            passed += 1
        else:
            print("test %s failed: you said \"%s\", it should have been \"%s\"" % (str((n,i2,i3)), str(f(i1,i2,i3)), str(o)))
    total += passed
    print("passed %d/5\n" % passed)

def mul(x,y):
    return x * y

problem2 = [([("Steven", 80), ("David", 50), ("Karen", 20)], 50), \
            ([("a",1),("b",2),("c",3),("d",4),("e",5)], 3), \
            ([("unit",123)],123), \
            ([("a",-2),("b",-1),("c",0),("d",1),("e",2)], 0), \
            ([("",9),("",9),("",9),("",9),("",9)], 9)]
problem3 = [([1,2,3,4,5],[5,4,3,2,1]), \
            ([],[]), \
            (list(range(10)),list(range(9,-1,-1))), \
            ([6,28,8128,35,121],[121,35,8128,28,6]), \
            ([8,6,4,2],[2,4,6,8])]
problem4 = [(1,{1:1}), \
            (2,{1:1,4:2}), \
            (3,{1:1,4:2,9:3}), \
            (4,{1:1,4:2,9:3,16:4}), \
            (6,{1:1,4:2,9:3,16:4,25:5,36:6})]
problem5 = [({1:1,4:2,9:3,16:4,25:5,36:6},[1,2,3,4,5,6]), \
            ({1:"a",2:"b"},["a","b"]), \
            ({"a":1,"b":2},[1,2]), \
            ({1:{},2:{"a":"a"}},[{},{"a":"a"}]), \
            ({1:[],2:[]}, [[],[]])]
problem6 = [((lambda x: x*x,            "square()", [1,2,3,4,5], 4),   2), \
            ((lambda x: x*x,            "square()", [1,2,3,4,5], 16),  4), \
            ((lambda x: chr(ord(x)+32), "lower()",  "ABCDEFG",   "d"), "D"), \
            ((lambda x: chr(ord(x)-32), "upper()",  "abcdefg",   "D"), "d"), \
            ((ord,                      "ord()",    "abcdefg",   103), "g")]
problem7 = [(("leaf","leaf"),True), \
            ((("leaf","branch","leaf"),("leaf","branch","leaf")),True), \
            (((("leaf","branch","leaf"),"branch","leaf"),("leaf","branch",("leaf","branch","leaf"))),True), \
            (((("leaf","branch","leaf"),"branch","leaf"),(("leaf","branch","leaf"),"branch","leaf")),False), \
            ((("leaf","branch","leaf"),"leaf"),False)]
problem8 = [("hello","HELLO"), \
            ("goodbye","GOODBYE"), \
            ("amidoneyet","AMIDONEYET"), \
            ("horseshoe","HORSESHOE"), \
            ("sleepisoverrated","SLEEPISOVERRATED")]
problem9 = [((lambda x,y: x and y, "and"), tand), \
            ((lambda x,y: x or y, "or"), tor), \
            ((lambda x,y: x == y, "eq"), teq), \
            ((lambda x,y: x != y, "xor"), txor), \
            ((lambda x,y: not (x and y), "nand"), tnand)]
problem10 = [(parse("1*(3+x)"),parse("3+x")), \
             (parse("0+x+7"),parse("x+7")), \
             (parse("2+x+7"),parse("9+x")), \
             (parse("x+x+x"),parse("3*x")), \
             (parse("x-x"),parse("0"))]


print("problem 2: averageGrade")
runTests(m.averageGrade, problem2)
print("problem 3: reverse")
runTests(m.reverse, problem3)
print("problem 4: sqrtDict")
runTests(m.sqrtDict, problem4)
print("problem 5: getValues")
runTestsIso(m.getValues, problem5)
print("problem 6: invert")
runTests3f(m.invert, problem6)
print("problem 7: symmetric")
runTests2(m.symmetric, problem7)
print("problem 8: toUpper")
runTests(m.toUpper, problem8)
print("problem 9: truthTable")
runTestsf(m.truthTable, problem9)
print("problem 10: simplify")
runTestsExpr(m.simplify, problem10)

print("total passed %d/45\n" % total)

