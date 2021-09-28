import codewars_test as test
from solution import solution

test.describe("Basic Tests")
test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !#apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas #!apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
test.assert_equals(solution("apples, pears # and bananas\ngrapes\navocado @apples", ["@", "!"]), "apples, pears # and bananas\ngrapes\navocado")
test.assert_equals(solution("apples, pears § and bananas\ngrapes\navocado *apples", ["*", "§"]), "apples, pears\ngrapes\navocado")
test.assert_equals(solution("", ["#", "!"]), "")
test.assert_equals(solution("#", ["#", "!"]), "")
test.assert_equals(solution("\n§", ["#", "§"]), "\n")
test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", []), "apples, pears # and bananas\ngrapes\nbananas !apples")


test.describe("Random tests")
from random import randint, shuffle
symbols=["@","#","!","?","'","^",".",",","=","-"]
fruits=["avocados","pears","apples","bananas","cherries","strawberries","oranges","lemons","watermelons"]
def test_solution(input,markers):
    res=input[:].split("\n")
    for i in range(len(res)):
        for symbol in markers:
            if symbol in res[i]: res[i]=res[i][:res[i].index(symbol)]
        res[i]=res[i].rstrip()
    return "\n".join(res)
for i in range(40):
    teststring="\n".join([" ".join([fruits[randint(0,len(fruits)-1)] if randint(1,10)<9 else symbols[randint(0,len(symbols)-1)] for i in range(randint(1,6))]) for z in range(randint(3,5))])
    shuffle(symbols)
    markers=symbols[:randint(0,len(symbols)-1)]
    test.it("Testing for solution("+repr(teststring)+", "+str(markers)+")")
    test.assert_equals(solution(teststring,markers),test_solution(teststring[:],markers),"It should work with random inputs too")