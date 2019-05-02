
while True:
    try:
        fname, lname = input('Please enter employee name: ').split()
        break
    except ValueError:
        print('\nInput Error! Please enter proper name\n')

employees = []
employees.append({'fname': fname, 'lname': lname})


print(employees)