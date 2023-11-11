try:
    import os
    import threading
    from lynx_files import handler
except Exception as e:
    print("Import error: ", e)
# end try

os.system("clear")
end = False
while end != True:
    try:
        # os.system("clear")
        print("Lynx - Console\n")
        print("1: Calculator")
        print("\nE: Exit")
        userInput = input("    -> ")
        if userInput.lower() == "e":
            end = True
        elif int(userInput) > 1 or int(userInput) < 1:
            os.system("clear")
            print("Error: Incorrect option")
        else:
            userInput = int(userInput)
            handler.Handler(userInput).Choices()
    except KeyboardInterrupt:
        print("You ended the program.")
        end = True
    except ValueError:
        os.system("clear")
        print("Error: Incorrect option")