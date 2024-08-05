'''
Task

Given three integers a, b, and c, return the largest number obtained after inserting the operators +, *, and parentheses (). In other words, try every combination of a, b, and c with the operators, without reordering the operands, and return the maximum value.
Example

With the numbers 1, 2, and 3, here are some possible expressions:

    1 * (2 + 3) = 5
    1 * 2 * 3 = 6
    1 + 2 * 3 = 7
    (1 + 2) * 3 = 9

The maximum value that can be obtained is 9.
Notes

    The numbers are always positive, in the range 1 ≤ a, b, c ≤ 10.
    You can use the same operation more than once.
    It is not necessary to use all the operators or parentheses.
    You cannot swap the operands. For example, with the given numbers, you cannot get the expression (1 + 3) * 2 = 8.

Input and Output Examples

    expressionsMatter(1, 2, 3) ==> 9, because (1 + 2) * 3 = 9.
    expressionsMatter(1, 1, 1) ==> 3, because 1 + 1 + 1 = 3.
    expressionsMatter(9, 1, 1) ==> 18, because 9 * (1 + 1) = 18.
'''

def expression_matter(a, b, c):
    # All possible expression to find the maximum value
    e1 = a+b+c
    e2 = a+b*c
    e3 = a*b+c
    e4 = (a+b)+c
    e5 = (a+b)*c
    e6 = a+(b+c)
    e7 = a+(b*c)
    e8 = (a*b)+c
    e9 = (a*b)*c
    e10 = a*(b+c)
    e11 = a*(b*c)

    # Add all the expresstions to this array
    expressions_list = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]

    # Return the highest value
    return max(expressions_list)

def test_expression_matter():
    assert(expression_matter(2, 1, 2) == 6)
    assert(expression_matter(2, 1, 1) == 4)
    assert(expression_matter(2, 2, 4) == 16)
    assert(expression_matter(3, 3, 3) == 27)
    assert(expression_matter(1, 1, 1) == 3)
    assert(expression_matter(1, 2, 3) == 9)
    assert(expression_matter(1, 3, 1) == 5)
    assert(expression_matter(2, 2, 2) == 8)
    assert(expression_matter(5, 1, 3) == 20)
    assert(expression_matter(3, 5, 7) == 105)
    assert(expression_matter(5, 6, 1) == 35)
    assert(expression_matter(1, 6, 1) == 8)
    assert(expression_matter(2, 6, 1) == 14)
    assert(expression_matter(6, 7, 1) == 48)
    assert(expression_matter(2, 10, 3) == 60)
    assert(expression_matter(1, 8, 3) == 27)
    assert(expression_matter(9, 7, 2) == 126)
    assert(expression_matter(1, 1, 10) == 20)
    assert(expression_matter(9, 1, 1) == 18)
    assert(expression_matter(10, 5, 6) == 300)
    assert(expression_matter(1, 10, 1) == 12)
    print("All tests passed.")


test_expression_matter()
