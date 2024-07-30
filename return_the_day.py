'''
Task

Complete the function which returns the weekday according to the input number:
    1 returns "Sunday"
    2 returns "Monday"
    3 returns "Tuesday"
    4 returns "Wednesday"
    5 returns "Thursday"
    6 returns "Friday"
    7 returns "Saturday"
    Otherwise returns "Wrong, please enter a number between 1 and 7"
'''

def whatday(num):
    if num == 1:
        return "Sunday"
    elif num == 2:
        return "Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num == 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    elif num == 7:
        return "Saturday"
    else:
        return "Wrong, please enter a number between 1 and 7"

'''
If there is an error function doesn't reach the end. It will throw an error if the tests don't match.
'''
def test_whatday():
    assert whatday(1) == "Sunday"
    print("Test 1 passed.")
    assert whatday(2) == "Monday"
    print("Test 2 passed.")
    assert whatday(3) == "Tuesday"
    print("Test 3 passed.")
    assert whatday(4) == "Wednesday"
    print("Test 4 passed.")
    assert whatday(5) == "Thursday"
    print("Test 5 passed.")
    assert whatday(6) == "Friday"
    print("Test 6 passed.")
    assert whatday(7) == "Saturday"
    print("Test 7 passed.")
    print("All tests passed.")

test_whatday()
