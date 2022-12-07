##########################################################################
#                                GOAL                                    #
##########################################################################

from AllFunctions import *
from character_class import *
from goal_class import *

# create a goal for the game. Each game has subgoals consisting of the amount of gold and xp you need to collect
class Goal:
    
    def __init__(self, goal_name: str, total_quest_days: int, gold_goal: int, animal_xp_goal: int, dex_xp_goal: int, entertainment_xp_goal: int):
        self.goal_name = goal_name
        self.total_quest_days = total_quest_days
        self.gold_goal = gold_goal
        self.animal_xp_goal = animal_xp_goal
        self.dex_xp_goal = dex_xp_goal
        self.entertainment_xp_goal = entertainment_xp_goal


    # print the goal that is chosen
    def __str__(self):
        return f"\nThe goal you chose is: {self.goal_name}.\nYou have {self.total_quest_days} days to achieve this goal,\nand to do this you will have to collect enough gold, and enough xp of various types. This is what you need:\n\n- {self.gold_goal} gold\n- {self.animal_xp_goal} animal xp\n- {self.dex_xp_goal} dexterity xp\n- {self.entertainment_xp_goal} entertainment xp.\n\nGood luck!\n"

    def get_goal_name(self):
        return self.goal_name

    def set_goal_name(self):
        return self.goal_name

    def get_total_quest_days(self):
        return self.total_quest_days
    
    def set_total_quest_days(self):
        return self.total_quest_days

    def get_animal_xp_goal(self):
        return self.get_animal_xp_goal

    def set_animal_xp_goal(self):
        return self.get_animal_xp_goal
    
    def get_dex_xp_goal(self):
        return self.dex_xp_goal        
    
    def set_dex_xp_goal(self):
        return self.dex_xp_goal        

    def get_entertainment_xp_goal(self):
        return self.entertainment_xp_goal        

    def set_entertainment_xp_goal(self):
        return self.entertainment_xp_goal        

    def get_gold_goal(self):
        return self.gold_goal        

    def set_gold_goal(self):
        return self.gold_goal        

    
    # after asking the user what goal they want to choose for the game, this method sets the related statistics as the goal of the current game
    def goal_values(self, goal_name):
        if goal_name == "buy horse":
            total_quest_days = 7
            animal_xp_goal = 30
            dex_xp_goal = 10
            entertainment_xp_goal = 0
            gold_goal = 300

        elif goal_name == "get own house":
            total_quest_days = 10
            animal_xp_goal = 0
            dex_xp_goal = 50
            entertainment_xp_goal = 0
            gold_goal = 400

        elif goal_name == "buy lute":
            total_quest_days = 9
            animal_xp_goal = 0
            dex_xp_goal = 10
            entertainment_xp_goal = 60
            gold_goal = 200
        
        return total_quest_days, animal_xp_goal, dex_xp_goal, entertainment_xp_goal, gold_goal

    def goal_reached(self, total_quest_days: int, animal_xp_goal: int, dex_xp_goal: int, entertainment_xp_goal: int, gold_goal: int): # get goal values to check against acquired gold and xp

        # check if this method is correct!
        # this method checks if the goal of the current game has been achieved. If yes, it goes to the method "game_won()", otherwise to the method "game_lost()"

        if current_quest_day <= total_quest_days:
            quest_day_success = True

        if animal_xp_goal >= self.char_status["Animal xp"]: # this is not correct, fix it
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

        if quest_day_success == True and animal_goal_reached == True and dex_goal_reached == True and entertainment_goal_reached == True and gold_goal_reached == True:
            Goal.game_won(mycharacter, Goal.mygoal) # why does this have wriggly lines?

        else:
            pass
            #game_lost()
            
"""     def game_won(mycharacter: Character, mygoal: Goal): # I coded this very fast, check that it works!
        print(f"Congratulations, you achieved your goal: {mygoal.goal_name}.\n\nYou won on day {mycharacter.get_quest_day} of {mygoal.get_total_quest_days}. You collected:\n- {mycharacter.get_gold} of {mygoal.get_gold} gold\n- {mycharacter.get_animal_xp} of {mygoal.get_animal_xp} gold\n- {mycharacter.get_dex_xp} of {mygoal.get_dex_xp} gold\n- {mycharacter.get_entertainment_xp} of {mygoal.get_entertainment_xp} gold.")


    def game_lost(mycharacter: Character, mygoal: Goal): # I coded this very fast, check that it works!
        print(f"Unfortunately you didn't manage to achieve your goal: buy horse") # continue coding this

        print(f"It is now the last day of your quest, day {mygoal.get_total_quest_days}. Unfortunately you haven't managed to achieve your goal: {mygoal.goal_name}.\n\nYou collected:\n- {mycharacter.get_gold} of {mygoal.get_gold} gold\n- {mycharacter.get_animal_xp} of {mygoal.get_animal_xp} gold\n- {mycharacter.get_dex_xp} of {mygoal.get_dex_xp} gold\n- {mycharacter.get_entertainment_xp} of {mygoal.get_entertainment_xp} gold.")
 """