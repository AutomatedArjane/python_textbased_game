from goal import (
    Goal
)

##########################################################################
#                            CHARACTER CLASS                             #
##########################################################################


# create a character with a name and character title. It keeps track of the amount of gold and experience you have, and the mission day 
class Character:

    def __init__ (self, name: str, character_title: str, current_quest_day: int, gold: int, animal_xp: int, dex_xp: int, entertainment_xp: int):
        self.name = name
        self.character_title = character_title
        self.current_quest_day = current_quest_day
        self.gold = gold
        self.animal_xp = animal_xp
        self.dex_xp = dex_xp
        self.entertainment_xp = entertainment_xp
        self.goal = self.create_goal()

    # print the status of the character
    def __str__(self):
        return f"\nYour character's statistics are:\n\nName: {self.character_title} {self.name}\n\nDay: {self.current_quest_day}\nGold: {self.gold}\n\nAnimal xp: {self.animal_xp}\nDexterity xp: {self.dex_xp}\nEntertainment xp: {self.entertainment_xp}\n\n------------------------------------------------------------------------------------------" # of {mission_days} quest days" --> add this later

    def get_name(self):
        return self.name

    def get_character_title(self):
        return self.character_title

    def get_current_quest_day(self):
        return self.current_quest_day
    
    def get_gold(self):
        return self.gold
    
    def get_animal_xp(self):
        return self.animal_xp
    
    def get_dex_xp(self):
        return self.dex_xp
    
    def get_entertainment_xp(self):
        return self.entertainment_xp

##########################################################################
#                              GOAL SETTING                              #
##########################################################################

    def create_goal(self):

        # ask for the goal name: this will get the data from the chosen goal and set it as the goal for the current game
        while True:
            goal_name = input('You are able to choose between three goals in this game: "buy horse", "get own house" and "buy lute".\nEach goal takes a certain number of days to achieve, and has a set amount of experience points (xp) and gold you need to collect.\n\nType the name of the goal you wish to choose here: ') # ask the user for their preferred goal
        
            if goal_name not in ("buy horse", "get own house", "buy lute"):
                if goal_name == "quit":
                    print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                    exit()
                
                else:
                    print("\nPlease pick one of the available options.\n")
                
            else:
                break

        goal = Goal(goal_name, Goal.get_total_quest_days, Goal.get_animal_xp_goal, Goal.get_dex_xp_goal, Goal.get_entertainment_xp_goal, Goal.get_gold_goal)

        # create a goal "goal"
        goal.set_goal_values(goal_name)

        print(goal)

        return goal

    def increase_gold_xp(): # make this work
        Character.get_gold()

    def goal_reached(self, total_quest_days: int, gold_goal: int, animal_xp_goal: int, dex_xp_goal: int, entertainment_xp_goal: int): # get goal values to check against acquired gold and xp

        # check if this method is correct!
        # this method checks if the goal of the current game has been achieved. If yes, it goes to the method "game_won()", otherwise to the method "game_lost()"
        if Character.character.get_current_quest_day() <= total_quest_days:
            quest_day_success = True

        if animal_xp_goal >= animal_xp: # this is not correct, fix it
            animal_goal_reached = True
        else:
            animal_goal_reached = False

        if dex_xp_goal >= dex_xp:
            dex_goal_reached = True
        else:
            dex_goal_reached = False

        if entertainment_xp_goal >= entertainment_xp:
            entertainment_goal_reached = True
        else:
            entertainment_goal_reached = False

        if gold_goal >= gold:
            gold_goal_reached = True

        if quest_day_success == True and animal_goal_reached == True and dex_goal_reached == True and entertainment_goal_reached == True and gold_goal_reached == True:
            Goal.game_won(character, Goal.goal) # why does this have wriggly lines?

        else:
            pass
            #game_lost()
                
"""     def game_won(character: Character, goal: Goal): # I coded this very fast, check that it works!
        print(f"Congratulations, you achieved your goal: {goal.goal_name}.\n\nYou won on day {character.get_quest_day} of {goal.get_total_quest_days}. You collected:\n- {character.get_gold} of {goal.get_gold} gold\n- {character.get_animal_xp} of {goal.get_animal_xp} gold\n- {character.get_dex_xp} of {goal.get_dex_xp} gold\n- {character.get_entertainment_xp} of {goal.get_entertainment_xp} gold.")


    def game_lost(character: Character, goal: Goal): # I coded this very fast, check that it works!
        print(f"Unfortunately you didn't manage to achieve your goal: buy horse") # continue coding this

        print(f"It is now the last day of your quest, day {goal.get_total_quest_days}. Unfortunately you haven't managed to achieve your goal: {goal.goal_name}.\n\nYou collected:\n- {character.get_gold} of {goal.get_gold} gold\n- {character.get_animal_xp} of {goal.get_animal_xp} gold\n- {character.get_dex_xp} of {goal.get_dex_xp} gold\n- {character.get_entertainment_xp} of {goal.get_entertainment_xp} gold.")
"""

##########################################################################
#                           TO DO IN THIS FILE                           #
##########################################################################

# Get the gain_gold() function and its fellows to work
# 