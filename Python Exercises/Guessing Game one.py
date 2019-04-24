import random

rand_num = random.randint(1, 10)
guess_iter = 0
while True:
    if guess_iter == 0:
        guess = input('Please enter a guess number between 1 and 9: ')
    if guess == 'exit':
        print('Thank you for playing')
        break
    elif int(guess) == rand_num:
        print('You guessed it right in ' + str(guess_iter+1) + ' guesses!')
        break
    elif int(guess) > rand_num:
        guess_iter += 1
        guess = input('Try a smaller number: ')
    else:
        guess_iter += 1
        guess = input('Try a bigger number: ')


