'''
Task

Write a function, isItLetter or is_it_letter or IsItLetter, which tells us if a given character is a letter or not.

'''

def is_it_letter(s):
    return s.isalpha()

def test_is_it_letter():
   assert(is_it_letter('a')== True)
   print("Test 1 passed.")
   assert(is_it_letter('A')== True)
   print("Test 2 passed.")
   assert(is_it_letter('!')== False)
   print("Test 3 passed.")
   assert(is_it_letter('1')== False)
   print("Test 4 passed.")
   print("All tests passed.")

test_is_it_letter()
