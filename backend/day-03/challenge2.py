print("Scenario: Man Asking for Shelter")
respOne = input("You will take him or not (Y/N): ")
if respOne == 'Y' or respOne == 'y':
    print("Police arrived & Asked whether thief is inside")
    respTwo = input("What will be your response?(Y/N): ")
    if respTwo == 'Y' or respTwo == 'y':
        print("You win!")
    elif respTwo == 'N' or respTwo  == 'n':
        print("Game Over! Try Again!")
    else:
        print("Invalid input, Try Again!")
elif respOne == 'N' or respOne == 'n':
    print("He attacked on you. Will you knock him down?")
    respTwo = input("Your response(Y/N): ")
    if respTwo == 'Y' or respTwo == 'y':
        print("You win!")
    elif respTwo == 'N' or respTwo == 'n':
        print("Game Over! Try Again!")
    else:
        print("Invalid input, Try Again!")
else:
    print("Invalid input, Try Again!")
