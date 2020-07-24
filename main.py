import random

moves = ['rock', 'paper', 'scissor']

computer_move = moves[random.randint(0,2)]
player_move = True

while(player_move == True):
    print("Enter your move: rock , paper or scissor?")
    move_played = input()
    if(move_played==computer_move):
        print("It's a tie")
    elif(move_played=='rock'):
        if(computer_move=='paper'):
            print("I won")
        elif(computer_move == 'scissor'):
            print("You won")
    elif(move_played == 'paper'):
        if(computer_move == 'rock'):
            print("I won")
        elif(computer_move == 'scissor'):
            print("I lost")
    elif(move_played == 'scissor'):
        if(computer_move == 'paper'):
            print('You won')
        elif(computer_move == 'rock'):
            print("I won")
    else:
        print("Enter correct option")
    player_move = True
    computer_move = moves[random.randint(0, 2)]

