'''
Task

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
Examples

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes

    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, and highest number is first.
'''

def high_and_low(numbers):
    lowest = 9223372036854775807 # Assign the highest number to the lowest value
    highest = -9223372036854775808 # Assign the lowest number to the highest value

    for n in numbers.split(" "):
        n = int(n) # Convert String to int type
        if n < lowest:
           lowest = n
        if n > highest:
            highest = n

    return f"{highest} {lowest}"

def test_high_and_low():
    assert(high_and_low("1 2 3 4 5") == "5 1")
    print("Test 1 passed.")
    assert(high_and_low("1 2 -3 4 5") == "5 -3")
    print("Test 2 passed.")
    assert(high_and_low("1 9 3 4 -5") == "9 -5")
    print("Test 3 passed.")
    print("All tests passed.")

test_high_and_low()
