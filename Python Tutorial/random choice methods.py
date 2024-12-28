import random

mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights = [10, 1, 1], k = 14))

"""
Return a list with 14 items.
The list should contain a randomly selection of the values from a specified list, and there should be 10 times higher possibility to select "apple" than the other two:


"""