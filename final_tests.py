
import final as f
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

def runTestGraph(tests):
    global total
    out = ""
    passed = 0
    for (G,x,y) in tests:
        win = True
        path = f.path(G,x,y)
        if path == [] and x != y:
            print("test path failed: empty path!")
            win = False
        elif path[0] != x:
            print("test %s failed:  path %s starts with %d" % (str((G,x,y)), str(path), path[0]))
            win = False
        elif path[-1] != y:
            print("test %s failed:  path %s ends with %d" % (str((G,x,y)), str(path), path[-1]))
            win = False
        i = 1
        while i < len(path) and win:
            if (path[i-1],path[i]) not in G:
                win = False
                print("test %s failed: path %s edge %s not in G" % (str((G,x,y)), str(path), str((path[i-1],path[i]))))
            i += 1
        if win:
            print("test %s passed:" % str((G,x,y)))
            passed += 1
    total += passed
    print("passed %d/5\n" % passed)

problem1 = [((100, [22, 10, 1]), [4,1,2]), \
            ((75,  [25,1]),      [3,0]),   \
            ((75,  [10,3,1]),    [7,1,2]), \
            ((20,  [1]),         [20]),    \
            ((100, [15,5,1]),    [6,2,0])]
problem2 = [([[1,2,3],[4,5,6],[7,8,9]], 45), \
            ([[],[1],[2,3]],            6),  \
            ([[],[],[]],                0),  \
            ([[1,2,3,4,5,4,5]],         24), \
            ([[1],[3],[1],[4]],         9)]
problem3 = [(([-5,0,5,20,-123], 2),       [-5, 5, -123]), \
            (([1,3,4,5,0,7], 3),          [1, 5]),        \
            (([], 1),                     []),            \
            (([1,2,3,4,5,6,7,8,9,10], 3), [1,4,7,10]),    \
            ((["a","b","c"], 1),          ["a","b","c"])]

problem4 = [(([],[]),           False), \
            (([1,2,3],[4,5,6]), False), \
            (([4,5,6],[1,2,3]), True),  \
            (([4,2,6],[1,3,3]), True),  \
            (([1,2,3],[1,2,3]), False)]

problem5 = [((100, "A"),  True),  \
            ((85,  "C"),  False), \
            ((12,  "D"),  False), \
            ((70,  "C"),  True),  \
            ((79,  "B"),  False)]
problem6 = [("Hi, I'm 12 years old.",        10), \
            ("xxzz zzxx",                     8), \
            ("55 is the speed limit at 5PM", 17), \
            ("WHY ARE WE YELLING?",           0), \
            ("i like to whisper too ",       17)]
problem7 = [("555-1212",     "five five five dash one two one two"),                         \
            ("800-555-4321", "eight zero zero dash five five five dash four three two one"), \
            ("867-5309",     "eight six seven dash five three zero nine"),                   \
            ("555-5555",     "five five five dash five five five five"),                     \
            ("123-4567",     "one two three dash four five six seven")]
problem8 = [(2,[2,1]),                      \
            (3,[3, 10, 5, 16, 8, 4, 2, 1]), \
            (4,[4, 2, 1]),                  \
            (5,[5, 16, 8, 4, 2, 1]),        \
            (6,[6, 3, 10, 5, 16, 8, 4, 2, 1])]
problem9a = [(([],        5), [5]),         \
             (([1],       0), [0,1]),       \
             (([1],       2), [1,2]),       \
             (([1,2,4,5], 3), [1,2,3,4,5]), \
             (([1,3],     2), [1,2,3])]
problem9 = [(([],[]),           []),            \
            (([1,3,5],[2,4,6]), [1,2,3,4,5,6]), \
            (([2],[1]),         [1,2]),         \
            (([],[1,2,3,4]),    [1,2,3,4]),     \
            (([1,2,3,4],[]),    [1,2,3,4])]

G1 = [(1,2),(2,3),(3,4),(2,4),(1,3),(2,1),(3,2),(4,3),(4,2),(3,1)]
G2 = [(1,2),(2,3),(3,1),(2,1),(3,2),(1,3)]
G3 = [(1,2),(2,3),(3,1),(2,1),(3,2),(1,3),(1,4),(4,1)]
G4 = [(1,2),(2,3),(3,4),(4,5),(5,1),(2,1),(3,2),(4,3),(5,4),(1,5), \
      (1,6),(2,7),(3,8),(4,9),(5,10),(6,1),(7,2),(8,3),(9,4),(10,5), \
      (6,8),(8,10),(10,7),(7,9),(9,6), (8,6),(10,8),(7,10),(9,7),(6,9)]

problem10 = [(G1,1,4), (G2,1,3), (G3,1,4), (G4,1,4), (G4,1,7)]

print("problem 1: makeChange")
runTests2(f.makeChange, problem1)
print("problem 2: sumLists")
runTests(f.sumLists, problem2)
print("problem 3: everyKth")
runTests2(f.everyKth, problem3)
print("problem 4: largerThan")
runTests2(f.largerThan, problem4)
print("problem 5: grade")
runTests2(f.grade, problem5)
print("problem 6: countLower")
runTests(f.countLower, problem6)
print("problem 7: sayPhoneNumber")
runTests(f.sayPhoneNumber, problem7)
print("problem 8: collatz")
runTests(f.collatz, problem8)
print("problem 9a: insert")
runTests2(f.insert, problem9a)
print("problem 9: merge")
runTests2(f.merge, problem9)
print("problem 10: path")
runTestGraph(problem10)

print("total passed %d/55\n" % total)
