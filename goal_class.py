##########################################################################
#                                GOAL                                    #
##########################################################################

from AllFunctions import *
from character_class import *
from goal_class import *

class Goal:
    
    def __init__(self, goal_name: str, no_of_quest_days: int, animal_xp_goal: int, dex_xp_goal: int, entertainment_xp_goal: int, gold_goal: int):
        self.no_of_quest_days = no_of_quest_days
        self.goal_name = goal_name
        self.animal_xp_goal = animal_xp_goal
        self.dex_xp_goal = dex_xp_goal
        self.entertainment_xp_goal = entertainment_xp_goal
        self.gold_goal = gold_goal

    def __str__(self): # fill this in!!!
        pass

    def get_goal_name(self):
        return self.goal_name

    def get_no_of_quest_days(self):
        return self.no_of_quest_days
    
    def get_animal_xp_goal(self):
        return self.get_animal_xp_goal
    
    def get_dex_xp_goal(self):
        return self.get_dex_xp_goal        

    def get_entertainment_xp_goal(self):
        return self.get_entertainment_xp_goal        

    def get_gold_xp_goal(self):
        return self.get_gold_xp_goal        
    
    # after asking the user what goal they want to choose for the game, this method sets the related statistics as the goal of the current game
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

        # check if this method is correct!
        # this method checks if the goal of the current game has been achieved. If yes, it goes to the method "game_won()", otherwise to the method "game_lost()"
         
        if animal_xp_goal >= self.char_status["Animal xp"]:
            animal_goal_reached = True
        else:
            animal_goal_reached = False

        if dex_xp_goal >= self.char_status["Dex xp"]:
            dex_goal_reached = True
        else:
            dex_goal_reached = False

        if entertainment_xp_goal >= self.char_status["Entertainment xp"]:
            entertainment_goal_reached = True
        else:
            entertainment_goal_reached = False

        if gold_goal >= self.char_status["Gold"]:
            gold_goal_reached = True

        if animal_goal_reached == True and dex_goal_reached == True and entertainment_goal_reached == True and gold_goal_reached == True:
            game_won(mycharacter)

        else:
            pass
            #game_lost()
