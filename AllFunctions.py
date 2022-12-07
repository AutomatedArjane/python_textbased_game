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
    if gender == "male":
        character_title = "Master"
    
    elif gender == "female":
        character_title = "Lady"

    elif gender == "other":
        character_title = "Honorable"

    # create the statistics of the character     
    current_quest_day = 0
    gold = 0
    animal_xp = 0
    dex_xp = 0
    entertainment_xp = 0
    
    # create a character "mycharacter"
    mycharacter = Character(name, character_title, current_quest_day, gold, animal_xp, dex_xp, entertainment_xp)
    return mycharacter

##########################################################################
#                              GOAL SETTING                              #
##########################################################################

# create a character using the class "Goal"
def create_goal():
    # ask for the goal name: this will get the data from the chosen goal and set it as the goal for the current game
    while True:
        goal_name = input('You can choose from three different goals in this game: "buy horse", "get own house" and "buy lute".\nEach goal takes a certain number of days to achieve, and has a set amount of xp and gold you need to collect.\n\nType the name of the goal you want to choose here: ') # ask the user for their preferred goal
    
        if goal_name not in ("buy horse", "get own house", "buy lute"):
            print("\nPlease pick one of the available options.\n")

        else:
            break

    mygoal = Goal(goal_name, Goal.get_total_quest_days, Goal.get_animal_xp_goal, Goal.get_dex_xp_goal, Goal.get_entertainment_xp_goal, Goal.get_gold_goal)

    # create a goal "mygoal"
    mygoal.set_goal_values(goal_name)

    return mygoal


##########################################################################
#                              CHOOSE TOWN                               #
##########################################################################

def choose_travel_destination():
    
    while True: # add name and character title
        town_name = input(f"Good morning, character_title()! It is now day current_quest_day() of total_quest_days() of your quest goal_name().\nTo which town would you like to travel today? You can choose between Novigrad, Oxenfurt, Vengerberg, Brugge and Hengfors: ")

        if town_name not in ("Novigrad", "Oxenfurt", "Vengerberg", "Brugge", "Hengfors"):
            print("\nPlease pick one of the available options.\n")
        else:
            break

    choose_job(town_name)

##########################################################################
#                               CHOOSE JOB                               #
##########################################################################

def choose_job(town_name): # OPTIONAL: add bonus xp depending on city and job!
    while True:
        if town_name == "Novigrad": # Add more explanation abouot the city, add name and character title
            job_name = input(f"\n\nWelcome to {town_name}, character_title(), name()! Any hard worker is welcome here. What kind of job would you be interested in today?\nYou can choose between farming, killing monsters, juggling and singing: ")
            
            if job_name not in ("farming", "killing monsters", "juggling", "singing"):
                print("\nPlease pick one of the available options.\n")
            else:
                break

        elif town_name == "Oxenfurt":
            job_name = input(f"\n\nWelcome to {town_name}! Any hard worker is welcome here. What kind of job would you be interested in today?\nYou can choose between hunting, farming, juggling and singing: ")

            if job_name not in ("hunting", "farming", "juggling", "singing"):
                print("\nPlease pick one of the available options.\n")
            else:
                break

        elif town_name == "Vengerberg":
            job_name = input(f"\n\nWelcome to {town_name}! Any hard worker is welcome here. What kind of job would you be interested in today?\nYou can choose between hunting, building, killing monsters and singing: ")

            if job_name not in ("hunting", "building", "killing monsters", "singing"):
                print("\nPlease pick one of the available options.\n")
            else:
                break

        elif town_name == "Brugge":
            job_name = input(f"\n\nWelcome to {town_name}! Any hard worker is welcome here. What kind of job would you be interested in today?\nYou can choose between farming, building, killing monsters and juggling: ")

            if job_name not in ("farming", "building", "killing monsters", "juggling"):
                print("\nPlease pick one of the available options.\n")
            else:
                break

        elif town_name == "Hengfors":
            job_name = input(f"\n\nWelcome to {town_name}! Any hard worker is welcome here. What kind of job would you be interested in today?\nYou can choose between hunting, building, killing monsters and singing: ")

            if job_name not in ("hunting", "building", "killing monsters", "singing"):
                print("\nPlease pick one of the available options.\n")
            else:
                break

    do_job(job_name)


##########################################################################
#                                 DO JOB                                 #
##########################################################################


def do_job(job_name):
    print(f"you entered the do_job function with the job '{job_name}'")
    
    gained_gold = 0
    gained_animal_xp = 0
    gained_dex_xp = 0
    gained_entertainment_xp = 0
    
    
    if job_name == "hunting": # add bonus?
        gained_gold = 50
        gained_animal_xp = 6
        gained_dex_xp = 4
    
    elif job_name == "farming ":
        gained_gold = 40
        gained_animal_xp = 7

    elif job_name == "building":
        gained_gold = 40
        gained_dex_xp = 7

    elif job_name == "killing monsters":
        gained_gold = 60
        gained_animal_xp = 4
        gained_dex_xp = 6

    elif job_name == "juggling":
        gained_gold = 25
        gained_dex_xp = 4
        gained_entertainment_xp = 5

    elif job_name == "singing":
        gained_gold = 35
        gained_entertainment_xp = 9

    Character.gain_gold(gained_gold)
    Character.gain_animal_xp(gained_animal_xp)
    Character.gain_dex_xp(gained_dex_xp)
    Character.gain_entertainment_xp(gained_entertainment_xp)
    print("You gained {gained_gold} gold, {gained_animal_xp} animal xp, {gained_dex_xp} dexterity xp and {gained_entertainment_xp} by {job_name}")
    print(Character.mycharacter)
