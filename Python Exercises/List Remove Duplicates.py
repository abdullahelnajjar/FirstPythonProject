def remove_duplicates(list):
    y = []
    for item in list:
        if item not in y:
            y.append(item)
    return y


def remove_duplicates_sets(l):
    return list(set(l))


a = [1, 1, 2, 3, 5, 8, 13, 21, 1, 34, 55, 89, 21, 5, 8]

print(remove_duplicates(a))
print(remove_duplicates_sets(a))

print(set(a))
