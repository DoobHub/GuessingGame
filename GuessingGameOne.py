'''
Generate a random number between 1 and 9 
'''
import random
from _dummy_thread import exit

print('Let the guessing game begin!!')

def Guess():
    print('A number have been generated...')
    c = random.randint(1, 9)
    k = 0
    while k < 3:
        n = 3 - k
        print(f'You have {n} life left!')
        try:
            u = int(input('Your guess: '))
        except:
            k += 1
            print('Enter only number you fool!')
            continue
        if u < 1 or u > 9:
            k += 1
            if k == 3:
                print('The computer only generate a number from 0 to 9.')
            else:
                print('The computer only generate a number from 0 to 9. Try again.')          
            continue
        elif u > c:
            k += 1
            if k == 3:
                print('Too high.')
            else:
                print('Too high. Guess again.')
            continue 
        elif u < c:
            k += 1
            if k == 3:
                print('Too low.')
            else:
                print('Too low. Guess again.')
            continue        
        else:
            print('YOU WIN!')  
            exit()
    print('Out of luck!')
    
Guess()
        