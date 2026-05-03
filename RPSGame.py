player1 = input("Player 1, enter Rock, Paper, or Scissors: ")
player2 = input("Player 2, enter Rock, Paper, or Scissors: ")

if player1 == player2:
    print("Draw")

elif player1 == "Rock" and player2 == "Scissors":
    print("Player 1 wins")

elif player1 == "Paper" and player2 == "Rock":
    print("Player 1 wins")

elif player1 == "Scissors" and player2 == "Paper":
    print("Player 1 wins")

elif player1 == "Rock" and player2 == "Paper":
    print("Player 2 wins")

elif player1 == "Paper" and player2 == "Scissors":
    print("Player 2 wins")

elif player1 == "Scissors" and player2 == "Rock":
    print("Player 2 wins")

else:
    print("Invalid input. Please enter Rock, Paper, or Scissors.")