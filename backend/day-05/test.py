import random

print("Simple rock-paper-scissor Game")
objList = ['rock', 'paper', 'scissor']

playerOne = random.choice(objList)# input("Player 1: ").lower()
compChoice = random.choice(objList)
print(f'Player 1: {playerOne}')
print(f'Computer: {compChoice}')

if playerOne == compChoice:
    print("It's a tie!")
elif playerOne == 'paper' and compChoice == 'rock':
    print("Player 1 Wins!")
elif playerOne == 'rock' and compChoice == 'paper':
    print("Computer Wins!")
elif playerOne == 'rock' and compChoice == 'scissor':
    print("Player 1 Wins!")
elif playerOne == 'scissor' and compChoice == 'rock':
    print("Computer Wins!")
elif playerOne == 'scissor' and compChoice == 'paper':
    print("Player 1 Wins!")
elif playerOne == 'paper' and compChoice == 'scissor':
    print("Computer Wins!")
else:
    print("Wrong Input, Try Again!")