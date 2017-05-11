
% Prolog is a strange and exciting language.
% It's actually based on the ideas of first order logic.
% As we've seen you can transform many statements into the form
% ∀ x . F(x) →  G(x)
% or more generally
% ∀ x1 x2 ... F1(x1,x2,...) ∧ F2(x1,x2,...) ... → G(x1,x2,...)
%
% The question to ask at this point is "can we write programs using logic?"
%
% Prolog takes this idea and runs with it.
% You don't write statements that do things,
% instead you write a predicate, and Prolog will find values for x1,x2,... to make that predicate true.
%
% Syntactically, prolog is very simple.
% We're only allowed to write clauses like the one above.
% However, we write all of the clauses backwards.
%
% instead of 
% ∀ x. F1 ∧ F2 → G 
% we write
% G(X) :- F1(X), F2(X).
% which means
% ∀ x. G(x) ←  F1(x) ∧ F2(x)
%
% formulas in this form are called Horn Clauses.
%
% I know this seems backwords, but Writing formulas in this way will make sense in a minute.
 
 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
% Warmup
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5


% GEN 1:   ALBERTUS   lydia       ALBERT     may
%             |         |            |        |
%             +--o------+            +----o---+
%                |                        |
% GEN 2:       RALPH                   alberta    JOHN                   cleo
%                |                        |        |                      |
%                +---o--------o-------o---+        +--o-------o--------o--+
%                    |        |       |               |       |        |
% GEN 3:    joan   WAYNE    martha   NEAL           debbie  elizabeth SEAN      kathy
%             |     |                 |               |                |          |
%             +-0---+                 +-o----o-----o--+                +-o-----o-+
%               |                       |    |     |                     |     |
% GEN 4:       amy                    NATE  IAN  bethany                KYLE  DANIEL
% 

parent(albertus, ralph).
parent(lydia,    ralph).

parent(albert, alberta).
parent(may,    alberta).

parent(ralph,   neal).
parent(ralph,   wayne).
parent(ralph,   martha).
parent(alberta, neal).
parent(alberta, wayne).
parent(alberta, martha).

parent(wayne, amy).
parent(joan,  amy).

parent(neal,   nate).
parent(neal,   ian).
parent(neal,   bethany).
parent(debbie, nate).
parent(debbie, ian).
parent(debbie, bethany).

parent(john, debbie).
parent(john, sean).
parent(john, elizabeth).
parent(cleo, debbie).
parent(cleo, sean).
parent(cleo, elizabeth).

parent(sean,  kyle).
parent(sean,  daniel).
parent(kathy, kyle).
parent(kathy, daniel).

% show how to use the interpreter.

grandparent(GrandParent, Child) :- false.


ancestor(X, Z) :- false.
ancestor(X, Z) :- false.

% Just like in functional programming, 
% the biggest mistake you can make with recursion here is trying to understand it.
% We want to write relations that are true, and have prolog figure out what needs to be done.

% Question:
% We can even use logic variables in the interpreter.
% what happens when you run
% ancestor(X,ian).
% or
% ancestor(may,X).
%
% How does this relate to the tree?

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
% Lists
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

% How do you use lists in the interpreter?

app(A, B, C) :- false.

last(List,X) :- false.

prefix(Pre,List) :- false. 

% Finally lets figure out how to permuta a list.
% being able to find permutations of a list can be very handy.
% For example you can use permute to write REALLY bad sorting algorithms.

% For convenience I'm going to make a function that can append 3 lists at a time.

app3(A,B,C,D) :- app(A,B,AB), app(AB,C,D).

% Permuting a list is really hard in a language like C or Java, but the idea is pretty simple.
% There are three cases.  
% Either the list is empty, in which case the permutation is empty,
% or the list is not empty, and the permutation keeps H on the front,
% or the permutation is not empty, and H is inserted somewhere in the middle of the permutation.

permute(A, PermA) :- False.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
% Boolean formulas
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

% Just for fun let's solve the satisfiability problem from last time
% This time we'll represent the list as a list of logic variable


% First, given a list of t or f values, we need to take the "or" of the list, and the "and" of the list.
% "or" is pretty simple.  Just check and see if we have a t.
or([t|_]).
or([f|T]) :- or(T).

% for the "and", we need to take the "or" of each clause.  If all of them are true, then the whole thing is true.
and([]).
and([H|T]) :- or(H), and(T).

% Instead of directly calculating the value of a CNF formula, I'm going to convert everything from
% strings to logic variables.  So if I see a b, then I'll convert it to a B.
% To do this I'm going to need to keep track of all of the logic variables.
%
%     input       output        logic variables
value([],         [],           _).
value([[]|T],     [[]|VT],      Vars)             :- value(T,VT,Vars).
value([[a|H]|T],  [[ A|VH]|VT], [A,B,C,NA,NB,NC]) :- value([H|T],[VH|VT],[A,B,C,NA,NB,NC]).
value([[b|H]|T],  [[ B|VH]|VT], [A,B,C,NA,NB,NC]) :- value([H|T],[VH|VT],[A,B,C,NA,NB,NC]).
value([[c|H]|T],  [[ C|VH]|VT], [A,B,C,NA,NB,NC]) :- value([H|T],[VH|VT],[A,B,C,NA,NB,NC]).
value([[na|H]|T], [[NA|VH]|VT], [A,B,C,NA,NB,NC]) :- value([H|T],[VH|VT],[A,B,C,NA,NB,NC]).
value([[nb|H]|T], [[NB|VH]|VT], [A,B,C,NA,NB,NC]) :- value([H|T],[VH|VT],[A,B,C,NA,NB,NC]).
value([[nc|H]|T], [[NC|VH]|VT], [A,B,C,NA,NB,NC]) :- value([H|T],[VH|VT],[A,B,C,NA,NB,NC]).

% Finally we can write our satisfiability funciton.
% Start by converting the formula to logic variables,
% Then set each logic variable to t or f, while it's negation is the opposite,
% Finally check the value of the formula.
sat(F, [A,B,C]) :- value(F,V,[A,B,C,NA,NB,NC]),
                   permute([t,f],[A,NA]),
                   permute([t,f],[B,NB]),
                   permute([t,f],[C,NC]),
                   and(V).

% now if we call sat([[a,b,c],[na,nb,nc]], [A,B,C,NA,NB,NC]),
% Prolog will tell us if this formula is satisfiable, and all satisfying assignments.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
% Translation
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

% I'd like to end with tackling a non-trivial problem in Prolog.
% We're going to translate the english alphabet to the Japanese alphabet Hiragana.
% To do this we need to know a little bit about Japanese, and a little bit about language itself.
%
% Hiragana is a little different than our alphabet.  Letters don't represent parts of sounds like they do in english.
% They actually represent entire syllables.   Because of this Hiragana is called a syllabary.
% This is really convenient for us, because we can translate words into Hiragana characters just by knowing the syllables.

% The following table gives us a mapping from each English syllable to the Hiragana character.

%   | a  i  u  e  k
%---+---------------
% a | あ い う え お
% k | か き く け こ
% g | が ぎ ぐ げ ご
% s | さ し す せ そ
% z | ざ じ ず ぜ ぞ
% t | た ち つ て と
% d | だ ぢ づ で ど
% n | な に ぬ ね の
% m | ま み む め も
% r | ら り る れ ろ
% h | は ひ ふ へ ほ
% b | ば び ぶ べ ぼ
% p | ぱ ぴ ぷ ぺ ぽ
% y | や    ゆ    よ
% w | わ          を
% n | ん


kana(a , あ). kana( i,  い). kana( u,  う). kana( e, え). kana( o, お).
kana(ka, か). kana(ki,  き). kana(ku,  く). kana(ke, え). kana(ko, こ).
kana(ga, が). kana(gi,  ぎ). kana(gu,  ぐ). kana(ge, げ). kana(go, ご).
kana(sa, さ). kana(si,  し). kana(su,  す). kana(se, せ). kana(so, そ).
kana(za, ざ). kana(zi,  じ). kana(zu,  ず). kana(ze, ぜ). kana(zo, ぞ).
kana(ta, た). kana(ti,  ち). kana(tu,  つ). kana(te, て). kana(to, と).
kana(da, だ). kana(di,  ぢ). kana(du,  づ). kana(de, で). kana(do, ど).
kana(na, な). kana(ni,  に). kana(nu,  ぬ). kana(ne, ね). kana(no, の).
kana(ma, ま). kana(mi,  み). kana(mu,  む). kana(me, め). kana(mo, も).
kana(ra, ら). kana(ri,  り). kana(ru,  る). kana(re, れ). kana(ro, ろ).
kana(ha, は). kana(hi,  ひ). kana(hu,  ふ). kana(he, へ). kana(ho, ほ).
kana(ba, ば). kana(bi,  び). kana(bu,  ぶ). kana(be, べ). kana(bo, ぼ).
kana(pa, ぱ). kana(pi,  ぴ). kana(pu,  ぷ). kana(pe, ぺ). kana(po, ぽ).
kana(ya, や).                kana(yu,  ゆ).               kana(yo, よ).
kana(wa, わ).                                             kana(wo, を).
kana(n,  ん).

% so, the question is, no that we can translate individual syllables to hiragana, can we translate entire sentences?
% This isn't too hard to do in C or Python.
% the basic algorithm would something like

% kana = ''
% i = 0
% while i < len(s):
%     s[i] == 'a':
%       kana += 'あ'
%       i += 1
%     s[i] == 'i':
%       kana += 'い'
%       i += 1
%     ...
%

% you could be more intelligent about this by using lists and dictionaries,
% but this still isn't trivial.
%
% so how do we do this in prolog?
% First we need to convert strings to lists of characters.
% Prolog has a predicate for this called atom_chars().
% Then at the very end, we want to take our list of translated characters and put them back into a single string.

toKana(Str,KanaStr) :- atom_chars(Str,Chrs),
                       toKanaList(Chrs,KanaChrs),
                       atom_chars(KanaStr,KanaChrs).

% now we only need to translate one syllable at a time.
% There's two possibilities here.
% Either it's a single character (a, i, u, e, o, n) or it's a consonant vowel pair.
% We do basically the same thing in both cases.
% We look up the character in our kana() table, and append

toKanaList(CS, KS) :- false.


% Ok, so that wasn't THAT hard to do, but there's a problem.
% Translating to Hiragana isn't quite that simple.
% There's a few extra rules.
% し is actually shi instead of si
% じ is actually ji  instead of zi
% ち is actually chi instead of ti
% ぢ is actually ji  instead of di
% つ is actually tsu instead of tu
% づ is actually zu  instead of do
% ふ is actually fu  instead of hu
%
% for example はじめまして is [ha ji me ma shi te] and not [ha zi me ma si te]

% Question 6
% modify the kana table to account for these extra rules.

%
% Ok, but all of these are really easy fixes, we can just edit the table right?
% Well, not quite, we still have to deal with the fact that some 
% hiragana characters are 3 english characters long.
% We can fix this by adding another case, but I want to try a more prology approach.
%
% Really both the 1 character and 2 character cases of toKanaList were pretty similar
% The only thing we need to do is get the group of characters we're translating.
% So, why not just try every possible group of characters
%
% We can do this with our append trick from earlier.
% if the string we're translating is Chars, then
% app(CS,Rest,Chars) will get every prefix that we might need to translate


% Question 7 
% use the append trick to write a single predicate for toKanaList.


% Finally we have a few extra rules.
%
% If there are two consonants in a row, then we write that as one character followed by っ.
% Example; itte should be いって
%
% If a consonant is followed by a y, then it should be the i character followed by the y character.
% Example: kya should be [ki ya] or きや
%
% For, sh, ch, and j, if they're followed by a vowel, then it should be tranlated as [shi y], [chi y], or [ji i]
% Example: [su ki ja na i] should be translated as [su ki ji ya na i] or すきじやない
% toKanaList([C1,C1,C2|Chrs], [っ|KRest]) :- C1 \= n, toKanaList([C1,C2|Chrs], KRest).
% toKanaList([C1,y,C2|Chrs],  KRest)      :-          toKanaList([C1,i,y,C2|Chrs], KRest).
% toKanaList([j,C|Chrs],      [じ|KRest]) :- C \= i,  toKanaList([y,C|Chrs], KRest).
% toKanaList([s,h,C|Chrs],    [し|KRest]) :- C \= i,  toKanaList([y,C|Chrs], KRest).
% toKanaList([c,h,C|Chrs],    [ち|KRest]) :- C \= i,  toKanaList([y,C|Chrs], KRest).


