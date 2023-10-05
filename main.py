import os
import functions
import saySomething


def main():
    #i wanted the window size to be consistent across the board. this sets the size
    os.system('mode 65,10')
    os.system('color 0B')

    saySomething.printOmni()
    saySomething.welcome()
    next = input()
    isItTimeToLeave = False
    while isItTimeToLeave == False:
        os.system('cls')
        saySomething.printMenu()
        selection = input("enter selection here: ")
        match selection:
            case "5":
                isItTimeToLeave = True
            case "1":
                functions.listScores()
            case "2":
                functions.resetScores()
            case "3":
                functions.createInspector()
            case "4":
                functions.deleteInspector()
            case "1978":
                functions.originEaster()
            case "6":
                os.system('cls')
                functions.humanType("Hello! I'm afraid this number isn't a selection. You can only enter "+
                "numbers 1-5. Definitley do not enter 7")
                next = input("press enter to continue ...")
            case "7":
                os.system('cls')
                functions.humanType("Look, there's nothing here. \n.\n.\n.\n.\n.\n.\n.\n.\n"+
                "and even if there was an Easter egg, which there isn't, it would have nothing to do with an important year\n")
                next = input("press enter to continue")


    os.system('cls')
    saySomething.goodbye()


main()