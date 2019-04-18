friends = ['kevin', 'karen', 'jim', 'jack', 'maya']
# This is a comment


friends.extend(["Creed"])
friends2 = friends.copy()

print(id(friends))

print(id(friends2))

coord = (4, 5)

print(coord[0])


# Functions ! Yaay !


def sayhi(x, y):
    return x + y


is_male = False
is_tall = False

'''
if is_male or is_tall:
    print('Your are a male or tall or both')
else:
    print('you r neither tall nor male') '''


# This function does so and so
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(3 ** 2)


# Recursive power function

def pow(num1, num2):
    if num2 == 0:
        return 1
    if num2 % 2 == 0:
        return pow(num1, num2 / 2) * pow(num1, num2 / 2)
    else:
        return num1 * pow(num1, num2 - 1)


print(pow(2, 5))
print()

'''
while True:
    try:
        number = int(input('Enter a number: '))
        print(number)
        break
    except ZeroDivisionError as err:
        print(err)
    except ValueError as err:
        print(err)
'''


'''
employee_file = open('emp.txt', 'r+')

print(employee_file.read())

employee_file.write('Added new line\n')

print(employee_file.read())

employee_file.close()
'''

from Student import Student

student1 = Student('Jim', 'Business', 3.1)

print(student1.)