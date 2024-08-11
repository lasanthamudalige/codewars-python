'''
Task

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Input = ["Ryan", "Kieran", "Jason", "Yous"]
Output = ["Ryan", "Yous"]

Input = ["Peter", "Stephen", "Joe"]
Output = []

Input strings will only contain letters. Note: keep the original order of the names in the output.
'''

def friend(x):
    friends = []
    for name in x:
        letter_count = 0
        for letter in name:
            letter_count += 1
        if letter_count == 4:
            friends.append(name)

    return friends

def test_friend():
    assert(friend(["Ryan", "Kieran", "Jason", "Yous"]) == ["Ryan", "Yous"])
    print("Test 1 passed.")
    assert(friend(["Ryan", "Kieran", "Mark",]) == ["Ryan", "Mark"])
    print("Test 2 passed.")
    assert(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]) == ["Ryan"])
    print("Test 3 passed.")
    assert(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]) == ["Jimm", "Cari", "aret"])
    print("Test 4 passed.")
    print("All tests passed.")

test_friend()
