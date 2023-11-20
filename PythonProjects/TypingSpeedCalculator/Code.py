#Typing Speed Calculator

from time import time,sleep
from random import choice
from getpass import getpass

class TypingSpeedCalculator:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.user_choice = 0
        self.user_rechoice = 0
        self.test_paragraph = ""
        self.file_content = ""
        self.user_text_input = ""
        self.overall_time = 0
        self.error = 0
        self.accuracy = 0
        self.speed_wpm = 0
        self.gross_wpm = 0

    
    def typing_test(self):

        while(1):

            print("\nChoose Difficulty Level\n")
            print("Type 1 for Easy")
            print("Type 2 for Medium")
            print("Type 3 for Hard")
            print("Type 4 for Expert")
            print("Type 5 to Exit\n")
            
            print("User Input : ",end="")
            self.user_choice = int(input())

            if(self.user_choice == 5):
                print("\nYou have successfully exited\n")
                break

            with open([r"Easy.txt",r"Medium.txt",r"Hard.txt",r"Hard.txt"][self.user_choice-1]) as file:
                self.file_content  = file.read() 

            while(1):

                self.test_paragraph = choice(self.file_content.split("\n")).strip()

                print("\nThe Text Paragraph will be on screen soon")
                print("Upon which the Timer will start, so start typing immediately\n")
                
                sleep(2)

                print("Paragraph : " + "\n" + self.test_paragraph + "\n")

                self.start_time = time()

                print("User Text Input : ")
                if self.user_choice == 4:
                    self.user_text_input = getpass("")
                else:          
                    self.user_text_input = input()
                    
                self.end_time = time()

                self.error = 0
                self.accurate_letter_count = 0

                for index in range(len(self.test_paragraph)):
                    try:
                        if(self.test_paragraph[index] != self.user_text_input[index]):
                            self.error+=1
                        else:
                            self.accurate_letter_count+=1
                    except:
                        self.error+=1

                self.overall_time = round(self.end_time-self.start_time,2)
                self.gross_wpm = round((len(self.user_text_input)*60)/(5*self.overall_time),2)
                self.speed_wpm = round((self.accurate_letter_count*60)/(5*self.overall_time),2)
                self.accuracy = round((self.speed_wpm * 100)/ self.gross_wpm,2)

                print("\nTyping Score")
                print("----------------------")
                print("Total Time(s)".ljust(15) + ": " + str(self.overall_time))
                print("Accuracy".ljust(15) + ": " + str(self.accuracy))
                print("Errors".ljust(15) + ": " + str(self.error))
                print("Gross WPM".ljust(15) + ": " + str(self.gross_wpm))
                print("Net WPM".ljust(15) + ": " + str(self.speed_wpm))
                print("----------------------")
            
                print("\nType 1 to Continue")
                print("Type 2 to Return Main Menu")
                print("Type 3 to Exit\n")

                print("User Input : ",end="")
                self.user_rechoice  = int(input())

                if self.user_rechoice == 1 :
                    print("\nYou are continuing in the same difficulty level")
                    continue
                elif self.user_rechoice == 2 :
                    print("\nYou have returned to Main Menu")
                    break
                else:
                    print("\nYou have successfully exited")
                    quit()


print("Welcome to Typing Speed Calculator")
TypingSpeedCalculator().typing_test()







    
