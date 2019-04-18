a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 0]
b=[]

key = input('Please input key number: ')
for index in range(len(a)):
    if a[index] < int(key):
        b.append(a[index])

print(b)



print([aa for aa in a if aa<5])