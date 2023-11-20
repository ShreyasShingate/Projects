#Tic Tac Toe

from time import sleep
from random import choice

class TicTacToe:
    
    def __init__(self):
        self.game_board = [" " for index in range(9)]
        self.player_name = ["",""]
        self.user_choice = 0
        self.first_choice_maker = ""
        self.second_choice_maker = ""
        self.system_choice = 0
        self.player_choice = 0
        self.scorecard = [0,0]

    def print_game_board(self):
        print("\n " + str(self.game_board[0]) + " | " + str(self.game_board[1]) + " | " + str(self.game_board[2]))
        print("---|---|---")
        print(" " + str(self.game_board[3]) + " | " + str(self.game_board[4]) + " | " + str(self.game_board[5]))
        print("---|---|---")
        print(" " + str(self.game_board[6]) + " | " + str(self.game_board[7]) + " | " + str(self.game_board[8]) + "\n")

    def get_player_name(self):
        if self.user_choice == 1 :
            self.player_name = ["System",input("\nEnter Your Name\n")]
        else :
            self.player_name = [input("\nEnter Player 1 Name\n"),input("\nEnter Player 2 Name\n")]

    def main_menu(self):
        print("\nType 1 for Single Player Mode")
        print("Type 2 for Multi-Player Mode")
        print("Type 3 to Exit\n")

        print("User Input : ",end="")

        self.user_choice = int(input())

        if self.user_choice == 1:
            print("\nYou entered in Single Player Mode")
            self.get_player_name()
            self.player_vs_system()
        elif self.user_choice == 2:
            print("\nYou entered in Multi-Player Mode")
            self.get_player_name()
            self.player_vs_player()
        elif self.user_choice == 3:
            print("\nYou have successfully exited")
            quit()
        else:
            print("\nUnexpected Input, Please enter the correct number")
            self.main_menu()

    def get_player_choice(self,mark):
        self.player_choice = int(input())
        if self.player_choice in [index for index in range(len(self.game_board)) if self.game_board[index]==" "]:
            self.game_board[self.player_choice] = mark
        elif self.player_choice in [index for index in range(len(self.game_board)) if self.game_board[index]!=" "]:
            print("\nSpace is already occupied, make a new choice : ",end="")
            self.get_player_choice(mark)
        else:
            print("\nIncorrect Input, make a new choice : ",end="")
            self.get_player_choice(mark)

    def get_system_choice(self,mark):
        self.system_choice = choice([index for index in range(len(self.game_board)) if self.game_board[index]==" "])
        print(self.system_choice)
        self.game_board[self.system_choice] = mark

    def choice_maker(self):
        self.first_choice_maker = choice(self.player_name)
        self.second_choice_maker = self.player_name[0] if self.player_name[0] != self.first_choice_maker else self.player_name[1]

    def validate_win_condintion(self,mark):
        return ((self.game_board[0] == mark and self.game_board[1] == mark and self.game_board[2] == mark) 
        or (self.game_board[3] == mark and self.game_board[4] == mark and self.game_board[5] == mark) 
        or (self.game_board[6] == mark and self.game_board[7] == mark and self.game_board[8] == mark)
        or (self.game_board[0] == mark and self.game_board[3] == mark and self.game_board[6] == mark)
        or (self.game_board[1] == mark and self.game_board[4] == mark and self.game_board[7] == mark)
        or (self.game_board[2] == mark and self.game_board[5] == mark and self.game_board[8] == mark)
        or (self.game_board[0] == mark and self.game_board[4] == mark and self.game_board[8] == mark)
        or (self.game_board[2] == mark and self.game_board[4] == mark and self.game_board[6] == mark))
    
    def get_scorecard(self,current_player,win):
        if current_player == self.player_name[0] and win == 1:
            self.scorecard[0]+=1
        elif current_player == self.player_name[1] and win == 1:
            self.scorecard[1]+=1
        print("\nScoreCard")
        print("{} : {}    {} : {}\n".format(self.player_name[0],self.scorecard[0],self.player_name[1],self.scorecard[1]))

    def menu(self,mode):
        print("\nType 1 to Continue")
        print("Type 2 to Return Main Menu")
        print("Type 3 to Exit\n")

        self.user_choice = int(input())

        if self.user_choice == 1:
            self.game_board = [" " for index in range(9)]
            print("\nContinuing.......\n")
            self.player_vs_player() if mode == "PlayerVsPlayer" else self.player_vs_system()
        elif self.user_choice == 2:
            self.__init__()
            print("\nYou have returned to Main Menu\n")
            self.main_menu()
        elif self.user_choice == 3:
            print("\nYou have successfully exited\n")
            quit()
        else:
            print("\nIncorrect Input, Please select correct option\n")
            self.menu(mode)

    def player_vs_system(self):
        self.choice_maker()
        print("\n{} will make first choice".format(self.first_choice_maker))
        print("{} will use 'X' and {} will use 'O' mark\n".format(self.first_choice_maker,self.second_choice_maker))
        win = 0
        for turn in range(9):
            current_player = self.first_choice_maker if turn%2 == 0 else self.second_choice_maker
            mark = "X" if turn%2 == 0 else "O"
            print("{} : ".format(current_player),end="")
            self.get_system_choice(mark) if (current_player) == "System" else self.get_player_choice(mark)
            self.print_game_board()
            if self.validate_win_condintion(mark): 
                win = 1            
                break  
        print("\nGame Ended!\nWinner : {}\n".format(current_player)) if win == 1 else print("\nGame Ended!\nIt's a Draw\n")
        self.get_scorecard(current_player,win)
        self.menu("PlayerVsSystem")
                
    def player_vs_player(self):
        self.choice_maker()
        print("\n{} will make first choice".format(self.first_choice_maker))
        print("{} will use 'X' and {} will use 'O' mark\n".format(self.first_choice_maker,self.second_choice_maker))
        win = 0
        for turn in range(9):
            current_player = self.first_choice_maker if turn%2 == 0 else self.second_choice_maker
            mark = "X" if turn%2 == 0 else "O"
            print("{} : ".format(self.first_choice_maker if turn%2 == 0 else self.second_choice_maker),end="")
            self.get_player_choice(mark)
            self.print_game_board()
            if self.validate_win_condintion(mark): 
                win = 1            
                break  
        print("\nGame Ended!\nWinner : {}\n".format(current_player)) if win == 1 else print("\nGame Ended!\nIt's a Draw\n")
        self.get_scorecard(current_player,win)
        self.menu("PlayerVsPlayer")

        
print("Welcome! to Tic Tac Toe Game")

print("\nInstructions\n")
print("* It is a battle between two player to complete a straight line")
print("* The one who completes first will be our winner")
print("* Choose a number between 0-8 to place your mark on GameBoard")
print("* Align your marks vertically,horizontally or diagonally to create a straight line")
print("* Refer below Gameboard to understand number and associated spot\n")

print(" 0 | 1 | 2 ")
print("---|---|---")
print(" 3 | 4 | 5 ")
print("---|---|---")
print(" 6 | 7 | 8 ")

print("\nContinuing to Main Menu")

TicTacToe().main_menu()
        