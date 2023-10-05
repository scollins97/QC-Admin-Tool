#this python program stores all the functions
import time
import random
import sys
import sqlFunctions
import os
import saySomething

#this is a cool function i picked up from a stack overflow discussion
#it basically randomly pauses between every single character in the string passed in 
#that looks as if its being typed in real time by a human. gives a gamey feel
def humanType(words):
    words += "\n"
    for char in words:
        time.sleep(random.choice([
          0.3, 0.11, 0.08, 0.07, 0.07,
          0.07, 0.06, 0.06, 0.05, 0.01
        ]))
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
#this function reteives all objects from inspectors table and lists
#their name and score to console.  
def listScores():
    os.system('cls')
    inspectors = sqlFunctions.fetchAllInspectors()
    for inspector in inspectors:
        print(f"{inspector[0]}-{inspector[1]}: {inspector[2]}")
    next = input("press enter to continue")
#this function creates a new inspector
#it passes an integer, string, and another number into a 
#sql function
def createInspector():
    os.system('cls')
    #need to ask user some questions about new inspector
    id = input("What is their employee number? : ")
    theirName = input("What's their first name? : ")
    os.system('cls')
    humanType("ok, let's double check that information")
    print(f"Name: {theirName}\nEmployee Number: {id}")
    answer = input("Is this correct? (Y/N) : ")
    os.system('cls')
    if answer == "Y":
        sqlFunctions.insertNewInspector(id, theirName)
        humanType("all set\ni recommend you reset everyone's scores")
        next = input("press enter to continue")
    else:
        humanType("oh well, let's try again") 
#this function calls a SQL function to reset all scores to 0
def resetScores():
    os.system('cls')
    humanType("you're about to reset every score for"+
                " every inspector to zero")
    password = input("Type 'ABRACADABRA' to confirm : ")
    os.system('cls')
    if password == "ABRACADABRA":
        sqlFunctions.resetScoresToZero()
        humanType("all points have been destroyed. returning to main menu ...")
    else:
        print("incorrect word\npress enter to continue")
        next = input()
def deleteInspector():
    os.system('cls')
    humanType("tragic to see them go ... anyway")
    os.system('cls')
    id = input("Enter their employee ID: ")
    humanType(f"the inspector with the employee Id {id} will now be targeted\n for immediate deletion ...")
    sqlFunctions.deleteInspector(id)
    humanType("it has been done, heading back to the main menu ...")
def originEaster():
    os.system('cls')
    saySomething.theLongOne()
    next = input("press enter to continue")