#!/usr/bin/env python
import os
import sys
import random
import time

# import os for clearing screen, sys- to exit execution
#random - to shuffle answers, timeit

'''new_python.py: Coded in python 3.5.2 version,is project submittion
for Udacity Fill in the blanks project (Stage 2 IPND). '''

__author__ = "Srilakshmi"

# NoviceLevel list has collection of 4 levels question tuple's within.
NoviceLevel = [
                    (
                            "\n A programming language is a formal _ _ _1_ _ _ "
                            "language designed to communicate _ _ _2_ _ _ to a"
                            " _ _ _3_ _ _, particularly a computer. Python is a"
                            " widely used _ _ _4_ _ _-level programming"
                            "language for _ _ _5_ _ _ programming, created by "
                            "Guido van Rossum. \n"
                            ),
                    (
                            "\n Computer Terminology: \n"
                            "\n A) _ _ _1_ _ _ is the physical aspect of the "
                            "computer that can be seen.\n"
                            "\n B) _ _ _2_ _ _ is the brain of a computer.\n"
                            "\n C) The speed of the CPU may be measured in "
                            "_ _ _3_ _ _.\n"
                            "\n D) _ _ _4_ _ _ is a lexical structure of source"
                            "code which is grouped together.\n"
                            "\n E) A _ _ _5_ _ _ is a collection of"
                            "instructions that performs"
                            "a specific task when executed by a computer.\n"
                            ),
                    (
                            "\n Computer Pioneers: \n"
                            "\n A) _ _ _1_ _ _ was the first to recognise that "
                            "the machine had applications beyond pure "
                            "calculation, and created the first algorithm "
                            "intended to be carried out by such a machine. And, "
                            "is often regarded as the first to recognise the "
                            "full potential of a computing machine and"
                            "the first computer programmer.\n"

                            "\n B) _ _ _2_ _ _ is a Dutch programmer who is best "
                            "known as the author of the Python Programing "
                            "language. \n"

                            "\n C) _ _ _3_ _ _ was one of the first programmers "
                            "of the Harvard Mark I computer and invented the "
                            "first compiler for a computer programming "
                            "language.\n"

                            "\n D) Who is known as the father of theoretical "
                            "computer science? _ _ _4_ _ _.\n"

                            "\n E) Father of C programming language? "
                            "_ _ _5_ _ _.\n"
                            ),
                    (
                            "\n ""Programming Errors:"" \n"
                            "\n _ _ _1_ _ _'S \t : These types of errors are "
                            "usually typing mistakes, but more generally it "
                            "means that there is some problem with the structure "
                            "of your program.\n"
                            "Output: _ _ _1_ _ _ There was an error in your "
                            "program: "
                            "EOL while scanning single-quoted string.\n"

                            "\n_ _ _2_ _ _'S \t : This error usually means that "
                            "there was an open parenthesis somewhere on a line, "
                            "but not a matching closing parenthesis. "
                            "Python reached the end of the file while looking for "
                            "the closing parenthesis.\n Output: _ _ _2_ _ _, "
                            "EOF in multi-line statement\n"

                            "\n_ _ _3_ _ _'S \t : These error occur as your program "
                            "executes. Since Python is an interpreted language,"
                            " these errors will not occur until the flow of control "
                            "in your program reaches the line with the problem."
                            "Looping and arithmetic errors falls under this category."
                            "\n"
                            "This will be a common error you encounter. It will give "
                            "you a Traceback message.\n"

                            "\n_ _ _4_ _ _'S \t : These are problems with the design "
                            "of your program. These usually do not produce "
                            "any error message, but instead cause your program to "
                            "behave incorrectly."
                            " These types of errors can be tricky to track down.\n"
                            "\n Often, these errors are often caused by accidentally "
                            "using one variable in a place where a different"
                            " variable is intended.\n"

                            "\n _ _ _5_ _ _'S \t : Is an error that happens during "
                            "execution of a program. When occured"
                            " Python generate an _ _ _5_ _ _ that can be handled, "
                            "which avoids your program to crash.\n"
                            )
                    ]

# SkilledLevel list has collection of 4 levels question tuple's within.
SkilledLevel = [
                    (
                            " \n _ _ _1_ _ _ -\t Adds a single element to the end of "
                            "the list.\n"
                            " Common error: does not return the new list, just "
                            "modifies the original."
                            " \n _ _ _2_ _ _ -\t Inserts the element at the given "
                            "index, shifting elements to the right.\n"
                            " \n _ _ _3_ _ _ -\t Adds the elements in list2 to the "
                            "end of the list. \n"
                            " Using + or += on a list is similar to using extend().\n"
                            " \n _ _ _4_ _ _ -\t Searches for the given element from "
                            "the start of the list and returns its index. \n"
                            " Throws a ValueError if the element does not appear "
                            "(use \"in\" to check without a ValueError).\n"
                            " \n _ _ _5_ _ _  -\t Searches for the first instance of "
                            "the given element and removes it"
                            "(throws ValueError if not present)"
                            ),
                    (
                            " \n _ _ _1_ _ _ \t \t -\t Sorts the list in place "
                            "(does not return it). \n"
                            "(The sorted() function shown below is preferred.)\n"
                            " \n _ _ _2_ _ _ \t \t -\t Reverses the list in place "
                            "(does not return it)\n"
                            "\n _ _ _3_ _ _ \t \t -\t Removes and returns the element "
                            "at the given index. "
                            "Returns the rightmost element if index is omitted "
                            "(roughly the opposite of append()).\n"
                            " \n _ _ _4_ _ _ -\t Returns the lowercase or uppercase "
                            "version of the string s \n"
                            " \n _ _ _5_ _ _ \t \t -\t Returns a string with whitespace "
                            "removed from the start and end\n"
                            ),
                    (
                            " \n _ _ _1_ _ _ \t Tests if all the string chars are in the "
                            "various character classes\n"
                            " \n _ _ _2_ _ _ \t Tests if the string starts or ends with "
                            "the given other string\n"
                            " \n _ _ _3_ _ _ \t Searches for the given other string "
                            "(not a regular expression) within s,"
                            " and returns the first index where it begins or -1 if not "
                            "found"
                            " \n _ _ _4_ _ _ \t Returns a string where all occurrences "
                            "of 'old' have been replaced by 'new'\n"
                            " \n_ _ _5_ _ _ \t Returns a list of substrings separated by "
                            "the given delimiter. "
                            "The delimiter is not a regular expression, it's just text. "
                            "'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. "
                            "As a convenient special case s.split() (with no arguments) "
                            "splits on all whitespace chars.\n"
                            "\n s.join(list) \t opposite of split(), joins the elements "
                            "in the given list together using the string as the "
                            "delimiter.\n"
                            "e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc \n"
                            ),
                    (
                            "\n STRINGS: \n"
                            "letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] \n"
                            "print letters[2:5] \t \t Output: _ _ _1_ _ _\n"

                            "\n S= '<any given string' \n"
                            " Which of these pairs are two things with the exact same "
                            "value? \n"
                            "\n 1) S[3],S[1+1+1]"
                            "\n 2) S[0],(S+S)[0]"
                            "\n 3) S[0]+S[1],S[0+1]"
                            "\n 4) S[1],(S+'ity')[1]"
                            "\n 5) S[-1],(S+S)[-1]"
                            "\t \t Output: _ _ _2_ _ _\n"

                            "\n For any string,\n"
                            "\n K = '<any given string>'"
                            "\n Which of the following always has the value 0?"
                            "\n 1) K.find(K)"
                            "\n 2) K.find('K')"
                            "\n 3) 'K'.find('K')"
                            "\n 4) K.find('')"
                            "\n 5) K.find(K+!!!)+"
                            "\t \t Output: _ _ _3_ _ _\n"

                            "\n Which of the followig evaluates to -1"
                            "\n 1) 'test'.find('t')"
                            "\n 2) \"test\".find('st')"
                            "\n 3) \"Test\".find('te')"
                            "\n 4) 'west'.find('test')"
                            "\t \t Output: _ _ _4_ _ _\n"

                            "\n sentence = 'A NOUN went on a walk.'"
                            "\n substring = sentence[6:]"
                            "\n print substring"
                            "\t \t Output: _ _ _5_ _ _\n"
                            )
                    ]

# ExpertLevel list has collection of 4 levels question tuple's within.
ExpertLevel = [
                    (
                            "\n A) print type(1/2) \t \t OUTPUT TYPE: _ _ _1_ _ _\n"
                            "\n B) print type([1,2]) \t \t OUTPUT TYPE: _ _ _2_ _ _\n"
                            "\n C) def f(): pass \n print type(f()) \t\t "
                            "OUTPUT TYPE: _ _ _3_ _ _\n"
                            "\n D) print type(1J) \t \t OUTPUT TYPE: _ _ _4_ _ _\n"
                            "\n E) print type(lambda:None) \t OUTPUT TYPE: "
                            "_ _ _5_ _ _\n"
                            ),
                    (
                            "\n print r\\nwoow \t \t Output: _ _ _1_ _ _\n \n"
                            "\n name = 'snow storm' \n name[5] = 'X' \n print name "
                            "\t \t Output: _ _ _2_ _ _\n"
                            "\n Print statement to print all the names in the below "
                            "list on a seperate line is? \n"
                            "names = ['Twitter', 'Microsoft', 'Google', 'Apple',"
                            "'Tesla'] \n"
                            "\t \t Output: _ _ _3_ _ _\n \n"
                            "\n kvps  = {""user"",""microphone"", ""password"","
                            " ""camera""} \n print kvps['password'] \n"
                            "\t \t Output: _ _ _4_ _ _ \n \n"
                            "class Account: \n \t"
                            "def __init__(self, id): \n \t \t"
                            "self.id = id \n \t \t id = 666 \n"
                            "acc = Account(123) \n"
                            "print acc.id \n"
                            "\t \t Output: _ _ _5_ _ _\n"
                            ),
                    (
                            "\n x = True \n y = False \n z = False \n"
                            " if not x or y:\n \t print 1\n"
                            " elif not x or not y and z: \n \t"
                            " print 2 \n elif not x or y or not y and x: \n\t"
                            " print 3 \n else: \n \t print 4 \t"
                            "\t Output: _ _ _1_ _ _\n"

                            "\n nums = set([1,1,2,3,3,3,4])\n print len(nums) "
                            "\t \t Output: _ _ _2_ _ _\n"

                            "\n a = [1,2,3,None,(),[],] \n print len(a)\t \t "
                            "Output: _ _ _3_ _ _\n"

                            "\n counter = 1 \n def doLotsOfStuff(): \n \t global "
                            "counter \n \t for i in (1, 2, 3): \n \t \t "
                            "counter += 1 \n"
                            "doLotsOfStuff() \n print counter \t \t "
                            "Output: _ _ _4_ _ _\n"

                            "\n x = 4.5 \n y = 2 \n print x//y \t \t "
                            "Output: _ _ _5_ _ _\n"
                            ),
                    (
                            "\n Given any string P, which of the following always "
                            "have the same value as P"
                            "(P can be an empty string ' ' )"
                            "\n 1) ('a' + P)[1:]"
                            "\n 2) P + '')"
                            "\n 3) P[0] + P[1:]"
                            "\n 4) P[0:]"
                            "\t \t Output: _ _ _1_ _ _\n"

                            "\n Show the output of the following code: \n"
                            "def f2(n, result): \n \t"
                            "if n == 0: \n \t "
                            "return 0 \n"
                            "else: \n \t"
                            "return f2(n - 1, n + result) \n"
                            "print(f2(2, 0))"
                            "\t \t Output: _ _ _2_ _ _\n"

                            "\n For any string, T = '<any sentence>'\n"
                            "Which of the these is always equivalent to T: \n"
                            "\n 1) T[:]"
                            "\n 2) T+T[0:-1+1]"
                            "\n 3) T[0:]"
                            "\n 4) T[:-1]"
                            "\n 5) T[:3] + T[3:]"
                            "\t \t Output: _ _ _3_ _ _\n"

                            "\n def bigger(a,b): \n \t"
                            "if(a>b):\n \t \t"
                            "return a \n \t"
                            "else: \n \t \t"
                            "return b"
                            "print bigger(2345,1245)"
                            "\t \t Output: _ _ _4_ _ _\n"

                            "\n What does this program do?"
                            "\n i=0"
                            "\n while i != 10:"
                            "\n \t i=i+1"
                            "\n \t print i"
                            "\n 1) Run Forever"
                            "\n 2) print numbers from 1 to 9"
                            "\n 3) print numbers from 0 to 9"
                            "\n 4) print numbers from 1 to 10"
                            "\n 5) Produce an error"
                            "\t \t Output: _ _ _5_ _ _\n"
                            )
                    ]

# NoviceLevelAnswers list has collection of 4 levels answer tuple's within.
#First 5 are answers.
NoviceLevelAnswers =    [
                                ('COMPUTER','INSTRUCTIONS','MACHINE','HIGH',
                                 'GENERAL-PURPOSE'),
                                ('HARDWARE','CPU','HERTZ','CODE BLOCK',
                                 'COMPUTER PROGRAM'),
                                ('ADA LOVELACE','GUIDO VAN ROSSUM',
                                 'GRACE HOPPER','ALAN TURING','DENNIS RITCHIE'),
                                ('SYNTAX ERROR','TOKEN ERROR','RUNTIME ERROR',
                                 'LOGIC ERROR','EXCEPTION','INDENTATION ERROR',
                                 'RUNNER ERROR','STANDARD ERROR')
                        ]
# SkilledLevelAnswers list has collection of 4 levels answer tuple's within.
SkilledLevelAnswers =   [
                                ('LIST.APPEND(ELEM)', 'LIST.INSERT(INDEX, ELEM)',
                                 'LIST.EXTEND(LIST2)','LIST.INDEX(ELEM)',
                                 'LIST.REMOVE(ELEM)'),
                                ('LIST.SORT()','LIST.REVERSE()',
                                 'LIST.POP(INDEX)','S.LOWER(), S.UPPER()',
                                 'S.STRIP()','S.JOIN(LIST)'),
                                ('S.ISALPHA()/S.ISDIGIT()/S.ISSPACE()',
                                 "S.STARTSWITH('OTHER')","S.ENDSWITH('OTHER')",
                                 "S.REPLACE('OLD','NEW')","S.SPLIT('DELIM')"),
                                ("['C', 'D', 'E']",'125','1345','34','WENT ON A WALK','123',
                                 '12','14','23','345','245','1234','2345',
                                 '1245',"['D', 'E\']")
                        ]
# ExpertLevelAnswers list has collection of 4 levels answer tuple's within.
ExpertLevelAnswers =    [
                                ('FLOAT','LIST','NONETYPE','COMPLEX','NONETYPE',
                                 'INT','TUPLE','FUNCTION','STR','TYPE','UNICODE'),
                                ('\\NWOOW','ERROR, THIS CODE WILL NOT RUN',
                                 'PRINT \\N.JOIN(NAMES)',
                                 'NOTHING. PYTHON SYNTAX ERROR',
                                 "123","SNOWXSTORM",
                                 'PRINT NAMES.JOIN(""%SR\\N"", NAMES)','666',
                                 'PRINT NAMES.JOIN("R\\N")','CAMERA',
                                 'PASSWORD'),
                                ('3','4','7','4','2.0','9.0','1','2','2','3','5',
                                 '6','9','ERROR'),
                                ('124','3','1235','2345','4','234','134','1245',
                                 '134','1','2','5')
                        ]

# Novice level game
# This function allow user to select how many wrong answers can be answered and
# Takes help of "EachLevelGame" function to play and iterate every level question.
def NoviceGame():
        # AllowedRange is list of lives for each level in this game
        AllowedRange = [1,2,3,4,5,6,7]
        # Initiating lives to 0
        AllowedLives = 0
        # While loop checks if the user input is in correct range of
        #lives for the game
        # (can be replaced with built-in function "range")
        while AllowedLives not in AllowedRange:
                AllowedLives = int(input("Choose number of lives for each"\
                                         "level (choose a number less than 7): "))
                '''Enter values between 1-7 inclusively'''
        # While loop from 0 iterates every level and calls the function
        #"EachLevelGame" to play every level to user
        Levelindex = 0
        while Levelindex < len(NoviceLevel):
                print (
                        "\n" + "Level " + str(Levelindex + 1)  + "\n"
                        "----------------------------------------------"
                        "------------------\n"
                        )
                # As the answers choices are tuple, we convert it to list
                RandomAnswer = list(NoviceLevelAnswers[Levelindex])
                # Presenting Shuffled answer choices to user
                random.shuffle(RandomAnswer)
                EachLevelGame(NoviceLevel[Levelindex],
                              NoviceLevelAnswers[Levelindex], RandomAnswer,
                              AllowedLives)
                Levelindex += 1

# Skilled level game
# This function has entire code for skilled game and takes help of
# "EachLevelGame" function to play and iterate every level question
def SkilledGame():
        # AllowedRange is list of lives for each level in this game
        AllowedRange = [1,2,3,4,5]
        # Initiating lives to 0
        AllowedLives = 0
        # While loop checks if the user input is within correct range of lives
        while AllowedLives not in AllowedRange:
                AllowedLives = int(input("Choose number of lives "
                                         "for each level (choose a number less "
                                         "than 5): "))
        # While loop from 0 iterates every level and calls the function
        #"EachLevelGame" to play every level to user
        Levelindex = 0
        while Levelindex < len(SkilledLevel):
                print (
                        "\n" + "Level " + str(Levelindex + 1)  + "\n"
                        "---------------------------------------------"
                        "-------------------\n"
                        )
                # As the answers choices are tuple, we convert it to list
                RandomAnswer = list(SkilledLevelAnswers[Levelindex])
                # Presenting Shuffled answer choices to user
                random.shuffle(RandomAnswer)
                EachLevelGame(SkilledLevel[Levelindex],
                              SkilledLevelAnswers[Levelindex],
                              RandomAnswer, AllowedLives)
                Levelindex += 1

# Expert level game function
# This function has entire code for skilled game and takes help of
# "EachLevelGame" function to play and iterate every level question
def ExpertGame():
        print ("Only 3 lives in this Game!")
        # Initiating to default 3 lives
        AllowedLives = 3
        Levelindex = 0
        # While loop from 0 iterates every level and calls the function
        #"EachLevelGame" to play every level to user
        while Levelindex < len(ExpertLevel):
                print (
                        "\n" + "Level " + str(Levelindex + 1)  + "\n"
                        "---------------------------------------------"
                        "-------------------\n"
                        )
                # As the answers choices are tuple, we convert it to list
                RandomAnswer = list(ExpertLevelAnswers[Levelindex])
                # Presenting Shuffled answer choices to user
                random.shuffle(RandomAnswer)
                EachLevelGame(ExpertLevel[Levelindex],
                              ExpertLevelAnswers[Levelindex],
                              RandomAnswer, AllowedLives)
                Levelindex += 1


# This function helps to iterate through each level of the game,
#dynamically for every stage
# Also determines the time taken by user to fill in the blanks
def EachLevelGame(EachLevel, Answerkey, DisplayAnswerKey, Num_lives):
        # Time count begins here
        timerstart = time.time()
        print ("Question: " + EachLevel + "\n \n")
        # Iterating every level 5 times as every level has 5 blanks precisely,
        # prints every question, random answers and prompts to fill in the blank
        EachLevelindex = 0
        TotalBlanks = 5
        while EachLevelindex < TotalBlanks:
                print ("Possible answers:")
                print ("\t" + "\t".join(DisplayAnswerKey))
                UserInput = input("\n \n What term should be filled "
                                  "in the blank: "
                                  + "_ _ _" + str(EachLevelindex + 1) +
                                  "_ _ _" + "?\n \t")
                # Checks user input, if true game cont. or else 1 live is lost
                if UserInput.upper() == Answerkey[EachLevelindex]:
                        EachLevel = EachLevel.replace("_ _ _" +
                                                      str(EachLevelindex + 1) +
                                                      "_ _ _",
                                                      Answerkey[EachLevelindex])
                        EachLevelindex += 1
                        print
                        print ("\t" + "Correctly answered!!: \n" + EachLevel)
                else:
                        Num_lives -= 1
                        print ("\n" + "Incorrect Answer! "
                               "Number of guesses remaining: " + str(Num_lives))
                        endLife = 0
                        if Num_lives == endLife:
                                print ("\n" + "Sorry, try again next time!!")
                                time.sleep(2)
                                sys.exit()
        # End of time
        timerend = time.time()
        print ("\t \t \n Good Job! Level Completed! \n")
        time.sleep(2)
        print ("\t \t Time took to complete Level (in secs):" +
               str(round(timerend - timerstart)))

# This funcion helps to restart or quit
def replay(val):
        if val == "Y":
                # clears screen and restarts the game by calling
                # the main game function
                os.system('cls')
                return MainGame()
        elif val == "N":
                time.sleep(10)
                return sys.exit()

# Main function for this project. This is executed first.
def MainGame():
        # GameDifficulty is the list of possible games can be played
        # by the user
        GameDifficulty = ["NOVICE", "N", "SKILLED", "S", "EXPERT", "E",
                          "QUIT", "Q"]
        # Initializing the game difficulty as a string
        difficulty = ""
        # printing out the initial titles for the game
        print ("\n \t \t --------------------------------------"
               "\n \t \t --- Welcome to Madlibs Python Quiz ---"
               "\n \t \t --------------------------------------\n\n"

               "\t Choose Game to play:\n"
               "\t--------------------------------- \n"
               "\t * Novice\n"
               "\t * Skilled\n"
               "\t * Expert\n"
               "\t * Quit\n"
               "\n **Input are not case-sensitive: shortcut keyboard keys"
               "(n, s, e, or q)**\n "
               )
        # Checking if the user has selected given games, if not take input
        # till the user enters correct answer choice
        while difficulty not in GameDifficulty:
                difficulty = input(" Choose Game [Novice|N || Skilled|S || Expert|E || Quit |Q]: ")
                DifficultyChoice = difficulty.upper()
                # Checks input "DifficultyChoice" and calls functions
                # accordingly once funtion is executed prompts user to replay
                if (DifficultyChoice == "NOVICE" or DifficultyChoice == "N"):
                        NoviceGame()
                        print ("\t \t \t -------------------------\n"+
                               "\t \t \t -NOVICE GAME COMPLETED-\n"+
                               "\t \t \t -------------------------\n")
                        ReplayGame = input("Do you want to play again? Y or N:")
                        replay(ReplayGame.upper())
                elif (DifficultyChoice == "SKILLED" or DifficultyChoice == "S"):
                        SkilledGame()
                        print ("\t \t \t-------------------------\n"+
                               "\t \t \t-SKILLED GAME COMPLETED-\n"+
                               "\t \t \t-------------------------\n")
                        ReplayGame = input("Do you want to play again? Y or N:")
                        replay(ReplayGame.upper())
                elif (DifficultyChoice == "EXPERT" or DifficultyChoice == "E"):
                        ExpertGame()
                        print ("\t \t \t-------------------------\n"+
                               "\t \t \t-EXPERT GAME COMPLETED-\n"+
                               "\t \t \t-------------------------\n")
                        ReplayGame = input("\n Do you want to play again? "
                                           "Y or N:")
                        replay(ReplayGame.upper())
                elif (DifficultyChoice == "QUIT" or DifficultyChoice == "Q"):
                        # As user has choose to quit, the program will terminate.
                        print ("\n \t Hope to see you soon!! By-Bye!")
                        time.sleep(2)
                        sys.exit()
MainGame()
