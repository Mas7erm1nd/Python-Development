import os
from os import path

yes = ("yes", "ye", "y")
no = ("no", "n")

Directory = os.getcwd()
GameVersion = "V_1.1"
GameFileName = "21_Game_Official_{}.py".format(GameVersion)
GamePath = Directory + "/" + GameFileName
GameCode = '''import random

# The press function that requires user to press 'ENTER'
def press():
    input("[Tap ENTER to proceed]*")

# If a Cheat is detected, this function is called
def cheat():
    print("*Cheat Detected! Please restart the Game*")
    press()
    exit()

# Function to handle blank or no inputs
def blank():
    print("*Integer input is required, please restart the game!")
    press()
    exit()

def credits():
    print("""Before we start. 
        ##Credits##
        Developers : Aadel (3adel)
                     Keshan
        Created using : Python
        Release Date : Wednesday 19th June, 2019
        """)

# This is the Bot's Response Generator Function
def ResponseGenerator(UserInput):
    BotResponse = 0
    LowerRangeLimit = UserInput + 1
    UpperRangeLimit = UserInput + 5
    BotResponse = random.sample(range(LowerRangeLimit, UpperRangeLimit), 1)
    return BotResponse
        
# Main Game Process
def Game():
    print("First Round, Start!")
    # UserInput takes the number the user inputs
    try:
        UserInput = input("*Enter a Number from 1 to 4 : ")
        print(Name,":", UserInput)
        press()

        # The bot generates a response based on the user's input
        if UserInput in ("1", "2", "3", "4"):
            Response = ResponseGenerator(int(UserInput))
            print(bot, Response)
        elif UserInput == (""):
            blank()
        else:
            cheat()
        press()

    except KeyboardInterrupt as error:
            print("*[ERROR] : Program Interrupted")
            print("Program Exiting...*")

    print("*You are now in the Second Round! Keep going!")
    
    try:
        UserInput = input("Enter a Number from 5 to 12 : ")
        print(Name,":",UserInput)
        press()

        if UserInput in ("5", "6", "7", "8", "9", "10", "11", "12"):
            Response = ResponseGenerator(int(UserInput))
            print(bot, Response)
        elif UserInput == (""):
            blank()
        else:
            cheat()
        press()
    
    except KeyboardInterrupt as error:
            print("*[ERROR] : Program Interrupted")
            print("Program Exiting...*")

    print("*You are now in the Third Round! Good Job!")
    
    try:
        UserInput = input("Enter a Number from 12 to 16 : ")
        print(Name,":",UserInput)
        
        if UserInput in ("12", "13", "14", "15", "16"):
            Response = ResponseGenerator(int(UserInput))
            print(bot, Response)
        elif UserInput == (""):
            blank()
        else:
            cheat()
        press()

    except KeyboardInterrupt as error:
            print("*[ERROR] : Program Interrupted")
            print("Program Exiting...*")

    print("*You are now in the Fourth Round! Almost there!")
    
    try:
        UserInput = input("Enter a Number from 16 to 21 : ")
        print(Name,":",UserInput)

        if UserInput == ("16"):
            Response = ResponseGenerator(int(UserInput))
            print(bot,Response)
        elif UserInput in ("17", "18", "19", "20"):
            print(bot, " 21")
            print("Bot-D won! ")
            input("*-- Press \'ENTER\' to exit game --*")
            exit()
        elif UserInput==("21"):
            print("""
                    Congratulations!
            You have won the game. Great Job!
            """)
            input("*-- Press \'ENTER\' to exit game --*")
            exit()
        elif UserInput==(""):
            blank()
        else:
            cheat()
    
    except KeyboardInterrupt as error:
            print("*[ERROR] : Program Interrupted")
            print("Program Exiting...*")

    print("[NOTE : Bot-D has not reached 21 and this is the last round!]")
    
    try:
        UserInput = input("Enter 21 to Win the Game! : ")
        if UserInput == ("21"):
            print("""
                    Congratulations!
            You have won the game. Great Job!""")
            input("*-- Press \'ENTER\' to exit game --*")
            exit()
        elif UserInput == (""):
            blank()
        else:
            cheat()
        press()
        exit()
    
    except KeyboardInterrupt as error:
            print("*[ERROR] : Program Interrupted")
            print("Program Exiting...*")

if __name__ == '__main__':

    # Bot Console Prompt
    bot = ("Bot-D :")

    # List of bad words. We try to keep the game family-friendly here!
    BadWords = ["gay","fuck","bitch","shit","bulshit","poop","fucker",\
        "mother fucker", "damn", "fucking"]

    print("""
            --    Welcome to the 21 Game!    --
                                                """)

    print('Hello there! My name is Bot-D!')
    Name = input('What\\'s your name? : ')
    try:
        if Name in BadWords:
            print("Watch your language! ")
            press()
            exit()
        elif Name in ("", " "):
            Name = "Unknown"
            print("*Oh, nice to meet you {}!".format(Name))
        elif Name.lower() in ("aadel", "adel", "3adel", "keshan"):
            print("*Oh, nice to meet you Creator of the game")
        else:
            print("*Oh, nice to meet you {}!".format(Name))
    
    except KeyboardInterrupt as error:
            print("*[ERROR] : Program Interrupted")
            print("Program Exiting...*")


    print('My developers developed me to run a game called 21')
    press()
    print('Would you like to play it?(Yes/No)')
    Answer = input(' Your Answer:')

    try:
        # Checks if answer is in the 'yes' list
        if Answer.lower() in ("yes", "y", "ye"):
            print('*Okay, Let me tell you the rules')
        
        # Checks if answer is in the 'no' list
        elif Answer.lower() in ("no", "n"):
            print("*How dare you? You should play the game anyway!")
            print("Let\'s start by telling you how it\'s played and what are the rules")
        else:
            print('*Was that an answer? :)')
            press()

    except KeyboardInterrupt as error:
            print("*[ERROR] : Program Interrupted")
            print("Program Exiting...*")

    print("""
                                Rules :

        Every person has to approach in a specified range of steps.
    Whoever reaches the number 21 first, wins. Do not enter a higher 
    or lower number than the specified range or you will be disqualified.

    Let's begin!    """)
    press()
    
    # Calls the main function of the Game
    Game()'''


def press():
	input("[Tap 'ENTER' to proceed]\n")


def Download():
    OldCode = ''
    NewCode = ''

    if path.exists(str(GamePath)) == True:
        print("[ERROR] : File Already Exists!")
        RewriteConfirm = input("\nDo you want to replace Game File? (Yes/No) : ")
        
        try:
            if RewriteConfirm.lower() in yes:
                DownloadFileOverwrite = open(GameFileName,"w+")
                DownloadFileOverwrite.write(GameCode)
                DownloadFileOverwrite.close()
            
                with open(GameFileName,"r") as DownloadFileOverwrite:
                    OldCode = DownloadFileOverwrite.read()
            
                NewCode = OldCode.replace("*", "\\n")
            
                with open(GameFileName,"w") as DownloadFileOverwrite:
                    DownloadFileOverwrite.write(NewCode)

                DownloadFileOverwrite.close()

            elif RewriteConfirm.lower() in no:
                print("\n[NOTICE] : Game File was not replaced. File located at {}".format(GamePath))
                print("[NOTICE] : Run the following comand to play game, python {}\n".format(GameFileName))
                exit()
            else:
                print("[ERROR] : Invalid Input. Please Retry")
                Download()
        
        except KeyboardInterrupt:
            print("\n[ERROR] : Program Interrupted")
            print("Program Exiting...\n")

    elif path.exists(str(GamePath)) == False:
        DownloadFile = open(GameFileName,"w+")
        DownloadFile.write(GameCode)
        DownloadFile.close()
        
        with open(GameFileName,"r") as DownloadFile:
            OldCode = DownloadFile.read()
        
        NewCode = OldCode.replace("*", "\\n")
        
        with open(GameFileName,"w") as DownloadFile:
            DownloadFile.write(NewCode)

        DownloadFile.close()

    else:
        print("[ERROR] : Invalid Input. Please Retry")
        Download()


def GameInstallation():
    UserAccept = input("Enter Exit to cancel Installation\nDo you want to Install the 21 Game? : ")
    try:
        if UserAccept.lower() in yes:
            Download()
            print("\n[NOTICE] : Game Downloading in Progress...")
            press()
            print("[NOTICE] : Game was Installed at",GamePath)
            print("[NOTICE] : Run the following comand to play game, python {}\n".format(GameFileName))
            exit()
        elif UserAccept.lower() in no:
            print("\n[ERROR] : Game was not Installed\n Exiting...\n")
            exit()
        elif str(UserAccept.lower()) == "exit":
            print("\n[NOTICE] : Installation Cancelled\n Exiting...\n")
            exit()
        else:
            print("\n[ERROR] : Invalid Input. Please Retry")
            GameInstallation()
    
    except KeyboardInterrupt:
        print("\n[ERROR] : Program Interrupted")
        print("Program Exiting...\n")


if __name__ == '__main__':
    print("""
        Welcome to the 21 Game Installation
        Game Installation will now Begin
    """)
    GameInstallation()
    
    
