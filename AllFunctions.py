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

    # create the statistics of the character     
    current_quest_day = 0
    gold = 0
    animal_xp = 0
    dex_xp = 0
    entertainment_xp = 0
    
    # create a character "mycharacter"
    mycharacter = Character(name, gender, current_quest_day, gold, animal_xp, dex_xp, entertainment_xp)
    return mycharacter

##########################################################################
#                              GOAL SETTING                              #
##########################################################################

# create a character using the class "Goal"
def create_goal():
    # ask for the goal name: this will get the data from the chosen goal and set it as the goal for the current game
    
    while True: # ask the user for their preferred goal, only specific replies are allowed
        goal_name = input('You can choose from three different goals in this game: "buy horse", "get own house" and "buy lute".\nEach goal takes a certain number of days to achieve, and has a set amount of xp and gold you need to collect.\nType the name of the goal you want to choose here: ') # ask the user for their preferred goal
        if goal_name not in ("buy horse", "get own house", "buy lute"):
            print("Please pick one of the available options.")
        else:
            break    
    
    
    # create a goal "mygoal"
    Goal.goal_values(goal_name)
    mygoal = Goal(goal_name, Goal.get_total_quest_days, Goal.get_animal_xp_goal, Goal.get_dex_xp_goal, Goal.get_entertainment_xp_goal, Goal.get_gold_goal)

    return mygoal


