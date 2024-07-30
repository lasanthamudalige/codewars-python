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

# This function is to test the whatday function
def main():
    test_whatday()

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
If there is an error function doesn't reach the end. It will show an error if the tests don't match.
'''
def test_whatday():
    assert whatday(1) == "Sunday"
    assert whatday(2) == "Monday"
    assert whatday(3) == "Tuesday"
    assert whatday(4) == "Wednesday"
    assert whatday(5) == "Thursday"
    assert whatday(6) == "Friday"
    assert whatday(7) == "Saturday"
    print("All test passed.")

main()
