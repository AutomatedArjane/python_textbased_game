# all variables, functions and classes needed for the story

##########################################################################
#                            CHARACTER CLASS                             #
##########################################################################

# create a character with a name and gender. It keeps track of the amount of gold and experience you have, and the mission day 
class Character:

    def __init__ (self, name: str, gender: str, char_status: dict):
        self.name = name
        self.gender = gender
        self.char_status = char_status
    
    # print the status of the character
    def __str__(self):
        stats_list = list(self.char_status.values())
        return f"\n\nYour character's statistics are:\n\nName: {self.name}\nGender: {self.gender}\nDay: {stats_list[0]}\nGold: {stats_list[1]}\nXP: {stats_list[2]}\nLevel: {stats_list[3]}" # of {mission_days} quest days" --> add this later

    # increase the xp of the character, and level up if needed
    def gain_animal_xp(self, animal_xp_increase: int):
        self.char_status["animal xp"] += animal_xp_increase
        if self.char_status["animal xp"] % 8 == 0: # check if level-up is needed # IS THIS STILL RELEVANT?????? <--------------------^^^*******ÄÄÄÄ
            self.char_status["level"] = round(self.char_status["animal xp"] / 8) # level up with the correct amount of levels

    def gain_dex_xp(self, dex_xp_increase: int):
        self.char_status["dex xp"] += dex_xp_increase
        if self.char_status["dex xp"] % 8 == 0: # check if level-up is needed
            self.char_status["level"] = round(self.char_status["dex xp"] / 8) # level up with the correct amount of levels

    def gain_entertainment_xp(self, entertainment_xp_increase: int):
        self.char_status["entertainment xp"] += entertainment_xp_increase
        if self.char_status["entertainment xp"] % 8 == 0: # check if level-up is needed
            self.char_status["level"] = round(self.char_status["entertainment xp"] / 8) # level up with the correct amount of levels                        

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
        
    char_status = {"day": 0, "gold": 0, "animal xp": 0, "dex xp": 0, "entertainment xp": 0, "level": 0} # create the statistics of the character

# create a character "mycharacter"
    mycharacter = Character(name, gender, char_status)
    return mycharacter

##########################################################################
#                                GOAL                                    #
##########################################################################

class Goal:

    def __init__(self, goal_name: str,):
        self.goal_name = goal_name
        
    def goal_values(self, goal_name):
        if goal_name == "buy horse":
            animal_xp_goal = 30
            dex_xp_goal = 10
            entertainment_xp_goal = 0
            gold_goal = 300

        elif goal_name == "get own house":
            animal_xp_goal = 0
            dex_xp_goal = 50
            entertainment_xp_goal = 0
            gold_goal = 400

        elif goal_name == "buy lute":
            animal_xp_goal = 0
            dex_xp_goal = 10
            entertainment_xp_goal = 60
            gold_goal = 200
        
        return animal_xp_goal, dex_xp_goal, entertainment_xp_goal, gold_goal

    def goal_reached(self, animal_xp_goal: int, dex_xp_goal: int, entertainment_xp_goal: int, gold_goal: int): # get goal values to check against acquired gold and xp
        if animal_xp_goal >= self.char_status["animal xp"]:
            animal_goal_reached = True
        else:
            animal_goal_reached = False

        if dex_xp_goal >= self.char_status["dex xp"]:
            dex_goal_reached = True
        else:
            dex_goal_reached = False

        if entertainment_xp_goal >= self.char_status["entertainment xp"]:
            entertainment_goal_reached = True
        else:
            entertainment_goal_reached = False

        if gold_goal >= self.char_status["gold"]:
            gold_goal_reached = True

        if animal_goal_reached == True and dex_goal_reached == True and entertainment_goal_reached == True and gold_goal_reached = True:
            game_won()

        else:
            game_lost()