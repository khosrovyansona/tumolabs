import random

def dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum0 = dice1 + dice2
    return dice1, dice2, sum0

dice1, dice2, sum0 = dice()
print(f'The sum of dice is: {dice1} + {dice2} = {sum0}')


if sum0 in (7,11):
    print('You win!')
elif sum0 in (2,3,12):
    print('Casino wins!')
else:
    goal_number = sum0
    print(f'New goal number is {goal_number}')
    over = True
    while over == True:
        dice1, dice2, sum0 = dice()
        print(f'The sum of dice is: {dice1} + {dice2} = {sum0}')
        if sum0 == goal_number:
            print('You win!')
            over = False
        if sum0 == 7:
            print('You lose!')
            over = False
