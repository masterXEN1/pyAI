import time
On = True

def BootCalculator():
    if On == True:
        print("PyAI: Calculator Loading...")
        time.sleep(3)
        print("PyAI: Calculator Loaded!")

def enterKey():
    number1 = int(input("Please insert the first number. \n"))
    operator = input("Please insert the operator. | +-x/ \n")
    number2 = int(input("Please insert the second number. \n"))
    time.sleep(0.75)

    if operator == "+":
        finished = number1 + number2
    elif operator == "-":
       finished = number1 - number2
    elif operator == "/":
        finished = number1 / number2
    elif operator == "x":
        finished = number1 * number2
    
    time.sleep(0.5)
    print("Your answer is:", finished)

# Due to python's compiler, some answers may differ to other calculators.
# Only for testing & learning purposes.

BootCalculator()
enterKey()
