#import pyfiglet
import functions

def printOmni():
    #ASCII_art_1 = pyfiglet.figlet_format("Omni")
    #print(ASCII_art_1)
    print("startup complete")
    return

def welcome():
    functions.humanType("hello, and welcome to the QC Selector Admin Page \n" +
                            "press enter to get started  . . .")
    return

def goodbye():
    functions.humanType("goodbye  ...")

def printMenu():
    print("Select your Option by entering a Number")
    print("1. View all Inspectors\n"+
            "2. Reset all Scores\n"+
            "3. Create a new Inspector\n"+
            "4. Delete an Inspector\n"+
            "5. Exit\n")
    return
def theLongOne():
    functions.humanType("Congratulations on finding "+
    "the Easter egg! "+ 
    "I'm glad you"+
    " enjoyed your little scavenger hunt. But seriously, "+
    "did you have"+
    " nothing better to do with your time? "+
    "\nI know what you're thinking:\n\n"+
     "'Easter eggs are fun! They're a way to "+
     "show that the developers"+
    " have a sense of humor and that they care "+
     "about their users.'\n\n"+ 
    " And I agree. Easter eggs can be fun. "+
    "But they're also a waste of time."+
    " Think about it. The developers spent hours upon hours"+ 
    " creating this Easter egg, just so that you could find it"+
    " and spend a few seconds giggling about it. And then what?"+
    " You go back to using the program like normal. But what if"+
    " those developers had spent that time on something more"+
    " important? Like fixing bugs or adding new features. Or even"+
    " just taking a break and enjoying their lives. But no, "+
    "instead they wasted their time on an Easter egg. And for"+
    " what? So that you could find it and spend a few seconds"+
    " giggling about it. I'm not saying you"+
    " shouldn't enjoy Easter"+
    " eggs. But I am saying that you shouldn't take them too "+
    "seriously. They're just a fun little diversion."+
    " Not something"+
    " to waste your time on.\n \n \n Now, go back to work."+
     " You have things to do.\n\n\n(But seriously, if you have"+
    " nothing better to do, here are a few more Easter"+
     " eggs that you can try to find in my program:"+
    "\nIf you click on the logo 10 times in a row, "+
    "it will turn into a picture of a cat."+
    "\nIf you hold down the 'Ctrl' and 'Alt'"+
    " keys and type 'easter egg' into the search bar,"+
    " a secret menu will appear."+
    "\nIf you type 'I'm bored' into the chat window,"+
    " I will tell you a joke."+
    "\nBut please, don't waste your whole day on this."+
    " You have more important things to do.)")