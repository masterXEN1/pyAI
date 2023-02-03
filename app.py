import random
import time
from tabulate import tabulate # imports our table



randomNumber = random.randint(1, 2)

def addVocabulary():
    vocab = input("Enter Vocabulary: \n")
    print("Vocabulary/Variable Saved. |", vocab)
    VocabArray = [] # Creates Array
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

if Decision == "N":
    print("Okay!")
elif Decision == "Y":
    addVocabulary() # adds the vocabulary to Line 13

