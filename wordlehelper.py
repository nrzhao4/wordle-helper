#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

# this list keeps track of previous states of the filtered word list
from gettext import find


WORDLIST_HIST = []

# this function is called on startup
def start():    
    wordList = loadWords()
    intro = "Welcome to Wordle Helper - here to help you solve your daily Wordle!"
    print(intro)

    printInstructions()
    
    # begin accepting user input to filter words
    findWords(wordList)

# this function loads the word list
def loadWords():
    with open("word-list.txt", "r") as tf:
        wordList = tf.read().split('\n')
    return wordList

# this function prints instructions for how to use Wordle Helper
def printInstructions():
    instructions = '''Type a command then press ENTER to filter through words. If entering multiple letters, no need to separate them with a comma. 
Type help then press ENTER at any time to see the list of available commands.'''
    print(instructions)
    commands = '''Available commands:
        no <letter(s)>
        contains <letter(s)>
        contains <letter> not <first/second/third/fourth/fifth>
        back
        restart
        <first/second/third/fourth/fifth> <letter>'''
    print(commands)

# use input to filter word list
def findWords(words):
        if len(words) == 0:
            print("Sorry, no more words match your criteria")
            return

        userInput = input("Type a command to start filtering words or type help the press ENTER: ")
        userInput = userInput.lower().split(' ')
        command = userInput[0]

        # special commands
        if command == "quit":
            return
        elif command == "help":
            printInstructions()
        elif command == "restart":
            loadWords()
            print("Word list reset")
        elif command == "back":
            words = WORDLIST_HIST.pop(len(WORDLIST_HIST)-1)
            printList(words)
        
        # check if input is valid
        if isValid(userInput) != True:
            print("Invalid user input. Try again")
        else:
            letters = userInput[1]
            secondaryArgs = []
            # optional secondary argument given with contains command
            if len(userInput) > 2:
                for x in range(2,4):
                    secondaryArgs.append(userInput[x])
            # filter words
            WORDLIST_HIST.append(words)
            words = filterWords(words, command, letters, secondaryArgs)
            printList(words)
        findWords(words)
                    

# this function checks if the user input is valid
def isValid(userInput):
    command = userInput[0]
    letters = userInput[1]

    # valid commands
    nonNumbered = {"no", "contains"}
    numbered = {"first", "second", "third", "fourth", "fifth"}
    
    # check that input has correct number of arguments
    if len(userInput) < 2:
        print("Your input does not have the correct number of arguments")
        return False
        # for commands other than no and contains, only one letter can be included
    if command != "contains" and len(userInput) > 2:
        print("The commands <first/second/third/fourth/fifth> can only include one letter")
        return False

    secondary = []
    if len(userInput) > 2:
        for x in range(2, len(userInput)):
            secondary.append(userInput[x])

    # check command is valid
    if command not in nonNumbered and command not in numbered:
        print("Enter a valid command")
        return False
    # check that input does not include numbers
    for char in letters:
        if char.isnumeric():
            print("Oops! Looks like you entered a numerical value instead of a letter")
            return False
    # the contains command can be followed by an additional 'not <first/second/third/fourth/fifth>'
    if command == "contains" and len(secondary) > 0:
        if len(secondary) != 2:
            print("Your input does not have the correct number of arguments")
            return False
        if secondary[0] != "not" or secondary[1] not in numbered:
            return False
    return True

# this function actualy performs the filtering
def filterWords(words, command, letters, secondaryArgs):
    # dict defines word place and corresponding index
    place = {
        "first": 0,
        "second": 1,
        "third": 2,
        "fourth": 3,
        "fifth": 4
    }

    # filter word list based on given criteria
    for char in letters:
        if command == "no":
            filtered = filter(lambda word: char not in word, words)
        elif command == "contains":
            if len(secondaryArgs) == 0:
                filtered = filter(lambda word: char in word, words)
            else:
                charPos = secondaryArgs[1]
                filtered = filter(lambda word: (char in word and char != word[place[charPos]]), words)
        elif command in place:
            filtered = filter(lambda word: char == word[place[command]], words)
        words = list(filtered)
    return words

# this function outputs the filtered word list
def printList(words):
    if len(words) <= 8:
            for x in range(len(words)):
                print(words[x])
    else:
        for x in range(len(words)):
            if x > 0 and x % 8 == 0:
                for i in range(9):
                    print(words[x-i], end = " ")
                print("\n")

# end program       
def end():
    print("\nThanks for using World Helper!")
    quit()

def main():
    start()
    end()


if __name__ == "__main__": 
	main() 