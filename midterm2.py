
#########################################
# Problem 1
#########################################

# give the type of the following data structure
company = [("pie eating", [("Alison",  1230, {"cherry" : 1,    "pie" : 2,    "orange" : 3}), \
                           ("Daniel",   500, {"chocolate" : 1, "humble" : 2, "wood" : 3}), \
                           ("Tristan", 1000, {"pumpkin" : 1,   "math" : 2,   "cow" : 3})]), \
           ("pie making", [("Yubin",   1260, {"chocolate" : 1, "cow" : 2,    "cherry" : 3}), \
                           ("Steven",    60, {"pumpkin" : 1,   "math" : 2,   "wood" : 3})])]

# return the type of company as a String
# so if company = 4
# then companyType() would return "Int"
def companyType():
    return ""

#########################################
# Problem 2
#########################################

# each person in this class has a grade
# if I give you a structure for students : [(String, Int)]

# example:
# students = [("Steven", 80), ("David", 50), ("Karen", 30)]

# compute the averge grade for the class

def averageGrade(students):
    return 0

#########################################
# Problem 3
#########################################

# write a funtion that reverses a list
# reverse([1,2,3,4,5]) == [5,4,3,2,1]

# you can do this with iteration or recursion
# you CAN NOT use the list.reverse() method.
# well... You can, you just won't get any points for it.

# reverse : [a] -> [a]
def reverse(l):
    return []

#########################################
# Problem 4
#########################################

# Write a function that will construct a square root dictionary for numbers up to n.
# example:
# sqrtDict(50) == {1 : 1, 4 : 2, 9 : 3, 16 : 4, 25 : 5, 36 : 6, 49 : 7}

# We sould only add numbers that have integer square roots.
# So if i is an integer, then the dictionary should have {i*i : i} as one of the elements.

# sqrtDict : Int -> {Int => Int}
def sqrtDict(n):
    return {}

#########################################
# Problem 5
#########################################

# Write a function that takes a dictionary and returns a list of values.
# You should not use any methods on dictionarys for this.

# getValues : {k => v} -> [v]
def getValues(d):
    return []

#########################################
# Problem 6
#########################################

# we learned in class how to use brute force to invert a function
# Using the ideas from functional programing we can generalize that
#
# f is a function that has one parameter
# S is a list of possible inputs for f
# y is a possible output for f
# find an x such that x is in S, and f(x) = y
#
# invert : (a -> b), [a], b -> a
def invert(f, S, y):
    return y

#########################################
# Problem 7
#########################################

# two branch trees are symmetric if they are mirrors of eachother
# for example:
#       t1                 t2
#         branch            branch
#          /   \             /   \
#         /     \           /     \
#      branch   leaf      leaf  branch
#       /  \                     /  \
#      /    \                   /    \
#    leaf  leaf               leaf  leaf

# t1 = (("leaf","branch","leaf"), "branch", "leaf")
# t2 = ("leaf", "branch", ("leaf","branch","leaf"))

# t1 and t2 are symmetric

# write a function to determine if two trees are symmetric

# Hints: 
# we can split a tree into subtrees using
# (t1left,t1branch,t1right) = t1
#
# two leaves are symmetric
# a leaf and a branch are NOT symmetric
# two branches are symmetric if t1left is symmetric with t2right
#                           and t1right is symmetric with t2left

# symmetric : tree, tree -> Bool
def symmetric(t1, t2):
    return False


#########################################
# Problem 8
#########################################

# We can also write map for strings.
# mapString : (String -> String), String -> String
def mapString(f, string):
    newString = ""
    for c in string:
        newString += f(c)
    return newString

# Write a function that converts a character to upper case.
# hint: ord("A") is 32 less then ord("a")

# toUpperChar : String -> String
def toUpperChar(c):
    return c

# Now use mapString to convert an entire string to upper case.
# 
# example:
# toUpper("hello") = "HELLO"
# toUpper : String -> String
def toUpper(string):
    return string


#########################################
# Problem 9
#########################################

# a boolean operator is a function that takes two boolean values and returns a boolean value
# we've seen a lot of those.  "and", "or", "not", and "==" are all boolean operators.
# we can make a truth table as a dictionary from (Bool,Bool) to Bool
# so the truth table for and is
#  a | b | a and b
# ---+---+--------
#  F | F |    F
#  F | T |    F
#  T | F |    F
#  T | T |    T

# Then the truth table for "and" in dictionary form is
# {(False, False) : False, \
#  (False, True) :  False, \
#  (True,  False) : False, \
#  (True,  True)  : True}

# If f is a boolean operator, return the truth table in dictionary form of f
# truthTable : (Bool, Bool -> Bool) -> {(Bool,Bool) => Bool}
def truthTable(f):
    return {}

#########################################
# Problem 10 (extra credit)
#########################################

# if we extend that ASTs we used in homework 6 to include variables, then we can do algebra with trees.

# our trees now have 6 possible cases
# (n, "Int", n)
# (x, "Var", x)
# (e1, "+", e2)
# (e1, "-", e2)
# (e1, "*", e2)
# (e1, "//", e2)

# Now, you may remeber from math classes that you need to simplify your expressions.
# We can actually write a program to do that for us.

# I'll get you started with a simplification called constant folding
# If every both subtrees are made up of numbers then we can just evaluate them
# for example: (3 * 4 + 8) * x == 20 * x no matter what x is

# you might come up with other ways to simplify an expression
# remember the rules of algebra.
# as an example:
#  1 * (3 + x) == 3 + x

# simplify : AST -> AST
def simplify(ast):
    (t1, op, t2) = ast

    # if our AST is an Int or a Var then we can't simplify it anymore
    if op == "Int" or op == "Var":
        return ast
    
    # we can simplify the subtrees with recursive calls
    st1 = simplify(t1)
    st2 = simplify(t2)
    (t1l,op1,t1r) = st1
    (t2l,op2,t2r) = st2

    # constant folding
    # if the t1 and t2 don't contain variables
    # then we can just evaluate them.
    if op1 == "Int" and op2 == "Int":
        out = 0
        if op == "+":
            out = t1l + t2l
        if op == "*":
            out = t1l + t2l
        if op == "-":
            out = t1l + t2l
        if op == "//":
            out = t1l + t2l
        return (out, "Int", out)

    # other simplifications here ..

    # none of the simplifications applied, so just return the simplified subtrees
    return (st1, op, st2)
