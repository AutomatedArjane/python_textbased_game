##########################################################################
#                                GAME INTRO                              #
##########################################################################


def enter_button():
    """ this function is meant to pause the game at set intervals. 
    Text will appear block by block and the game will only continue 
    after the user presses enter  
    """
    while True:

        reply = input("")

        if reply == "":
            break

        elif reply =="quit":
            print(
            "\nYou have quit the game, thank you for playing. "
            f"Come back soon to play again!\n"
            )

            exit()            

        else: 
            print(
            '\nOnly the enter button enables you to continue. '
            f'Press enter or type "quit" if you want to quit the game.\n'
            )


def game_intro():
    """ here, the idea of the game is explained, and how to play it
    the player can type "quit" in reply to any question in 
    order to quit the game (this works throughout the whole game) 
    """
    
    print(
    '\n----------------------------------------------------'
    f'--------------------------------------\nWELCOME TO THE '
    f'FANTASY GAME "WOIANZII"\n\n\nThis game was completed '
    f'by Arjane Kerkhoven on 11.12.2022,\nas part of the '
    f'Ohjelmoinnin Perusteet course at JAMK in Jyväskylä.\n\n'
    f'(Click in the console and press enter to continue. '
    f'Type "quit" to exit the game.)\n\n-----------------'
    f'---------------------------------------------------'
    f'----------------------'
    )

    enter_button()

    print(
    "You can play this game with your keyboard. The program "
    f"will\nprompt you with a question, and you can type the "
    f"answer into the console.\nDuring the game, you go on a "
    f"quest that you can choose yourself.\nIn order to fulfill "
    f"this quest, you have to gain enough gold and\nexperience "
    f"points (divided over 3 categories). Each quest has "
    f"different end goals.\n(press enter to continue)\n\n"
    f"-------------------------------------------------"
    f"-----------------------------------------"
    )
    
    enter_button()

    print(
    "At the beginning of the game, you are asked to provide "
    f"some information\nabout your character (you can make "
    f"that up yourself). The game then shows\nyou your character and "
    f"the amount of gold and XP they have (zero is default).\n"
    f"It also shows you what the current day is. After this, "
    f"you choose a goal.\n\n---------------------------------"
    f"---------------------------------------------------------"
    )

    enter_button()

    print(
    "The goal's requirements are shown, and this is where the "
    f"main part\nof the game starts. For each day of your quest,"
    f" you can choose a city to visit.\nEach city has various jobs on "
    f"offer that can gain you gold and XP.\nTry to choose the "
    f"jobs that bring you closer to your goal.\n\n"
    f"-------------------------------------------------"
    f"-----------------------------------------"
    )

    enter_button()

    print(
    'Once the days are up, you have either achieved your goal,'
    f'\nor you have not. If you did not succeed, you can always '
    f'try again.\n\nGood luck!\nPs. If you want to quit at any time, '
    f'please type "quit" as a reply to any question.\nYour progress '
    f'will be saved automatically!\n\n---------------------------'
    f'---------------------------------------------------------------'
    )

    enter_button()

    while True:
        answer = input(
        "\nAre you ready to play the game? Type yes or no: "
        )

        if answer not in ("yes", "Yes", "no", "No"):
            if answer == "quit":
                print(
                "\nYou have quit the game, thank you for playing. "
                f"Come back soon to play again!\n"
                )

                exit()
                
            else:
                print(
                "\nPlease pick one of the available options.\n"
                )
                
        elif answer == "no" or answer == "No":
            print(
            "\nYou have quit the game, thank you for playing. "
            f"Come back soon to play again!\n"
            )

            exit()

        elif answer == "yes" or answer == "Yes":
            break

    print(
    "\nExcellent! Welcome to the fantasy world of Woianzii. "
    f"Now, it is time to create your character. Start by "
    f"choosing your name.\nIf you have a saved character, "
    f"the game will automatically download it for you.\n"
    )