
#####################
# problem 0
#####################

# rewrite the isPrime function using for loops
# a number is prime if it has no divisors between 1 and itself
# isPrime : Int -> Bool
def isPrime(n):
    return False

#####################
# problem 1
#####################

# in number theory the function pi(n) counts the number of primes that are <= x.
# use the isPrime function and a for loop to write pi(n)
# Hint: if we copy all of the prime numbers to a list, then pi(n) is the length of that list

# pi : Int -> Int
def pi(n):
    return 0

#####################
# problem 2
#####################

# writes a function that transforms a list into a dictionary that inverts the list.
# so, if l = ["this", "is", "a", "list"]
# then invertList(l) should be {"this" : 0, "is" : 1, "a" : 2, "list" : 3}

# It should be the case that for any list l, index i, and element e
# if d = invertList(l)
# d[l[i]] == i
# and
# l[d[e]] == e

def invertList(l):
    return {}

#####################
# problem 3
#####################

# we can represent a database table as a list tuples.
# If we have a table with names, salaries, and departments, then we might represent it by
# employees : [(String, Int, String)]
employees = [("jill",  4000, "accounting"), \
             ("bob",   3000, "shipping"), \
             ("jack",    20, "falling down hills"), \
             ("homer",  100, "nuclear safety")]

# if we have another table with a related column, such as each person's address
# address : [(String, String)]
address = [("Jack",  "under a well"), \
           ("bob",   "1888 Madeup Pl."), \
           ("jill",  "1234 Place Dr."), \
           ("homer", "742 evergreen ter.")]

# Then, the join of two tables is a list where every tuple has all of the columns from both tables.

# empJoinAddr : [(String, Int, String, String)]
empJoinAddr = [("jill",  4000, "accounting",          "1234 Place Dr."),  \
               ("bob",   3000, "shipping",            "1888 Madeup Pl."), \
               ("jack",    20, "falling down hills",  "under a well"),    \
               ("homer",  100, "nuclear safety",      "742 evergreen ter.")]

#write a function to find the join of two tables with the structure given above.

# join : [(String, Int, String)], [(String, String)] -> [(String, Int, String, String)]
def join(table1, table2):
    return []

#####################
# problem 4
#####################

# we can make a list of all of the five character strings with the following code
# allStrings : [String]
def allStrings():
    strings = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for c1 in alpha:
        for c2 in alpha:
            for c3 in alpha:
                for c4 in alpha:
                    strings += [c1+c2+c3+c4]
    return strings

# we can also use the ceasar cipher from lecture 7
# ceasar : String, Int -> String
def ceasar(message, n):
    # letters : String
    letters = "abcdefghijklmnopqrstuvwxyz"
    # ints : {String => Int}
    ints = dict(a= 0, b= 1, c= 2, d= 3, e= 4, f= 5, g= 6, h= 7, i= 8, j= 9, \
                k=10, l=11, m=12, n=13, o=14, p=15, q=16, r=17, s=18, t=19, \
                u=20, v=21, w=22, x=23, y=24, z=25)

    newMessage = ""
    for c in message:
        newMessage += letters[(ints[c] + n) % 26]
    return newMessage


# we can use the to break a ceasar cipher for any 4 character string.
#
# write a function to compute the inverse of ceaser on four character words.

# invertCeaser : String, Int -> String
def invertCeasar(cipherText, n):
    return cipherText


