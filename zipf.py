

# Zipf's law is on odd language phenominon.
# It has to do with the frequency of words in a large body of writing.
# The idea is that if you count how often each word is used,
# and sort the words by their frequency, the results will be a harmonic sequence.

# For example if the most common words in a book are "the", "am", "I", "was", "bathtub"
# and the word "the" appeared 1000 times, then we would expect the other words to appear
# the     : 1000
# am      :  500
# I       :  333
# was     :  250
# bathtub :  200

# Vsauce did an interesting video on this.
# https://www.youtube.com/watch?v=fCn8zs912OE

# I'm a bit skeptical about this law, so lets put it to the test.
# We'll do this in 4 parts


# First, we'll take a string (representing a book) and split it up into a list of words.
# While spliting it into words we should ignore punctuation, 
# and we shouldn't add any empty strings to the list.

# def getWords : String -> [String]
def getWords(string):
    return []

# convert a single character from upper case to lower case
# toLowerCase : String -> String
def toLowerCase(c):
    return chr(ord(c) - ord("A") + ord("a"))

# Next, we'll count all of the words that we've seen so far.
# Fortunately we can do the really easily with a dictionary.

# countWords : [String] -> {String : Int}
def countWords(words):
    return {}

# Next, We'll take take that dictionary and turn it back into a list.
# This time, however, we want a list of pairs of the word count, and the word.
# from our previous example
# 
# ( 200, bathtub)
# ( 250, was)
# ( 333, I)
# ( 500, am)
# (1000, the)
#
# Finally we finish by sorting the list

# sortWords : {String : Int} -> [(Int, String)]
def sortWords(wordCounts):
    return []

# Finally, we put it all together.
# zipf : String -> [(Int, String)]
def zipf(string):
    return []


# This isn't part of the assignment
# You don't need to write anything here.
# put in a file name (in the same directory) and it will print out the 20 most common words.
def runZipf(fileName):
    words = zipf(open(fileName,'r').read())
    i = -1
    maxWord = words[-1][0]
    while -i < min(len(words), 20):
        (freq,word) = words[i]
        print("%10s:%5d => 1/%.2f" % (word,freq,maxWord/freq))
        i -= 1
    return 0


# you can test with "Moby Dick" found at http://www.gutenberg.org/files/2701/2701-0.txt
#       the:14605 => 1/1.00
#        of: 6712 => 1/2.18
#       and: 6450 => 1/2.26
#         a: 4699 => 1/3.11
#        to: 4659 => 1/3.13
#        in: 4213 => 1/3.47
#      that: 2955 => 1/4.94
#       his: 2522 => 1/5.79
#        it: 2382 => 1/6.13
#         i: 1943 => 1/7.52
#       but: 1781 => 1/8.20
#      with: 1768 => 1/8.26
#        he: 1751 => 1/8.34
#        is: 1731 => 1/8.44
#        as: 1731 => 1/8.44
#       was: 1637 => 1/8.92
#       for: 1627 => 1/8.98
#       all: 1494 => 1/9.78
#      this: 1411 => 1/10.35

# or with "Hound of the Baskervills" found at http://www.gutenberg.org/files/2852/2852-0.txt
#       the: 3496 => 1/1.00
#        of: 1715 => 1/2.04
#       and: 1685 => 1/2.07
#        to: 1487 => 1/2.35
#         i: 1465 => 1/2.39
#         a: 1363 => 1/2.56
#      that: 1143 => 1/3.06
#        it:  985 => 1/3.55
#        in:  964 => 1/3.63
#        he:  914 => 1/3.82
#       you:  894 => 1/3.91
#       was:  803 => 1/4.35
#       his:  690 => 1/5.07
#        is:  649 => 1/5.39
#      have:  547 => 1/6.39
#       had:  505 => 1/6.92
#      with:  487 => 1/7.18
#        my:  477 => 1/7.33
#        we:  462 => 1/7.57

# You can get a lot of other test cases at Project Gutenberg
