import os
from lynx_files import calculator
from lynx_files import os_info

class Handler:
    def __init__(self, choice):
        self.choice = choice
    def Choices(self):
        os.system("clear")
        if self.choice == 1:
            CalculatorLink.MathInput()
        elif self.choice == 2:
            OSInfoLink.UserChoice()


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
            except ValueError:
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
 
class OSInfoLink:
    def UserChoice():
        done = False
        while done != True:
            try:
                print("1: Platform")
                print("2: Release version")
                print("3: Platform and release version")
                print("\nE: Exit")
                userInput = input("    -> ")
                if userInput.lower() == "e":
                    os.system("clear")
                    done = True
                    break
                else:
                    userInput = int(userInput)
                    OSInfoLink.Choices(userInput)
            except ValueError:
                os.system("clear")
                print(f"Error: Incorrect option.")
            except KeyboardInterrupt:
                os.system("clear")
                done = True
    def Choices(input):
        if input == 1:
            os.system("clear")
            print(os_info.SystemInfo.Platform())
            print()
        elif input == 2:
            os.system("clear")
            print(os_info.SystemInfo.ReleaseVer())
            print()
        elif input == 3:
            os.system("clear")
            print(os_info.SystemInfo.FullInfo())
            print()
        else:
            os.system("clear")
            print("Error: Incorrect option.")