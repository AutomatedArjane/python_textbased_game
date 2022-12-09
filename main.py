from intro import (
    enter_button
)

from character import (
    Character
)

from goal import (
    Goal
)

##########################################################################
#                           CHARACTER CREATION                           #
##########################################################################

def print_greeting(character):
    print(f'Good morning, {character.get_character_title()} {character.get_name()}! It is currently day '
    f'{character.get_current_quest_day()} of {character.goal.get_total_quest_days()} of your quest "{character.goal.get_goal_name()}"')


# create a character using the class "Character"
def create_character():

    while True:
        name = input("What is your name? ") # ask the user for the name of their character
        if name == "":
            print("Please write your name.")
        elif name == "quit":
            print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
            exit()
        else:
            break

    while True: # ask the user for the character's gender, only specific replies are allowed
        gender = input("\nHow do you wish to be known? Choose male/female/other: ")
        if gender not in ("male", "female", "other"):
            if gender == "quit":
                print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                exit()
            
            else:
                print("\nPlease pick one of the available options.\n")
        else:
            break
    if gender == "male":
        character_title = "Master"
    
    elif gender == "female":
        character_title = "Lady"

    elif gender == "other":
        character_title = "Honorable"

    # create the statistics of the character     
    current_quest_day = 1
    gold = 0
    animal_xp = 0
    dex_xp = 0
    entertainment_xp = 0

    print(f"\nIt is a pleasure to meet you, {character_title} {name}! Please press enter to continue.\n\n"
    f"------------------------------------------------------------------------------------------")
    
    enter_button()

    # create a character "character"
    character = Character(name, character_title, current_quest_day, gold, animal_xp, dex_xp, entertainment_xp)

    return character