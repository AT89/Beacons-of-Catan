import random
import time
import subprocess

min = 1
max = 6

roll_again = 'yes'

while roll_again == 'yes' or roll_again =='y' or roll_again =='Y':
    print 'Shaking'
    time.sleep(1)
    print 'Shaking'
    time.sleep(1)
    print 'Shaking'
    time.sleep(1)
    print 'Rolling the dice...'
    time.sleep(1)
    value_dice1 = random.randint(min, max)
    value_dice2 = random.randint(min, max)
    value_dices = value_dice1+value_dice2
##    value_dices = 7
    print 'you rolled a ',value_dice1,' and ',value_dice2, '' 
    print 'total value is ',value_dices,''
    
    if value_dices == 6:
        subprocess.call('python R-LED.py', shell=True)
    if value_dices == 8:
        subprocess.call('python B-LED.py', shell=True)
    if value_dices == 7:
        subprocess.call('python ALL-LED.py', shell=True)

    roll_again = raw_input('Roll again? ')