# on this final you're allowed to use
# len(list)
# range(start,end)
# list[start:end]
# list.append(elem)
# list.insert(elem)
# list indexing (l[i])
# list slices (l[a:b])
# binary operators (+,*,//,...)
# and keywords (for,while,in,if,...)

########################################################
# Problem 1
########################################################

# Make change for amount using the fewest coins possible.
# coins is a list of the value of each coin.
# so, if coins is [10,5,2], that means theres a 10 cent coin, a 5 cent coin, and a 2 cent coin.
# The result should be a list of how many of each coin there is in change.
# for example:
# makeChange (100, [22, 10, 1]) is [4,1,2]
# since 4*22 + 1*10 + 1*2 == 100

# You can assume that the coins will be in descending order of value (i.e. quarters, dimes, nickels, pennies),
# and that no coin is more than half of the value of the previous coin.
# This means the solution from homework 1 will work.

# makeChange : Int -> [Int] -> [Int]
def makeChange(amount, coins):
    return []

########################################################
# problem 2
########################################################

# Write a function to find the sum of a list of lists.
# example:
# sumLists([[1,2,3],[4,5,6],[1,3]]) is 25

# sumLists : [[Int]] -> Int
def sumLists(lists):
    return 0

########################################################
# problem 3
########################################################

# return a new list skipping every kth element in l.
# for example:
# everyKth([1,2,3,4,5], 2) is [1,3,5]

# everyKth : [a], Int -> [a]
def everyKth(l, k):
    return []

########################################################
# problem 4
########################################################

# Return True if ANY element in list1 is larger than the corresponding element in list2.
# for example:
# largerThan([1,2,3],[4,5,6]) is False
# largerThan([4,5,6],[1,2,3]) is True
# largerThan([0,3,1],[1,2,3]) is True because 3 is larger than 2
# largerThan([1,2,3],[1,2,3]) is False because 1 isn't larger than 1

# largerThan : [Int], [Int] -> [Int]
def largerThan(list1,list2):
    return False

########################################################
# problem 5
########################################################

# Return the if the score on a test earns the grade g.
# for example:
# grade(70,"C") is True
# grade(85,"C") is False # 85 should be a B
#
# The grades are:
# "A" - score is above 90
# "B" - score is between 80 and 90
# "C" - score is between 70 and 80
# "D" - score is between 60 and 70
# "F" - score is below 60

# grade : Int, String -> String
def grade(score,g):
    return False

########################################################
# problem 6
########################################################

# Return the number of lower case characters in a string.
# A lower case character is any character between "a" and "z".
# for example:
# countLower("Hi, I'm 12 years old.") == 10

# countLower : String -> Int
def countLower(text):
    return 0

########################################################
# problem 7
########################################################

# Write a function to convert a phone number into the words of that phone number.
# A phone number is a string containing digits and dashes.
# The result should be the digits replaced with words.
# for example:
# sayPhoneNumber("555-1212") == "five five five dash one two one two"

# hint: this would be a good place for a dictionary!
# hint2: don't worry too much about the extra space at the end. It's not worth many points.

# sayPhoneNumber: String -> String
def sayPhoneNumber(phoneNumber):
    return ""

########################################################
# problem 8
########################################################


# The Collatz conjecture is a famous conjecture in math.
# 
# The idea is that we define a function f on Ints.
# f(n) is n/2 if n is even  (notice how this is still an Int)
# f(n) is 3*n + 1 if n is odd.
#
# The conjecture is that if we repeatedly apply f to a number, then it will eventually become 1.
# First write the function f in Python.

# f : Int -> Int
def f(n):
    return 0

# now we can write a function to test the collatz conjecture
# Write a RECURSIVE function that returns the sequence of values from repeatedly applying f to a number
# for example
# collatz(5) == [5, 16, 8, 4, 2, 1]

# collatz(1) = [1]
# collatz(n) = [n] + collatz(f(n))

# Note that we don't actually know that this will ever stop running.

# collats : Int -> [Int]
def collatz(n):
    return []

########################################################
# problem 9
########################################################

# We saw in class a more efficient sort called mergesort.
# We can sort a list by splitting it in half, sorting the halves, and merging them together.
# example:
# msort([6,3,5,2,4,1]) == merge(msort([6,3,5]), msort([2,4,1])) == merge([3,5,6],[1,2,4]) == [1,2,3,4,5,6]

# if this seems a little daunting, don't worry, I've written msort for you!
def msort(l):
    if len(l) <= 1:
        return l
    n = len(l)//2
    return merge(msort(l[:n]), msort(l[n:]))

# The only thing you need to do in write the merge function.

# Before we do that, let's write an insert function.

# Insert an element x into a sorted list l without using sorted().
# for example:
# insert([1,3,7,8], 5) == [1,3,5,7,8]
def insert(l, x):
    return []

# Now we can use the fold function to merge two lists.

# fold, as defined in class
def fold(f, i, l):
    for x in l:
        i = f(i,x)
    return i


# Now use insert and fold to make our merge function.
# how do we merge two lists?
# we can insert all of the elements from one into the other.

# merge two sorted lists *using fold*.
# for example: 
# merge([1,3,5],[2,4,6]) == [1,2,3,4,5,6]
def merge(l1, l2):
    return []


########################################################
# problem 10 (extra credit)
########################################################

# A graph is a set of points connected by edges.
# We can represent a graph as a list of edges.
# So, if x and y are points, then (x,y) is the edge connecting the points.

# example:
# if we have the graph G
# 1 --- 2
# |    /|
# |   / |
# |  /  |
# | /   |
# |/    |
# 3 --- 4

G = [(1,2),(2,3),(3,4),(2,4),(1,3), \
     (2,1),(3,2),(4,3),(4,2),(3,1)]

# A path from x to y is a set of points p0,p1...pn such that p0 = x, pn = y, and (pi,pi+1) is an edge.
# This is a fancy way of saying that all the points in a path are connected by edges.
# for example:
# [1,2,4] is a path from 1 to 4, since (1,2) and (2,4) are in G

# Write a function that returns a path from x to y for a graph G.

# hints:
# We might want to write a helper function here.
# If x is a point in the graph, then [x] is a path.
# if (s, t) is an edge in G, then [s,t] is a path.
# A path from x to y is the union of a path from x to p, and a path from p to y.

# A path should not pass through the same point twice, so
# you should keep a list (or set) of points you've already seen.

# path : [(Int,Int)], Int, Int -> [Int]
def path(G,x,y):
    return []
