-- Prelude is always imported by default, we're overriding it, because we're going to define these functions ourselves.
import Prelude hiding (foldr,map,or,and,filter)

-- Today we're going to take a quick tour of functional programming.
-- We'll be using the Haskell programming language to explore these ideas.

------------------------------------------------------------------
-- Functions
------------------------------------------------------------------

-- Haskell is a functional programming language, so functions are probably a good place to start.
-- We can define a function by writing
--
-- functionName :: Type
-- functionName param1 param2 ... paramN = expression
--
-- notice that there are no parentheses around the parameters.

-- The Type of a function is just like in C, C++ or Java.
-- The only difference is how we write it.

-- In math we write a function f from set A to set B as
-- f : A -> B

-- We do the same in Haskell
-- f :: a -> b means f has a parameter of type a, and returns a value of type b
-- f :: a -> b -> c means f has two parameters of type a and b, and returns something of type c.

-- let's look at some examples
addi :: Int -> Int -> Int
addi x y = x + y

avgf :: Float -> Float -> Float
avgf x y = (x + y) / 2

-- we can apply a function f to an argument x with the syntax f x

normf :: Float -> Float -> Float
normf x y = sqrt (x**2 + y**2)

-- here we're applying sqrt to the expression (x**2 + y**2)
-- We used parentheses to group the argument together, 
-- but we don't have to have parentheses around arguments.

double :: Int -> Int
double x = addi x x

-- We can also make mini functions inside our main function with the "where" clause
-- for example if we want to compute the maximum of three numbers
max3 a b c = max a (max b c)
 where max x y = if x > y then x else y

-- we can have as many of these where clauses as we want.
median a b c = a + b + c - max3 a b c - min3 a b c
 where 
  max x y = if x > y then x else y
  min x y = if x < y then x else y
  max3 x y z = max x (max y z)
  min3 x y z = min x (min y z)

-- We can do some cool things with functions.
-- First we can use *pattern matching* to get different value
-- This is defined just like it is in propositional/first order logic

isOne :: Int -> Bool
isOne 1 = True
isOne x = False

and :: Bool -> Bool -> Bool
and False False = False
and False True  = False
and True  False = False
and True  True  = True

-- Exercise:  Write a function "or" that computes (a \/ b)
or :: Bool -> Bool -> Bool
or a b = undefined

-- We can even use pattern matching to do recursion.
-- Let's use this to calculate the factorial of a number.

fac :: Int -> Int
fac 0 = 1
fac n = n * fac (n-1)

-- Notice that the first function will only run if the argument is 0
-- for any other number the second function will run.

-- Exercise: Write a function "sum" that will sum the numbers from 0 to n
sum :: Int -> Int
sum n = undefined

-- That's easy, and it looks like math, but what if we want a function with more than 1 statement?
-- The short answer is: you dont.
-- This is the first thing to notice about haskell: Everything is an expression.

-- function calls are expressions.
-- if then else, is an expression.
-- loops aren't a thing.
-- assignment isn't a thing.

-- Wait! If loops, assignment, and statements aren't in the language, why even bother with it?
-- The short answer is, we gain alot by abandoning statements.

-- We'll explore these in the rest of the lecture.

------------------------------------------------------------------
-- Types
------------------------------------------------------------------

-- We have Int's and Booleans, but what if we want more complicated types?
-- How do we make them?

-- Haskell has a very simple way to do this.
-- data typeName = Constructor Params

--                   Name   Age
data Person = Person String Int

--               Month Day Year
data Date = Date Int   Int Int

-- we can make an value of that type with 
-- Constructor Params
john = Person "John" 24
newYear = Date 1 1 17

-- Note: this isn't actually assignment even though we're using =
-- try uncommenting the following line and see what happens.
--john = Person "John" 30
-- you CAN NOT re-assign to variables.
-- It's better to think of john as a function that has 0 parameters.

-- We can even pattern match on these types.

isJohn :: Person -> Bool
isJohn (Person "John" x) = True
isJohn (Person other  x) = False


-- We can also make *disjoint unions*
-- This just means we can have more than one option for how to make a type.
-- Suppose we wanted to represent the days of the week.
data Day = Monday
         | Tuesday
         | Wednesday
         | Thursday
         | Friday
         | Saturday
         | Sunday

--We can pattern match on this as well.
isWeekend :: Day -> Bool
isWeekend Saturday = True
isWeekend Sunday   = True
isWeekend day      = False

-- In fact this is exactly how Bool is defined.
--data Bool = True | False

-- We can even make recursive types.
data BoolList = BEmpty
              | BCons Bool BoolList

-- So, what is a Bool List?
-- Either it's empty,
-- or it has a Bool on the front.
-- Let's see some example.

empty = BEmpty
b1 = BCons True BEmpty
b2 = BCons False BEmpty
b3 = BCons True (BCons False BEmpty)
b5 = BCons True (BCons True (BCons True (BCons True BEmpty)))

-- That's right, our BoolList is just a linked List.
-- How do we use this in a function?
-- Unsurprisingly you deal with recursive types using recursive functions.
--
-- let's write a function to check if the list is all True.
-- Remember every element in the Empty list is vacuously True.
-- A BoolList is all True if the first element is True, and the rest is allTrue.
allTrueB :: BoolList -> Bool
allTrueB BEmpty           = True
allTrueB (BCons True bs)  = allTrueB bs
allTrueB (BCons False bs) = False

-- Exercise: Write an anyTrue function that determines if any element is True.

anyTrueB :: BoolList -> Bool
anyTrueB = undefined

------------------------------------------------------------------
-- Polymorphism
------------------------------------------------------------------

-- Let's start off with an exercise.
-- There's a data type called a tuple.
-- For this lecture a tuple is just a pair.
-- We can make a tuple of elements using parentheses

-- a tuple of Ints
intt = (1,2)

-- a tuple of Strings
stringt = ("foo","bar")

-- a tuple of Persons
persont = (Person "John" 24, Person "John" 30)

-- Let's write a function to swap the elements in a tuple of Ints
swapi :: (Int, Int) -> (Int, Int)
swapi (a,b) = (b,a)

-- That was easy
-- Exercise:
-- write a function to swap a tuple of Bools
-- write a function to swap a tuple of (Person,Int)
swapb :: (Bool, Bool) -> (Bool, Bool)
swapb = undefined

swappi :: (Person, Int) -> (Int, Person)
swappi = undefined

-- Notice anything here?
-- There's got to be a better way to do this.
-- Fortunately there is.  It's called Polymorphism.
--
-- Polymorphism means we can use the same function for different types
-- We can write a general form for swap
-- we make a function polymorphic by using a lower case letter instead of the type.
--
-- we can write a general form for swap.
-- Exercise: finish the general version of swap.
swap :: (a,b) -> (b,a)
swap = undefined

-- Haskell has a very powerful system of polymorphism
-- we can be polymorphic in any parameter, and we can even make polymorphic data types.

data List a = Empty
            | Cons a (List a)

data Tree a = Leaf a
            | Branch (Tree a) (Tree a)


-- In fact most of the Types defined in Haskell are polymorphic.

------------------------------------------------------------------
-- Higher Order Functions
------------------------------------------------------------------

-- One of the most powerful features of haskell is the ability to pass functions as arguments to other functions.`
-- A function that takes a function as a parameter is called a higher order function.

-- Let's see how this can work on lists.

-- Haskell has a list type that's already defined as [a]
-- so [Int] is a list of Ints, and [Float] is a list of floats
-- It has two constructors [] and :
-- This is different from what we've seen before. That's because lists are very common in haskell.

-- We can  make a list with [1,2,3] or (1:2:3:[]).

-- Let's rewrite allTrue using [Bool]
--
-- allTrueB :: BoolList -> Bool
-- allTrueB Empty            = True
-- allTrueB (BCons True bs)  = allTrueB bs
-- allTrueB (BCons False bs) = False

allTrue :: [Bool] -> Bool
allTrue []         = True
allTrue (True:bs)  = allTrue bs
allTrue (False:bs) = False

-- You can see that it's pretty similar.

-- Exercise:
-- Now let's find the compliment of a list.
compliment :: [Bool] -> [Bool]
compliment xs = undefined

-- These are both very common patterns.
-- We can actually generalize them.
-- We'll do compliment first, because it's easier.
--
-- Notice that comp looks at each element of the list, and returns the opposite elemen of the list.
-- so we can define a function that can flip a single boolean.
comp :: Bool -> Bool
comp True  = False
comp False = True

-- can we make a general function that can use it?
-- it turns out we can.
-- If the list is empty then we don't do anything.
-- If it's not empty, then we apply f to the first element.
-- then we recursively call mapBool again.
mapBool :: (Bool -> Bool) -> [Bool] -> [Bool]
mapBool f []     = []
mapBool f (b:bs) = f b : map f bs

-- now complement bs = mapBool comp bs

-- We can generalise this even further, to a function that takes an a and gives us back a b.
map :: (a -> b) -> [a] -> [b]
map f []     = []
map f (x:xs) = f x : map f xs

-- What about allTrue
-- Well really we're taking all of the values of the list, and combining them.
-- How do we combine them?
-- well if we ever see a False, then it sould be False.
-- If we only see true, then it should be True.
comb :: Bool -> Bool -> Bool
comb False False = False
comb False True  = False
comb True  False = False
comb True  True  = True

-- Exercise: why did I not need to write this function?

-- So how can combind all of the values in the list?
foldBool :: (Bool -> Bool -> Bool) -> Bool -> [Bool] -> Bool
foldBool f init []     = init
foldBool f init (b:bs) = f b (foldBool f init bs)

-- Now allTrue bs = foldBool comb True bs.
-- And, again, we can genrealize this further.
foldr :: (a -> b -> b) -> b -> [a] -> b
foldr f init [] = init
foldr f init (x:xs) = f x (foldr f init xs)


-- map and foldr are very common examples of higher order functions.
-- there's also filter, this takes a function (a -> Bool), and removes any x where f x is False.
filter :: (a -> Bool) -> [a] -> [a]
filter f [] = []
filter f (x:xs) = if f x then x : filter f xs
                         else filter f xs

-- There are many other useful higher order functions, Including zipWith, scan, and takeWhile.
-- If I went through all of them, we'd be here all day.

-- Haskell also has tools for working with functions

-- haskell allows partial application.
-- That means you can make a new function by only giving some of the parameters.
-- Some examples:

square :: Int -> Int
square = (^2)

flipCols :: [[Int]] -> [[Int]]
flipCols = map reverse


-- function composition allows us to build new functions from old ones.
-- f (g x) is so common that haskell made a special . operator for it.
doNothing :: [a] -> [a]
doNothing = reverse . reverse

sumMatrix :: [[Int]] -> Int
sumMatrix = foldr (+) 0 . map (foldr (+) 0)

-- notice that we're using partial application and function composition on sumMatrix

-- This can get complicated quickly, 
-- but once you get the hang of it you can  write complex functions quickly.

transpose :: [[a]] -> [[a]]
transpose ([]:empty) = []
transpose xs         = (map head xs) : transpose (map tail xs)
 where head (x:xs) = x
       tail (x:xs) = xs

-- So, can we use these ideas to solve a real world problem?

------------------------------------------------------------------
-- Extended example
------------------------------------------------------------------

-- suppose, for some reason, you had to write a program to check if a formula in CNF was satisfiable.
-- Let's see how we could do this in haskell.
--
-- We'll represent the formula in CNF as a list of lists of strings.
-- so, (a \/ b \/ c) /\ (!a \/ !b \/ !c) is [["a","b","c"], ["!a","!b","!c"]]


-- We'll do this in two parts.
-- In the first part, given assignments for a, b, and c, we want to determine if the entire formula is true.
-- We can do this by determining if every clause has at least one True term.
-- We'll call this function value.
value :: [[String]] -> (Bool, Bool, Bool) -> Bool
value cnf (a,b,c) = everyClause (map clauseIsTrue bools)
 where 
  -- we can determine if a term in the cnf formula is true for these particular variables
  -- So if "a" is in our formula, and we passed in False for a, then lookup "a" will return False.
  lookup "a"  = a
  lookup "b"  = b
  lookup "c"  = c
  lookup "!a" = not a
  lookup "!b" = not b
  lookup "!c" = not c

  -- Exercise: 
  -- (map . map) :: (a -> b) -> [[a]] -> [[b]]
  -- It will take a matrix of a, and apply f to every element in that matrix.
  -- use (map . map) and lookup to convert cnf to a matrix of Bools.
  bools = undefined

  -- Exercise:
  -- Use foldr write a function to determine if any value in a list is True.
  -- We can use this to determine if a clause is true.
  clauseIsTrue clause = undefined

  -- Exercise:
  -- Use foldr to write a function to determine if every value in a list is true
  -- we can use this to determine if every clause is true.
  everyClause clauses = undefined


-- Finally we want to check if a cnf formula is satisfiable.
-- This is true if there is any value for a, b, and c which makes the formula True.
--
sat :: [[String]] -> Bool
sat cnf = foldr or False (map (value cnf) vars)
  where
    -- we can get all of the values for a, b, and c with a list comprehension.
    -- You can read this just list set theory notation
    -- a <- [False,True] means a is an element of the set [False,True]
    -- So, this get's all of the combinations for a,b,c
    vars = [(a,b,c) | a <- [False,True],
                      b <- [False,True],
                      c <- [False,True]]


-------------------------------------------------
-- Where to go from here
-------------------------------------------------

-- There are many great haskell resources online.
-- I recommend "Learn you a Haskell for Great Good" http://learnyouahaskell.com/
-- It's free online.
--
-- There are also many haskell communities online
-- Facebook, Google+, Reddit, StackOverflow all have communities.
--
-- PSU also has many Haskell programmers.
-- Mark Jones was the origonal author of Hugs.  He's also made many other contributions.
-- Tim Sheard made major contributions to the theory of the Haskell language.
-- Andrew Tolmach has worked on provably correct programs and optimizations for the haskell compiler.
-- Sergio Anoty is one of the creators of a functional-logic variant of Haskell called Curry.

