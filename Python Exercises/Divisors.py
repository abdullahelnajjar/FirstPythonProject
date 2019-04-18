

num = input('Please enter a number: ')


print('You entered the number ' + num + '\nIt\'s divisors are:' +
      str([divisor for divisor in range(1, int(num)+1) if int(num) % divisor == 0]))


