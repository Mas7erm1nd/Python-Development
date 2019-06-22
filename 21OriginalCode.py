import random

# The press function that requires user to press 'ENTER'
def press():
    input("Tap enter to proceed\n")

# If a Cheat is detected, this function is called
def cheat():
    print("\nPlease don't cheat and restart the game! ")
    press()
    exit()

# Function to handle blank or no inputs
def blank():
    print("\nInteger input is required, please restart the game!")
    press()
    exit()

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
    UserInput = input("\nEnter a Number from 1 to 4 : ")
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

    print("\nYou are now in the Second Round! Keep going!")
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

    print("\nYou are now in the Third Round! Good Job!")
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

    print("\nYou are now in the Fourth Round! Almost there!")
    UserInput = input("Enter a Number from 16 to 21 : ")
    print(Name,":",UserInput)

    if UserInput == ("16"):
        Response = ResponseGenerator(int(UserInput))
        print(bot,Response)
    elif UserInput in ("17", "18", "19", "20"):
        print(bot, " 21")
        print("Bot-D won! ")
        press()
        exit()
    elif UserInput==("21"):
        print("You won!")
        input("\n-- Press \'ENTER\' to exit game --\n")
        exit()
    elif UserInput==(""):
        blank()
    else:
        cheat()


    print("[NOTE : Bot-D has not reached 21 and this is the last round!]")
    UserInput = input("Enter 21 to Win the Game! : ")
    if UserInput == ("21"):
        print("You won!")
        press()
        exit()
    elif UserInput == (""):
        blank()
    else:
        cheat()
    press()
    exit()

if __name__ == '__main__':

    # Bot Console Prompt
    bot = ("Bot-D :")

    # List of bad words. We try to keep the game family-friendly here!
    BadWords = ["gay","fuck","bitch","shit","bulshit","poop","fucker",\
        "mother fucker", "damn", "fucking"]

    print("""
            *    Welcome to the 21 Game!    *
                                                """)

    print('Hello there! My name is Bot-D!')
    Name = input('What\'s your name? : ')

    if Name in BadWords:
        print("Watch your language! ")
        press()
        exit()
    elif Name in ("", " "):
        Name = "Unknown"
        print("\nOh, nice to meet you {}!".format(Name))
    elif Name.lower() in ("aadel", "adel", "3adel", "keshan"):
        print("\nOh, nice to meet you Creator of the game")
    else:
        print("\nOh, nice to meet you {}!".format(Name))


    print('My developers developed me to run a game called 21')
    press()
    print('Would you like to play it?(Yes/No)')
    Answer = input(' Your Answer:')

     # Checks if answer is in the 'yes' list
    if Answer.lower() in ("yes", "y", "ye"):
        print('\nOkay, Let me tell you the rules')
    
     # Checks if answer is in the 'no' list
    elif Answer.lower() in ("no", "n"):
        print("\nHow dare you? You should play the game anyway!")
        print("Let\'s start by telling you how it\'s played and what are the rules")
    else:
        print('\nWas that an answer? :)')

    print("""
                                Rules :

        Every person has to approach in a specified range of steps.
    Whoever reaches the number 21 first, wins. Do not enter a higher
    or lower number than the specified range or you will be disqualified.

    Let's begin!    """)
    press()
    
    # Calls the main function of the Game
    Game()


#If you are a python developer can you help me build this game? and thanks.
#Keshan was here =p
