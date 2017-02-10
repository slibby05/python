import midterm as m
from functools import reduce
rock = 0
paper = 2
scissors = 5
total = 0

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

def runTestPrime():
    global total
    if reduce(mul,m.primeFactor()) == 70499:
        print("test passed: the factors of 70499 are " + str(m.primeFactor()))
        print("passed 1/1\n")
        total += 1
    else:
        print("test failed: the factors "+str(m.primeFactor())+" produce "+ str(reduce(mul,m.primeFactor())))
        print("passed 0/1\n")

def mul(x,y):
    return x * y

problem1 = [("たべます",True), ("いきます",True), ("たべる",False), ("かう",False), ("はじめる",False)]
problem3 = [((rock,scissors),True),((paper,rock),True),((scissors,paper),True),((rock,rock),False),((paper,scissors),False)]
problem4 = [(6,True),(28,True), (8128,True), (35,False), (121,False)]
problem5 = [("Test String", "T|e|s|t| |S|t|r|i|n|g"), ("a","a"), ("happy","h|a|p|p|y"), ("def","d|e|f"), ("hams","h|a|m|s")]
problem6 = [("Test String", "est tring"), ("",""), ("happy!","happy!"), ("FOOD",""), ("Hi There","i here")]
problem7 = [(1,1),(2,5),(3,14),(5,55),(10,385)]
problem8 = [(("happy", 5), 'mfuud'), (("abcdefg", 5), 'fghijkl'), (("running", 20), 'lohhcha'), (("broken", 10), 'lbyuox'), (("wxyz", 1), 'xyza')]
problem9 = [("This is a sentence", 4), \
            ("I've had it with these mother #!&*$% snakes on this mother #!&*$% plane", 13), \
            ("This sentence has five words", 5), \
            ("This sentence has five words, wait, I mean 11 words, dang!", 11), \
            ("Why is the sky blue?", 5)]
problem10 = [(34, (0, 0, 0, 2, 0)), \
             (100, (0, 0, 0, 0, 4)), \
             (70, (0, 0, 2, 0, 2)), \
             (49, (0, 1, 1, 2, 0)), \
             (74, (0, 1, 1, 2, 1))]

print("problem 1: isFormal")
runTests(m.isFormal, problem1)
print("problem 2: primeFactor")
runTestPrime()
print("problem 3: beats")
runTests2(m.beats, problem3)
print("problem 4: isPerfect")
runTests(m.isPerfect, problem4)
print("problem 5: insertBar")
runTests(m.insertBar, problem5)
print("problem 6: removeCapitals")
runTests(m.removeCapitals, problem6)
print("problem 7: sumOfSquares")
runTests(m.sumOfSquares, problem7)
print("problem 8: caesarCipher")
runTests2(m.caesarCipher, problem8)
print("problem 9: wordCount")
runTests(m.wordCount, problem9)
print("problem 10: makeChange")
runTests(m.makeChange, problem10)

print("total passed %d/46\n" % total)
