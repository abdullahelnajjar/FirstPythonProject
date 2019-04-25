with open('names.txt', 'r') as open_file:
    content = {}
    for line in open_file:
        if line[:-1] in content:
            content[line[:-1]] += 1
        elif line[:-1] is not '':
            if line[-1] != '\n':  # This if statement is to handle the last line in the file,
                # because it is not terminated by a \n
                content[line[:]] += 1
            else:
                content.update({line[:-1]: 1})



with open('names2.txt', 'a+') as open_file:
    for count in range(1,10):
        open_file.write('Zizo %d \n' % count)
