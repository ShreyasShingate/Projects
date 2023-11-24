#WordHub

from random import *

class WordHub:

    def __init__(self):
        self.word_list = None
        self.hint_list = None
        self.word_dict = None
        self.score = 0
        self.choosen_word = None
        self.choosen_word_letter_list = None
        self.index_list = None
        self.display_word = None
        self.random_index = None
        self.user_input = None
        self.lives = 5
        self.hint = 2

    def get_words_and_hints(self):
        with open(r"Word.txt","r") as file:
            self.word_list = file.read().split("\n")

        with open(r"Meaning.txt","r") as file:
            self.hint_list = file.read().split("\n")

        self.word_dict = dict(zip(self.word_list,self.hint_list))

    def get_choosen_word(self):
        self.choosen_word = choice(list(self.word_dict.keys()))

    def get_display_word(self):      
        self.choseen_word_letter_list = list(self.choosen_word)
        self.index_list = []
        self.display_word = ""

        for index in range(len(self.choosen_word)//2):
            self.random_index = choice([index for index in range(len(self.choosen_word)) if index not in self.index_list])
            self.choseen_word_letter_list[self.random_index] = "_"
            self.index_list.append(self.random_index)

        for ele in self.choseen_word_letter_list :
            self.display_word+=ele

    def checkwin_and_scorecard(self):
        if self.choosen_word == self.user_input:
            print("\nYou are correct..!\n")
            self.score+=1
        else:
            self.lives-=1
            print("\nSorry, it's incorrect\n")
            print("Correct word is {}\n".format(self.choosen_word))

        print("Score : {} ".format(self.score))
        
    def game_play(self):
        while True:
            self.get_words_and_hints()
            self.get_choosen_word()
            self.get_display_word()

            print("\nLives available : {}".format(self.lives))
            print("Hints available : {}\n".format(self.hint))

            print("Guess the word : {} ".format(self.display_word))
            print("Type here to guess the word")
            print("Type 1 for hint")
            print("Type 2 to exit\n")
            print("User Input : ",end="")
            self.user_input = input()

            if self.user_input == "1":
                if self.hint == 0:
                    print("\nYou have already utilized your hints, no more hints available\n")
                else:
                    self.hint-=1
                    print("\nHint : {}\n".format(self.word_dict[self.choosen_word]))
                print("Guess the word : {} ".format(self.display_word))
                print("Type here to guess the word")
                print("User Input : ",end="")
                self.user_input = input()
            elif self.user_input == "2":
                print("\nYou have successfully exited")
                break;
            
            self.checkwin_and_scorecard()

            if self.lives>0:
                continue
            else:
                print("\nGame Over!, you don't have any lives left to contiune")
                break


if __name__ == "__main__":
    print("Welcome to WordHub\n")
    print("Unleash your linguistic prowess in WordHub, where each correctly guessed word unlocks a new level of vocabulary mastery!")
    WordHub().game_play()

