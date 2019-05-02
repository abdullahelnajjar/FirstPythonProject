with open('names.txt', 'r') as open_file:
    content = {}
    for line in open_file:
        line = line.strip()
        if line in content:
            content[line] += 1
        else:
            content.update({line: 1})

print(content)
'''
with open('names2.txt', 'a+') as open_file:
    for count in range(1,10):
        open_file.write('Zizo %d \n' % count) '''