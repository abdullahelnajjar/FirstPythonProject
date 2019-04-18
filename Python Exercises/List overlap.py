import random

a = random.sample(range(30),10)
b = random.sample(range(30),10)


print(a)
print(b)

print([key for key in a if key in b])


# This is a change to check its reflection

