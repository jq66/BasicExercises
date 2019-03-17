game  = True

while game == True:
    player1 = input('Player 1! Rock/Paper/Scissors? ')
    player2 = input('Player 2! Rock/Paper/Scissors? ')
    if player1 == 'Rock':
        if player2 == 'Rock':
            print('It\'s a draw!')
        elif player2 == 'Paper':
            print('Player 2 won!')
        elif player2 == 'Scissors':
            print('Player 1 won!')
        else:
            print('Oops! Something went wrong!')
    elif player1 == 'Paper':
        if player2 == 'Paper':
            print('It\'s a draw!')
        elif player2 == 'Scissors':
            print('Player 2 won!')
        elif player2 == 'Rock':
            print('Player 1 won!')
        else:
            print('Oops! Something went wrong!')
    elif player1 == 'Scissors':
        if player2 == 'Scissors':
            print('It\'s a draw!')
        elif player2 == 'Rock':
            print('Player 2 won!')
        elif player2 == 'Paper':
            print('Player 1 won!')
        else:
            print('Oops! Something went wrong!')
    else:
        print('Oops! Something went wrong!')
    restart = input('Do you want to restart? (y/n): ')
    if restart == 'y':
        continue
    else:
        game = False
        print('Thank you for playing the game! Bye!')
