import random, time, sys 
 
print('''Quarts, Parchemnt, Shiers,
 - Quarts beats Shiers.
 - Parchment beats quarts.
 - Shiers beats parchment.
 ''')
 
 # These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0
 
while True:  # Main game loop.
     while True:  # Keep asking until player enters R, P, S, or Q.
         print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
         print('Enter your move: (R)Quarts (P)archement (S)hiers or (Q)uit')
         playerMove = input('> ').upper()
         if playerMove == 'Q':
             print('Thanks for playing!')
             sys.exit()
 
         if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
             break
         else:
             print('Type one of R, P, S, or Q.')
 
     # Display what the player chose:
     if playerMove == 'R':
         print('QUARTS versus...')
         playerMove = 'QUARTS'
     elif playerMove == 'P':
         print('PARCHEMNT versus...')
         playerMove = 'PARCHMENT'
     elif playerMove == 'S':
         print('SHIERS versus...')
         playerMove = 'SHIERS'
 
     # Count to three with dramatic pauses:
     time.sleep(0.5)
     print('1...')
     time.sleep(0.25)
     print('2...')
     time.sleep(0.25)
     print('3...')
     time.sleep(0.25)
 
     # Display what the computer chose:
     randomNumber = random.randint(1, 3)
     if randomNumber == 1:
         computerMove = 'QUARTS'
     elif randomNumber == 2:
         computerMove = 'PARCHMENT'
     elif randomNumber == 3:
         computerMove = 'SHIERS'
     print(computerMove)
     time.sleep(0.5)
 
     # Display and record the win/loss/tie:
     if playerMove == computerMove:
         print('It\'s a tie!')
         ties = ties + 1
     elif playerMove == 'QUARTS' and computerMove == 'SHIERS':
         print('You win!')
         wins = wins + 1
     elif playerMove == 'PARCHMENT' and computerMove == 'QUARTS':
         print('You win!')
         wins = wins + 1
     elif playerMove == 'SHIERS' and computerMove == 'PARCHMENT':
         print('You win!')
         wins = wins + 1
     elif playerMove == 'QUARTS' and computerMove == 'PARCHMENT':
         print('You lose!')
         losses = losses + 1
     elif playerMove == 'PARCHMENT' and computerMove == 'SHIERS':
         print('You lose!')
         losses = losses + 1
     elif playerMove == 'SHIERS' and computerMove == 'QUARTS':
         print('You lose!')
         losses = losses + 1