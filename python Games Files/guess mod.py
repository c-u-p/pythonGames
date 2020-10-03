'''Modifications are :
    1. Limit is extended of the generation of random numbers to be guessed
    2. Prompts Player that, One want to play again or not
'''
from random import randint
choice = 'y'
while (choice == 'Y' or choice == 'y'):
    start = 1
    end = 1000
    value = randint(start, end)
    
    print("I'm thinking of a number between", start, "and", end)
    
    guess = None
    
    while guess != value:
        text = input("Guess the number: ")
        guess = int(text)
    
        if guess < value:
            print("The number is Higher than ", guess, ".")
        elif guess > value:
            print("The number is Lower than ", guess, ".")
    
    print("Congratulations! You guessed the right answer : ", value)
    choice = input('Do You want to play again, if Yes then enter "y" or "Y" : \n')
