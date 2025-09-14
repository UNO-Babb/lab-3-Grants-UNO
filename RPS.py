#RPS.py
#Name: Grant Schaeffer
#Date: 9/14/25
#Assignment: RPS
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.

  playAgain = "Y"
  while playAgain == "Y":
    #User can play as many games as they wish.
    computer = random.choice([ "R", "P", "S"])
    player = input("Make your play (R,P,S): ")
    #Randomly choose the computer between 'R', 'P', or 'S'
    if computer == "R":
      print("The computer plays rock")
    elif computer == "P":
      print("The computer plays paper")
    else:
      print("The computer plays scissors")

    
    #Prompt the user for their RPS selection
    #Determine winner and state what happened to the user

    if player == "R":
      print("You play rock")
    elif player == "P":
      print("You play paper")
    elif player == "S":
        print("You play scissors")
    else:
      print("What the heck. That was not an option.")

    if player == computer:
      print("Tie")
      ties = ties + 1
    if player == "R" and computer == "P":
      print("You lose!")
      losses = losses + 1
    if player == "P" and computer == "S":
      print("You lose!")
      losses = losses + 1
    if player == "S" and computer == "R":
      print("You lose!")
      losses = losses + 1
    if player == "R" and computer == "S":
      print("You win!")
      wins = wins + 1
    if player == "P" and computer == "R":
      print("You win!")
      wins = wins + 1
    if player == "S" and computer == "P":
      print("You win!")
      wins = wins + 1
  
  #Ask the user if they would like to play again.
    playAgain = input("Would you like to play again? (Y/N): ")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
