'''
Task

Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
'''

def even_or_odd(number):
    if number % 2 == 1:
        return "Odd"
    else:
        return "Even"

def test_even_or_odd():
    assert even_or_odd(1) == "Odd"
    print("Test 1 passed.")
    assert even_or_odd(2) == "Even"
    print("Test 2 passed.")
    assert even_or_odd(-1) == "Odd"
    print("Test 3 passed.")
    assert even_or_odd(-2) == "Even"
    print("Test 4 passed.")
    assert even_or_odd(0) == "Even"
    print("Test 5 passed.")
    print("All tests passed.")

test_even_or_odd()
