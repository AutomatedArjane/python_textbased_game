# all variables and functions needed for the story

from AllFunctions import *
from character_class import *
from goal_class import *

##########################################################################
#                           CHARACTER CREATION                           #
##########################################################################

# create a character using the class "Character"
def create_character():

    name = input("What is your name? ") # ask the user for the name of their character
    
    while True: # ask the user for the character's gender, only specific replies are allowed
        gender = input("How do you wish to be known? Choose male/female/other: ")
        if gender not in ("male", "female", "other"):
            print("Please pick one of the available options.")
        else:
            break
        
    char_status = {"Day": 0, "Gold": 0, "Animal xp": 0, "Dex xp": 0, "Entertainment xp": 0, "Level": 0} # create the statistics of the character

    
    # create a character "mycharacter"
    mycharacter = Character(name, gender, char_status)
    return mycharacter

##########################################################################
#                              GOAL SETTING                              #
##########################################################################

# create a character using the class "Goal"
def create_goal():
    # ask for the goal name: this will get the data from the chosen goal and set it as the goal for the current game
    goal_name = input('You can choose from three different goals in this game: "buy horse", "get own house" and "buy lute".\nEach goal takes a certain number of days to achieve, and has a set amount of xp and gold you need to collect.\nType the name of the goal you want to choose here: ') # ask the user for their preferred goal
    
    Goal.goal_values(goal_name) # this doesn't work, find out why

    # create a goal "mygoal"
    mygoal = Goal(goal_name, animal_xp_goal, dex_xp_goal, entertainment_xp_goal, gold_goal) # check why there's wriggly lines here
    return mygoal


def game_won(mycharacter: Character): # I coded this very fast, check that it works!
    print(f"Congrats, you achieved your goal: buy horse")
    you_won_status = mycharacter.get_char_status()

    for key, value in you_won_status.items():
        print(get_animal_xp_goal) # fix this
        print(key, ":", value)

def game_lost(self, char_status: Character): # I coded this very fast, check that it works!
    print(f"Unfortunately you didn't manage to achieve your goal: buy horse") # continue coding this

