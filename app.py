import random
import time
from tabulate import tabulate # imports our table
VocabArray = ["help", "savedData", "EnterVocab"] # Creates Array

randomNumber = random.randint(1, 2)

def addVocabulary():
    vocab = input("Enter Vocabulary: \n")
    print("Vocabulary/Variable Saved. |", vocab)
    VocabArray.append(vocab) # Saves Inputted Variable into a array which you can access.



if randomNumber == 1: # Randomising Greetings
    print("Hello there!")
elif randomNumber == 2:
    print("Hi!")

time.sleep(1.5)

name = input("What's your name? \n")
print("Epic!", name, "is such a cool name!")

time.sleep(0.75)

Commands = [ # Commands that we have
    ["Help", "Shows the list of commands"],
    ["savedData", "Inputted Commands"],
    ["EnterVocab", "Submit Vocabulary"]
]

head = ["Commands", "Description"] # header of the help menu



print(tabulate(Commands, headers=head, tablefmt="grid")) # Prints the help menu

Decision = input("Would you like to submit some vocabulary? (Y), (N) \n")


def EnterCommand():
    command = input("Please enter a command.")

    if command == "help":
        print(tabulate(Commands, headers=head, tablefmt="grid")) # Prints the help menu
        EnterCommand()
    elif command == "savedData":
        print(VocabArray)
        EnterCommand()
    elif command == "EnterVocab":
        addVocabulary()
        EnterCommand()
    elif command in VocabArray:
        print(command)
        EnterCommand()

if Decision == "N":
    print("Okay!")
    EnterCommand()
elif Decision == "Y":
    addVocabulary() # adds the vocabulary to Line 13
    EnterCommand()
