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
    Quest_day = 0
    Gold = 0
    Animal_xp = 0
    Dex_xp = 0
    Entertainment_xp = 0
    Level = 0
    
    # create a character "mycharacter"
    mycharacter = Character(name, gender, Quest_day, Gold, Animal_xp, Dex_xp, Entertainment_xp, Level)
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


def game_won(mycharacter: Character, mygoal: Goal): # I coded this very fast, check that it works!
    print(f"Congratulations, you achieved your goal: {mygoal.goal_name}.\n\nYou won on day {mycharacter.get_quest_day} of {mygoal.get_no_of_quest_days}. You collected:\n- {mycharacter.get_gold} of {mygoal.get_gold} gold\n- {mycharacter.get_animal_xp} of {mygoal.get_animal_xp} gold\n- {mycharacter.get_dex_xp} of {mygoal.get_dex_xp} gold\n- {mycharacter.get_entertainment_xp} of {mygoal.get_entertainment_xp} gold\n You have achieved level {mycharacter.get_level}")


def game_lost(mycharacter: Character, mygoal: Goal): # I coded this very fast, check that it works!
    print(f"Unfortunately you didn't manage to achieve your goal: buy horse") # continue coding this

    print(f"It is now the last day of your quest, day {mygoal.get_no_of_quest_days}. Unfortunately you haven't managed to achieve your goal: {mygoal.goal_name}.\n\nYou collected:\n- {mycharacter.get_gold} of {mygoal.get_gold} gold\n- {mycharacter.get_animal_xp} of {mygoal.get_animal_xp} gold\n- {mycharacter.get_dex_xp} of {mygoal.get_dex_xp} gold\n- {mycharacter.get_entertainment_xp} of {mygoal.get_entertainment_xp} gold\n You have achieved level {mycharacter.get_level}")

