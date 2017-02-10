
#################################
# Problem 1
#################################

# A verb in japanese is formal if it ends with ます.
# Otherwise it is informal and will end in either る or う.
# Write a function to determine if a japanese verb is formal
# and if it is, return True.  
# You can assume all verbs are at least 2 characters long.
#
# examples:
# formal
#   "たべます
#   "いきます"
#   "はじめます"
# informal
#   "たべる"
#   "いう"
#   "はじめる"

def isFormal(verb):
    masu = "ます"
    ru = "る"
    u = "う"
    return False

#################################
# Problem 2
#################################

# Return the prime factors of 70499 in a tuple in increasing order
# for example the prime factors of 75 are (3,5,5)
# you might find the python shell useful here.
def primeFactor():
    return (0,0)

#################################
# Problem 3
#################################

# Write a function to determine if player1 beats player2 in rock paper scissors.
# beats(rock, scissors) should return True, 
# but beats(rock, rock) and beats(rock, paper) should both return False.
# we will use: 
# 0 to represent rock
# 2 to represent paper
# 5 to represent scissors
#
# examples:
# beats(rock,scissors) is True
# beats(rock,paper) is False
# beats(rock,rock) is False
rock = 0
paper = 2
scissors = 5
def beats(player1, player2):
    return False


#################################
# Problem 4
#################################

# A number larger than 1 is perfect if all of its divisors add up to the number itself.
# for example 6 is perfect and should return True, because its divisors are 
# 1, 2, and 3, and 1 + 2 + 3 == 6 
# write a function to determine if a number is perfect
# 6, 28, and 8128 are all perfect numbers.
#
# examples:
# isPerfect(6) is True
# isPerfect(28) is True
# isPerfect(8128) is True
# isPerfect(8128) is True
# isPerfect(35) is False
# isPerfect(121) is False
def isPerfect(n):
    return False

#################################
# Problem 5
#################################

# Write a function that inserts a vertical bar "|" between each character of a string
# example:
# insertBar("Test String")
# "T|e|s|t| |S|t|r|i|n|g"
# notice that there are no vertical bars on the outside of the string.
#
# examples
# insertBar("Test String") is  "T|e|s|t| |S|t|r|i|n|g"
# insertBar("a") is "a"
# insertBar("happy") is "h|a|p|p|y"
# insertBar("def") is "d|e|f"
# insertBar("hams") is "h|a|m|s"
def insertBar(string):
    return string

#################################
# Problem 6
#################################

# Write a function that removes all capital letters from a string
# remember a capital letter is anything with an ASCII value between 65 and 90
# So, the string "Hi There", should become "i here"
# ord() might be relevant here
# ord() takes a character, and returns it's ASCII value
#
# exambles:
# removeCapitals("Test String") is  "est tring"
# removeCapitals("") is ""
# removeCapitals("happy!") is "happy!"
# removeCapitals("FOOD") is ""
# removeCapitals("Hi There") is "i here"
def removeCapitals(string):
    return string

#################################
# Problem 7
#################################

# Write a function that finds the sum of the squares of all the numbers from 1 to n
# so sumOfSquares(3) should be 1*1 + 2*2 + 3*3 == 14
#
# examples:
# sumOfSquares(1) is 1
# sumOfSquares(2) is 5
# sumOfSquares(3) is 14
# sumOfSquares(5) is 55
# sumOfSquares(10) is 385
def sumOfSquares(n):
    return 0

#################################
# Problem 8
#################################

# A caesar cipher is a way to send secret messages.
# All we need to do is pick a number n, which is called the key,
# then we take our message, and move every character up by n.
# So, if the message is "abcdefg" and n is 5 we get "fghijkl".
# Write a function that encrypts the message using the caesar cipher
# with n as the key.  
# The functions toInt and toLetter will be helpful here, and their 
# descriptions are below.
# You can assume message is entirely in lower case.
#
# examples:
# caesarCipher("happy", 5) is 'mfuud'
# caesarCipher("abcdefg", 5) is 'fghijkl'
# caesarCipher("running", 20) is 'lohhcha'
# caesarCipher("broken", 10) is 'lbyuox'
# caesarCipher("wxyz", 1) is 'xyza'
def caesarCipher(message,n):
    return message

# Takes a letter in lower case and returns a number between 0 and 25 where
# a -> 0
# b -> 1
# ...
# z -> 25
def toInt(letter):
    return ord(letter) - ord("a")

# converts a number from 1 to 26 to the corresponding letter in lower case
def toLetter(integer):
    return ord(letter + ord("a"))


#################################
# Problem 9
#################################

# In a sentence a word is anything with spaces around it.
# we can use this to define a wordCount function.
# example
# "This is a sentence" has 4 words, "this", "is", "a", and "sentence".
# "I've had it with these mother #!&*$% snakes on this mother #!&*$% plane" has 13 words.
#   1    2   3  4    5      6      7       8    9  10    11     12    13
# Write a function that counts and returns the number of words in a string. 
#
# examples:
# wordCount("This is a sentence") is 4
# wordCount("I've had it with these mother #!&*$% snakes on this mother #!&*$% plane") is 13
# wordCount("This sentence has five words") is  5
# wordCount("This sentence has five words, wait, I mean 11 words, dang!") is 11
# wordCount("Why is the sky blue?") is 5
def wordCount(string):
    return -1

#################################
# Problem 10 (extra credit)
#################################

# making change
# I think our current money system is a little boring
# I want to add a new coin called the screwup, which is worth 17 cents.
# You need to write a new version of makeChange using
# pennies, nickels, dimes, screwups, and quarters.
# remember, this should give you back the fewest coins to make change for the amount
#
# question: what is the change for 34 cents?
#
# examples:
# makeChange(34) is (0, 0, 0, 2, 0)
# makeChange(100) is (0, 0, 0, 0, 4)
# makeChange(70) is (0, 0, 2, 0, 2)
# makeChange(49) is (0, 1, 1, 2, 0)
# makeChange(74) is (0, 1, 1, 2, 1)

def makeChange(amount):
    pennies  = 0
    nickels  = 0
    dimes    = 0
    screwups = 0
    quarters = 0
    return (pennies,nickels,dimes,screwups,quarters)

