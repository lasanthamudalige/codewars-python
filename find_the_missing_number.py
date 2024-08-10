'''
Task

The following was a question that I received during a technical interview for an entry level software developer position. I thought I'd post it here so that everyone could give it a go:

You are given an unsorted array containing all the integers from 0 to 100 inclusively. However, one number is missing. Write a function to find and return this number. What are the time and space complexities of your solution?
'''

def missing_no(nums):
    nums = sorted(nums)
    for i in range(0, 101):
        try:
            if i != nums[i]:
                return i
        except IndexError: # If the missing number is 100
            return 100;

def test_missing_no():
    #Numbers from 0 to 100, but missing 5
    nums = list(range(0,101))
    nums.remove(5)
    assert(missing_no(nums) == 5)
    print("Test 1 passed.")

    nums = list(reversed(range(0,101)))
    nums.remove(10)
    assert(missing_no(nums) == 10)
    print("Test 2 passed.")

    nums = list(range(0,101))
    nums.remove(100)
    assert(missing_no(nums) == 100)
    print("Test 3 passed.")

    print("All tests passed.")


test_missing_no()
