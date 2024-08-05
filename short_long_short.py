'''
Task

Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty ( zero length ).
'''

def solution(a, b):
    string = ""
    if len(a) > len(b):
        string += b
        string += a
        string += b
    else:
        string += a
        string += b
        string += a

    return string

def test_solution():
    assert(solution('45', '1') == '1451')
    assert(solution('13', '200') == '1320013')
    assert(solution('Soon', 'Me') == 'MeSoonMe')
    assert(solution('U', 'False') == 'UFalseU')
    print("All tests passed.")


test_solution()
