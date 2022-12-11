from intro import (
    enter_button
)

from character import (
    Character
)

import os

##########################################################################
#                           CHARACTER CREATION                           #
##########################################################################


def print_greeting(character):
    """ print the greeting of the day """

    print(
    f'Good morning, {character.get_character_title()} {character.get_name()}!'
    f'It is currently day {character.get_current_quest_day()} of '
    f'{character.goal.get_total_quest_days()} of your quest '
    f'"{character.goal.get_goal_name()}"'
    )

FILE_NAME = "saved_game.txt"


def get_old_character_if_it_exists():
    """download the details of your old character, after checking if it exists """
    
    character_stats = [""]

    try:
        path = os.path.expanduser("~")
        file = FILE_NAME
        filename2 = path + "/" + file

        if os.path.exists(filename2):
            file = open(filename2, "r")

        else:
            return

        for item in file:
            if len(item) > 0:
                character_stats.append(item.strip())
        character_stats.remove("")

        if character_stats:
            name = character_stats[1]
            character_title = character_stats[2]
            current_quest_day = int(character_stats[3])
            gold = int(character_stats[4])
            animal_xp = int(character_stats[5])
            dex_xp = int(character_stats[6])
            entertainment_xp = int(character_stats[7])
            
            file.close()

            character = Character(
                name, 
                character_title, 
                current_quest_day, 
                gold, 
                animal_xp, 
                dex_xp, 
                entertainment_xp, 
                FILE_NAME
                )

            character.goal.set_saved_quest_days(
            character.goal.get_total_quest_days() 
            - current_quest_day + 1
            )
            
            print(
            "You have downloaded a previously saved character. "
            f"Have fun continuing your game!"
            )

            return character

        return

    except Exception as e:
        print(
            f"Failed to access file '{file}' while downloading saved "
            f"your character: {e}.\n\nThe game has now closed."
        )

        exit()


def create_character():
    """ create a character using the class "Character" """
    
    """ ask the user for the name of their character, 
    empty strings are not allowed 
    """
    while True:
        name = input(
        "What is your name? "
        )

        if name == "":
            print(
            "Please write your name."
            )

        elif name == "quit":
            print(
            "\nYou have quit the game, thank you for playing. "
            f"Come back soon to play again!\n"
            )

            exit()
        else:
            break

    # set the character's title
    while True:    
        gender = input(
        "\nHow do you wish to be known? Choose male/female/other: "
        )

        if gender not in ("male", "female", "other"):
            if gender == "quit":
                print(
                "\nYou have quit the game, thank you "
                f"for playing. Come back soon to play again!\n"
                )
                
                exit()
            
            else:
                print(
                "\nPlease pick one of the available options.\n"
                )

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

    print(
    f"\nIt is a pleasure to meet you, {character_title} "
    f"{name}! Please press enter to continue.\n\n"
    f"-----------------------------------------"
    f"-------------------------------------------------"
    )
    
    enter_button()

    # create a character "character" using the information the user gave
    character = Character(
        name, 
        character_title, 
        current_quest_day, 
        gold, 
        animal_xp, 
        dex_xp, 
        entertainment_xp, 
        FILE_NAME
        )

    return character