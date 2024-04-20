# Develop a rock paper scissors game
import random
import sys

class Game:
    def __init__(self):
        self.computer_points = 0
        self.player_points = 0
        self.choices = ["r", "p", "s"]
    def intro(self):
        accept = input("ROCK PAPER SCISSORS.\nYou always have three choices (r, p, s).\nChoose One!!\nYou can always press \"q\" to end the game.\nDo you want to continue? (\"y\" or \"n\"): ").lower()
        return accept
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def get_player_choice(self):
        player_choice = input("Rock Paper Scissors (r, p, s): ").lower()
        return player_choice
    
    def player_win(self, computer_choice, player_choice):
        print("You win!!")
        #print choices
        print(f"{player_choice} > {computer_choice}\n")
        self.player_points += 1

    def computer_win(self, computer_choice, player_choice):
        print("The computer wins!!")
        #print choices
        print(f"{computer_choice} > {player_choice}\n")
        self.computer_points += 1
        
    def draw(self, computer_choice, player_choice):
        print("Draw!!")
        #print choices
        print(f"{computer_choice} == {player_choice}\n")
    
    def check_winner(self, player_choice, computer_choice):
        # Player wins
        if (player_choice == "r" and computer_choice == "s") or (player_choice == "p" and computer_choice == "r") or (player_choice == "s" and computer_choice == "p"):
            self.player_win(player_choice, computer_choice)

        # Computer wins
        elif (computer_choice == "r" and player_choice == "s") or (computer_choice == "p" and player_choice == "r") or (computer_choice == "s" and player_choice == "p"):
            self.computer_win(computer_choice, player_choice)
            
        # Draw
        elif computer_choice == player_choice:
            self.draw(computer_choice, player_choice)
            
        # Quit game
        elif player_choice == "q":
            self.quit_game()
            
        # Invalid response
        else:
            print("Invalid Response!!\n")
    
    def quit_game(self):
        print("=" * 20)
        print("Game Over!!")
        # Computer won
        if self.computer_points > self.player_points:
            print("Overall the Computer won!")
        # Player won
        elif self.player_points > self.computer_points:
            print("Overall you won!")
        # Draw
        else:
            print("Overall it was a draw!!")
        
        # Print results
        print(f"RESULTS: \nComputer Points: {self.computer_points}\nYour Points: {self.player_points}")
        print("=" * 20)
        sys.exit()
        
    #initialise the game
    def start_game(self):
        accept = self.intro()
        while accept not in ["y", "n", "q"]:
            print("**" * 20)
            print("Invalid input")
            print("**" * 20)
            accept = self.intro()

        if accept == "y":
            while True:
                computer_choice = self.get_computer_choice()
                player_choice = self.get_player_choice()
                self.check_winner(player_choice, computer_choice)
        elif accept == "n" or "q":
            self.quit_game()

game = Game()
game.start_game()
