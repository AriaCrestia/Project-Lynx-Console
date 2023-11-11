import os
from lynx_files import calculator

class Handler:
    def __init__(self, choice):
        self.choice = choice
    def Choices(self):
        os.system("clear")
        if self.choice == 1:
            CalculatorLink.MathInput()


class CalculatorLink:
    def MathInput():
        done = False
        while done != True:
            try:
                print("Lynx - Console\n")
                print("1: Add")
                print("2: Subtract")
                print("3: Divide")
                print("4: Multiply")
                print("5: Division(remainder only)")
                print("6: Division(nearest whole number)")
                print("7: Square root")
                print("8: Cube root")
                print("\nE: Exit")
                userInput = input("    -> ")
                if userInput.lower() == "e":
                    os.system("clear")
                    done = True
                    break
                else:
                    userInput = int(userInput)
                CalculatorLink.MathChoice(userInput)
            except KeyboardInterrupt:
                done = True
            except ValueError as e:
                os.system("clear")
                print("Error: Incorrect option.")
    def MathChoice(choice):
        if choice == 1:
            os.system("clear")
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            print(calculator.Core4(num1, num2).AddFunc())
            print()
        elif choice == 2:
            os.system("clear")
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            print(calculator.Core4(num1, num2).SubtractFunc())
            print()
        elif choice == 3:
            os.system("clear")
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            print(calculator.Core4(num1, num2).DivideFunc())
            print()
        elif choice == 4:
            os.system("clear")
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            print(calculator.Core4(num1, num2).MultiplyFunc())
            print()
        elif choice == 5:
            os.system("clear")
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            print(calculator.AdditionalOps(num1, num2).ModuloFunc())
            print()
        elif choice == 6:
            os.system("clear")
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            print(calculator.AdditionalOps(num1, num2).FloorDivisionFunc())
            print()
        elif choice == 7:
            os.system("clear")
            num1 = int(input("Enter number: "))
            print(calculator.AdditionalOps(num1).SquareRoot())
            print()
        elif choice == 8:
            os.system("clear")
            num1 = int(input("Enter number: "))
            print(calculator.AdditionalOps(num1).CubeRoot())
            print()
        else:
            os.system("clear")
            print("Error: Incorrect option.")