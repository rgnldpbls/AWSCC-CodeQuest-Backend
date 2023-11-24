print("Simple rock-paper-scissor Game")

playerOne = input("Player 1: ").lower()
playerTwo = input("Player 2: ").lower()

if playerOne == playerTwo:
    print("It's a tie!")
elif playerOne == 'paper' and playerTwo == 'rock':
    print("Player 1 Wins!")
elif playerOne == 'rock' and playerTwo == 'paper':
    print("Player 2 Wins!")
elif playerOne == 'rock' and playerTwo == 'scissor':
    print("Player 1 Wins!")
elif playerOne == 'scissor' and playerTwo == 'rock':
    print("Player 2 Wins!")
elif playerOne == 'scissor' and playerTwo == 'paper':
    print("Player 1 Wins!")
elif playerOne == 'paper' and playerTwo == 'scissor':
    print("Player 2 Wins!")
else:
    print("Wrong Input, Try Again!")