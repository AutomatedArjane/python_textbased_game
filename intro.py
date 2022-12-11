##########################################################################
#                                GAME INTRO                              #
##########################################################################

def enter_button():
    """this function is meant to pause the game at set intervals. 
    Text will appear block by block and the game will only continue after the user presses enter """
    while True:

        reply = input("")
        if reply == "":
            break

        elif reply =="quit":
            print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
            exit()            

        else: 
            print('\nOnly the enter button enables you to continue. '
            f'Press enter or type "quit" if you want to quit the game.\n')

def game_intro():
    """ here, the idea of the game is explained, and how to play it
    the player can type "quit" in reply to any question in 
    order to quit the game (this works throughout the whole game) """
    
    print("\n------------------------------------------------------------------------------------------")
    print('WELCOME TO THE FANTASY GAME "WOIANZII"\n\n\nThis game was completed by Arjane Kerkhoven on '
    f'11.12.2022,\nas part of the Ohjelmoinnin Perusteet course at JAMK in Jyväskylä.\n\n(Click '
    f'in the console and press enter to continue. Type "quit" to exit the game.)\n\n'
    f'------------------------------------------------------------------------------------------')

    enter_button()

    print("You can play this game with your keyboard. The program will\nprompt you with a question, "
    f"and you can type the answer into the console.\nDuring the game, you go on a quest that you can "
    f"choose yourself. In order to fulfill this quest, you have to gain enough gold and\nexperience "
    f"points (divided over 3 categories). Each quest has different end goals.\n(press enter to continue)\n\n"
    f"------------------------------------------------------------------------------------------")
    
    enter_button()

    print("At the beginning of the game, you are asked to provide some information\nabout your "
    f"character (you can make that up yourself). The game then shows\nyou your character and "
    f"the amount of gold and xp they have (zero is default).\nIt also shows you what the "
    f"current day is. After this, you choose a goal.\n\n"
    f"------------------------------------------------------------------------------------------")

    enter_button()

    print("The goal's requirements are shown, and this is where the main part\nof the game starts. "
    f"For each day of your quest, you can choose a city to visit. Each city has various jobs on "
    f"offer that can gain you gold and xp.\nTry to choose the jobs that bring you closer to your goal.\n\n"
    f"------------------------------------------------------------------------------------------")

    enter_button()

    print('Once the days are up, you have either achieved your goal,\nor you have not. If you '
    f'did not succeed, you can always try again.\n\nGood luck!\nPs. If you want to quit at any time, '
    f'please type "quit" as a reply to any question. Your progress will be saved automatically!\n\n'
    f'------------------------------------------------------------------------------------------')

    enter_button()

    while True:
        answer = input("\nAre you ready to play the game? Type yes or no: ")

        if answer not in ("yes", "Yes", "no", "No"):
            if answer == "quit":
                print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                exit()
                
            else:
                print("\nPlease pick one of the available options.\n")
                
        elif answer == "no" or answer == "No":
            print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
            exit()

        elif answer == "yes" or answer == "Yes":
            break

    print("\nExcellent! Welcome to the fantasy world of Woianzii. "
    f"Now, it is time to create your character. Start by choosing your name.\n"
    f"If you have a saved character, the game will automatically download it for you.\n")