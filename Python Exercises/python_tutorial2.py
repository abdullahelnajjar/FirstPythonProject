database = []
while True:

    if input('Enter Customer\'s name (Yes/No) : ').lower()[0] == 'n':
        for name in database:
            print(name)
        break
    else:
        fname, lname = input('Enter Customer Name: ').split()
        database.append({'fname': fname, 'lname': lname})


print(cust for cust in database)



