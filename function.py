import os
import random
import getch


def lucky():
    day = int(input('Enter your day : '))
    month = int(input('Enter your month : '))
    year = int(input('Enter your years : '))
    luckys = day + (month*12) + (year*365)
    good_luck = luckys % 3

    if good_luck == 0:
        print("!!! Bad day !!!")
    elif good_luck == 1:
        print('****Today is lucky ****')
    else:
        print('### As well As lucky day ###')
# Your Python code here

    input("Press Enter to continue...")


def dice_game():

    player = random.randint(1, 6)
    computer = random.randint(1, 6)
    print('Turn Player')
    input("Press Enter to continue...")
    print(f'player: {player}')
    print('Turn Computer')
    input("Press Enter to continue...")
    print(f'compuer: {computer}')
    input("Press Enter to continue...")
    os.system('clear')
    if player > computer:
        print("Player Win !!!")
    elif player < computer:
        print("Computer Win !!!")
    elif player == computer:
        print("Value are the same trun again !!!!")
    else:
        print("!!!Enter only number !!!")


def advancture():
    x_min = 0
    x_max = 10
    y_min = 0
    y_max = 10
    player_x = 5
    player_y = 5

    while True:
        key = getch.getch()
        if key == 'a':
            player_x = player_x - 1
            if player_x < x_min:
                player_x = x_min

        if key == 'd':
            player_x = player_x + 1
            if player_x > x_max:
                player_x = x_max

        if key == 'w':
            player_y = player_y - 1
            if player_y < y_min:
                player_y = y_min

        if key == 's':
            player_y = player_y + 1
            if player_y > y_max:
                player_y = y_max

        if key == 'q':
            print('Exiting ....')
            play()

        print(f'player location is x = {player_x}, y = {player_y}')
        for i in range(0, player_y):
            print()
        avt = ''
        for i in range(0, player_x):
            avt = avt + '  '
        avt = avt + "*"
        print(avt)


def play():
    while True:
        print('0: *** exit ***')
        print('1: *** lucky game *** ')
        print('2: *** dice game ***')
        print('3: *** advancture ***')
        choice = int(input('Enter your choice :'))
        os.system("clear")

        if choice == 0:
            print('Exiting ......')
            exit()
        elif choice == 1:
            lucky()
        elif choice == 2:
            dice_game()
        elif choice == 3:
            advancture()

        else:
            print("Invalid choice. Please enter 1 or 2 or 3... ")


play()
