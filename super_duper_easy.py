'''
Task

Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".
'''

def problem(a):
    if type(a) == str:
        return "Error"
    else:
        return a * 50 + 6
'''
If there is an error function doesn't reach the end. It will throw an error if the tests don't match.
'''
def test_problem():
    assert problem("hello") == "Error"
    assert problem(1) == 56
    print("All tests passed".)


test_problem()
