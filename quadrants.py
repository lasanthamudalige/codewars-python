'''
Task

Given a point in a Euclidean plane (x and y), return the quadrant the point exists in: 1, 2, 3 or 4 (integer). x and y are non-zero integers, therefore the given point never lies on the axes.

Examples:
(1, 2)     => 1
(3, 5)     => 1
(-10, 100) => 2
(-1, -9)   => 3
(19, -56)  => 4
(1, 1) => 1
(-60, -12) => 3

There are four quadrants:

    First quadrant, the quadrant in the top-right, contains all points with positive X and Y
    Second quadrant, the quadrant in the top-left, contains all points with negative X, but positive Y
    Third quadrant, the quadrant in the bottom-left, contains all points with negative X and Y
    Fourth quadrant, the quadrant in the bottom-right, contains all points with positive X, but negative
'''

def main():
    test_quadrant()

def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

'''
If there is an error function doesn't reach the end. It will show an error if the tests don't match.
'''
def test_quadrant():
    assert quadrant(1, 2) == 1 "Should be 1"
    assert quadrant(3, 5) == 1
    assert quadrant(-10, 100) == 2
    assert quadrant(-1, -9) == 3
    assert quadrant(19, -56) == 4
    assert quadrant(1, 1) == 1
    assert quadrant(-60, -12) == 3
    print("All test passed.")

main()
