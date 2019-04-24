#This function calcutlate the nth fibonacci number recursively
def fibonacci(length):
    if length == 1 or length == 2:
        return 1
    else:
        return fibonacci(length - 1) + fibonacci(length - 2)


number = int(input('Please enter how many Fibonnaci number you need: '))
print('Here is your fibonacci sequence: ' + str([fibonacci(key) for key in range(1, number+1)]))
