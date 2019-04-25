filters = ('valuable data','special data')
filtered_data = []

with open('lines.txt') as opened_file:
    for line in opened_file:
        if any(filter_ in line for filter_ in filters):
            filtered_data.append(line)

with open('filtered_Data.txt', 'w+') as f:
    for line in filtered_data:
        f.write(line)


print('done')


print(f.closed)
