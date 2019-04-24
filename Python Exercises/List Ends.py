import random

def list_ends(list):
    return [list[0], list[-1]]


test = random.sample(range(30), 10)
print(test)
print(list_ends(test))
