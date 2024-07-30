'''
Task

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
Examples (Input -> Output):

* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
'''

def double_chars(s):
   new_string = ""
   for letter in s:
       new_string += letter * 2

   return new_string

'''
If there is an error function doesn't reach the end. It will throw an error if the tests don't match.
'''
def test_double_char():
    assert double_chars("String") == "SSttrriinngg"
    assert double_chars("Hello World") == "HHeelllloo  WWoorrlldd"
    assert double_chars("1234!_ ") == "11223344!!__  "
    print("All tests passed.")

test_double_char()
