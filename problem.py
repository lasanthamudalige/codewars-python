def problem(a):
    if type(a) == int:
        return a * 50 + 6
    else:
        return "Error"

def test_problem():
    assert problem("hello") == "Error"
    assert problem(1) == 56
    print("All tests passed")


test_problem()
