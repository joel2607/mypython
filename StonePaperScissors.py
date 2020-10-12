from random import randint
from os import system
from time import sleep



def getinput():
    print('1 -------- STONE')
    print('2 -------- PAPER')
    print('3 -------- SCISSORS\n\n')
    inpt = 0
    while 1:
        try:  
            inpt = int(input('Enter Number\n\t\t'))
        except:
            pass
        if inpt in range(1,4):
            break
        else:
            print('Please Enter Valid Input.')
            continue
    return inpt-1
    

def showcomp():
    print('You have chosen:\n\t\t\t', choice[user])
    print('Computer has chosen:\n\t\t\t', choice[comp])

def score():
    global userscore
    global compscore
    if comp == user:
        print('\n\n\t\t\tNo points.')
    elif comp == 0 and user == 2:
        compscore += 1
        print('\n\n\t\t\tCOMPUTER GETS A POINT!')

    elif comp == 1 and user == 0:
        compscore += 1
        print('\n\n\t\t\tCOMPUTER GETS A POINT!')

    elif comp == 2 and user == 1:
        compscore += 1
        print('\n\n\t\t\tCOMPUTER GETS A POINT!')

    elif comp == 2 and user == 0:
        userscore += 1
        print('\n\n\t\t\tYOU GET A POINT!')

    elif comp == 0 and user == 1:
        userscore += 1
        print('\n\n\t\t\tYOU GET A POINT!')

    elif comp == 1 and user == 2:
        userscore += 1
        print('\n\n\t\t\tYOU GET A POINT!')

    else:
        print('Why are you reading this. This will never happen!')                                      

def checkwin(usrscr,compscr):
    if usrscr == 5:
        return -1
    elif compscr == 5:
        return 0
    else:
        return 1

def showwin():
    if checkwin(userscore,compscore) == 1:
        pass
    elif checkwin(userscore,compscore) == 0:
        print('\n\t\t\tComputer has won the game!')
        print('\n\n\t\t\t\tO O\n\t\t\t _ \n')
    elif checkwin(userscore,compscore) == -1:
        print('\n\t\t\t****YOU HAVE WON THE GAME****')
        print('\n\n\t\t\t\tO O\n\t\t\t U \n')
    else:
        print('Why are you reading this. This will never happen!')
while 1:
    userscore = 0
    compscore = 0
    while checkwin(userscore,compscore) == 1:
        
        choice = ('Stone', 'Paper', 'Scissor')
        print('**********STONE-PAPER-SCISSORS**********\n') 
        user = getinput()
        comp = randint(0,2)
        showcomp()
        score()
        print('\nYour Score:', userscore, '\nComputer Score', compscore)
        checkwin(userscore,compscore)
        showwin()
        a = input('')
        system('cls')
        