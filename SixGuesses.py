import os
import math
from os import system, name

def clearscr():  
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

print('**************Welcome to SIX GUESSES**************\n\n\n\n\nThink of a number between 1 and 100.\nI will try to guess your number.\nIf my guess is incorrect, \n\t\tEnter \'1\' if your number is lesser than our guess. \n\t\tEnter \'2\' if your number is greater than our guess. \n I will take a maximum of 6 guesses to find your number.')

uselessinput = input('')
clearscr()
while 1:
    guess = 64
    n = 6
    for n in range(6,0,-1):
        print('My guess is:\n', guess,'\n\n')
        print('Number of Guesses:', abs(n-6))
        ch = input('Enter \'1\' if your number is lesser than our guess.\nEnter \'2\' if your number is greater than our guess.\nEnter any other key if our guess is Correct.\n\n')

        if ch=='1': guess -= 2**(n-1)
        elif ch=='2': guess += 2**(n-1)
        else: break
        clearscr()
    clearscr()
    print('Your number is:', guess)
    uselessinput = input('')
    clearscr()

