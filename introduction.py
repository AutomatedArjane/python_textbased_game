from day_tasks import (
    choose_travel_destination,
    choose_job,
    do_job
)

from main import (
    create_character,
    create_goal,
)

from introduction import (
    enter_button,
    game_intro
)

from character import (
    Character
)

from goal import (
    Goal
)

def enter_button(): # the user can make the text appear block by block through pressing the enter button
    while True:

        reply = input("")
        if reply == "":
            break

        elif reply =="quit":
            print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
            exit()            

        else: 
            print('\nOnly the enter button enables you to continue. Press enter or type "quit" if you want to quit the game.\n')

def game_intro():
    
    print("\n------------------------------------------------------------------------------------------")
    print('WELCOME TO THE FANTASY GAME "WOIANZII"\n\n\nThis game was created by Arjane Kerkhoven on 11.12.2022,\nas part of the Ohjelmoinnin Perusteet course at JAMK in Jyväskylä.\n\n(Click in the console and press enter to continue. Type "quit" to exit the game.)\n')
    print("------------------------------------------------------------------------------------------")

    enter_button()

    print("You can play this game with your keyboard. The program will\nprompt you with a question, and you can type the answer into the console.\nDuring the game, you go on a quest that you can choose yourself.")
    print("In order to fulfill this quest, you have to gain enough gold and\nexperience points (divided over 3 categories). Each quest has different end goals.\n(press enter to continue)\n")
    print("------------------------------------------------------------------------------------------")
    
    enter_button()

    print("At the beginning of the game, you are asked to provide some information\nabout your character (you can make that up yourself). The game then shows")
    print("you your character and the amount of gold and xp they have (zero is default).\nIt also shows you what the current day is. After this, you choose a goal.\n")
    print("------------------------------------------------------------------------------------------")

    enter_button()

    print("The goal's requirements are shown, and this is where the main part\nof the game starts. For each day of your quest, you can choose a city to visit.")
    print("Each city has various jobs on offer that can gain you gold and xp.\nTry to choose the jobs that bring you closer to your goal.\n")
    print("------------------------------------------------------------------------------------------")

    enter_button()

    print("Once the days are up, you have either achieved your goal,\nor you have not. If you didn't succeed, you can always try again.\n\nGood luck!")
    print('\nPs. If you want to quit at any time, please type "quit" as a reply to any question.')
    print("------------------------------------------------------------------------------------------")

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

    print("\nExcellent! Welcome to the fantasy world of Woianzii. Now, it is time to create your character. Start by choosing your name:\n")