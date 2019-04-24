

def isprime(num):
    return [divisor for divisor in range(1, int(num) + 1) if int(num) % divisor == 0] == [1, num]


print(isprime(int(input('Please enter a number to check if prime: '))))


