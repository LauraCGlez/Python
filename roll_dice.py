import random

roll = random.randint(1,6)

def diceroll():
    
    guess = int(input('Guess the dice roll:\n'))

    if guess == roll:
        print('Nice, you win!')
        
    else:
        print('Keep trying!')
        diceroll()

diceroll()

