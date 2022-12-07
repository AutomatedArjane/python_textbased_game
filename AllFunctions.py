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
    while True:
        goal_name = input('You can choose from three different goals in this game: "buy horse", "get own house" and "buy lute".\nEach goal takes a certain number of days to achieve, and has a set amount of xp and gold you need to collect.\nType the name of the goal you want to choose here: ') # ask the user for their preferred goal
    
        if goal_name not in ("buy horse", "get own house", "buy lute"):
            print("Please pick one of the available options.")

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
    
    while True:
        town_name = input("To which town would you like to travel today? You can choose between Novigrad, Oxenfurt, Vengerberg, Brugge and Hengfors: ")

        if town_name not in ("Novigrad", "Oxenfurt", "Vengerberg", "Brugge", "Hengfors"):
            print("Please pick one of the available options.")
        else:
            break

    choose_job(town_name)

def choose_job(town_name): # OPTIONAL: add bonus xp depending on city and job!
    while True:
        if town_name == "Novigrad": # Add more explanation abouot the city, add name and gender
            job_name = input(f"Welcome to {town_name}! Any hard worker is welcome here. What kind of job would you be interested in today? You can choose between farming, killing monsters, juggling and singing: ")
            
            if job_name not in ("farming", "killing monsters", "juggling", "singing"):
                print("Please pick one of the available options.")
            else:
                break

        elif town_name == "Oxenfurt":
            job_name = input(f"Welcome to {town_name}! Any hard worker is welcome here. What kind of job would you be interested in today? You can choose between hunting, farming, juggling and singing: ")

            if job_name not in ("hunting", "farming", "juggling", "singing"):
                print("Please pick one of the available options.")
            else:
                break

        elif town_name == "Vengerberg":
            job_name = input(f"Welcome to {town_name}! Any hard worker is welcome here. What kind of job would you be interested in today? You can choose between hunting, building, killing monsters and singing: ")

            if job_name not in ("hunting", "building", "killing monsters", "singing"):
                print("Please pick one of the available options.")
            else:
                break

        elif town_name == "Brugge":
            job_name = input(f"Welcome to {town_name}! Any hard worker is welcome here. What kind of job would you be interested in today? You can choose between farming, building, killing monsters and juggling: ")

            if job_name not in ("farming", "building", "killing monsters", "juggling"):
                print("Please pick one of the available options.")
            else:
                break

        elif town_name == "Hengfors":
            job_name = input(f"Welcome to {town_name}! Any hard worker is welcome here. What kind of job would you be interested in today? You can choose between hunting, building, killing monsters and singing: ")

            if job_name not in ("hunting", "building", "killing monsters", "singing"):
                print("Please pick one of the available options.")
            else:
                break

    do_job(job_name)

def do_job(job_name):
    print(f"you entered the do_job function with the job '{job_name}'")
