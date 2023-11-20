#Rock Paper Scissor

from random import choice
from getpass import getpass

class RockPaperScissor:

    def __init__(self):
        self.player_1_choice = ""
        self.player_2_choice = ""
        self.player_1_score = 0
        self.player_2_score = 0
        self.choice = 0
        self.game_over = 0
        self.player_name = ["",""]

    def main_menu(self):
        print("Type 1 for Single Player Mode")
        print("Type 2 for Multi-Player Mode\n")

        print("User Input : ",end="")
        self.choice = int(input())

        if self.choice == 1:
            self.player_name = ["System",input("\nEnter Your Name : ")]
            self.player_vs_system()
        elif self.choice == 2:
            self.player_name = [input("\nEnter Player 1 Name : "),input("Enter Player 2 Name : ")]
            self.player_vs_player()
        else:
            print("\nIncorrect Input, Please Select Correct Option\n")
            self.main_menu()

    def menu(self):
        print("Type 1 to Continue")
        print("Type 2 to Return Main Menu")
        print("Type 3 to Exit\n")

        print("User Input : ",end="")
        self.choice = int(input())

        if self.choice == 1:
            print("\nYou are continuing with same Mode\n")
            self.game_over = 0
        elif self.choice == 2:
            print("\nYou have returned to Main Menu\n")
            self.__init__()
            self.main_menu()
        elif self.choice == 3:
            print("\nYou have successfully exited\n")
            self.game_over = 1

    def game_actions(self):                   
        self.validate_winner()
        self.print_choices()
        self.print_score()
        self.menu()

    def player_vs_system(self):
        while(self.game_over == 0):
            self.player_1_choice = choice(["Rock","Paper","Scissor"])
            self.player_2_choice = input("\nRock Paper Scissor, Player2 Make Your Choice : ")
            self.game_actions()

    def player_vs_player(self):
        while(self.game_over==0):
            self.player_1_choice = getpass("\nRock Paper Scissor, Player1 Make Your Choice : ")
            self.player_2_choice = getpass("Rock Paper Scissor, Player2 Make Your Choice : ")
            self.game_actions()
    
    def print_choices(self):
        print("Choices\n{} : {}    {} : {}\n".format(self.player_name[0],self.player_1_choice,self.player_name[1],self.player_2_choice))
 
    def print_score(self):
        print("Scorecard\n{} : {}    {} : {}\n".format(self.player_name[0],self.player_1_score,self.player_name[1],self.player_2_score))

    def validate_winner(self):
        if self.player_1_choice == "Rock":
            if self.player_2_choice == "Rock":
                print("\nIt's a Draw\n")
            elif self.player_2_choice == "Paper":
                print("\n{} Won\n".format(self.player_name[1]))
                self.player_2_score+=1
            elif self.player_2_choice == "Scissor":
                print("\n{} Won\n".format(self.player_name[0]))
                self.player_1_score+=1

        if self.player_1_choice == "Paper":
            if self.player_2_choice == "Rock":
                print("\n{} Won\n".format(self.player_name[0]))
                self.player_1_score+=1
            elif self.player_2_choice == "Paper":
                print("\nIt's a Draw\n")
            elif self.player_2_choice == "Scissor":
                print("\n{} Won\n".format(self.player_name[1]))
                self.player_2_score+=1

        if self.player_1_choice == "Scissor":
            if self.player_2_choice == "Rock":
                print("\n{} Won\n".format(self.player_name[1]))
                self.player_2_score+=1
            elif self.player_2_choice == "Paper":
                print("\n{} Won\n".format(self.player_name[0]))
                self.player_1_score+=1
            elif self.player_2_choice == "Scissor":
                print("\nIt's a Draw\n")


print("Welcome..! to Rock Paper and Scissor Game\n")
RockPaperScissor().main_menu()



