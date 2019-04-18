import datetime

name = input('Please enter your name: ')
age = input('Please enter your AGE: ')

if int(age) < 100:
    year = datetime.datetime.now().year + 100 - int(age)
    print('Hi ' + name + ' you will turn 100 in ' + str(year))
else:
    print('Hi '+ name + ' you already passed 100 years old!')



