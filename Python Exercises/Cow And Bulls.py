import random


def compare_numbers(number, user_guess):
    cowbull = [0,0] #cows, then bulls
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[0]+=1
        else:
            cowbull[1]+=1
    return cowbull



if __name__=="__main__":

    number = ''.join([str(random.randint(0, 9)), str(random.randint(0, 9)), str(random.randint(0, 9)), str(random.randint(0, 9))]) #random 4 digit number
    guesses = 0

    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")
    print(number)11
    while True:
        user_guess = input("Give me your best guess!")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[0]==4:
            print("You win the game after " + str(guesses) + " guesses!\nThe number was "+str(number))
            break

        else:
            print("Your guess isn't quite right, try again.")



