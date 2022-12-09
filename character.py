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

    def set_current_quest_day(self, current_quest_day):
        self.current_quest_day += current_quest_day
    
    # get and set the gold your character has
    #def get_gold(self):
     #   return self.gold

    #def set_gold(self, gold):
        #self.gold = gold

    # get and set the gold goal
    def get_gold_goal(self):
        return self.gold_goal        

    def set_gold_goal(self, gold_goal):
        self.gold_goal = gold_goal

    # get and set the amount of gained gold
    def get_gained_gold(self):
        return self.gold

    def set_gained_gold(self, gained_gold):
        self.gold += gained_gold

    # get and set the animal xp your character has   
    def get_animal_xp(self):
        return self.animal_xp

    def set_animal_xp(self, animal_xp):
        self.animal_xp = animal_xp    

    # get and set the animal xp goal
    def get_animal_xp_goal(self):
        return self.get_animal_xp_goal

    def set_animal_xp_goal(self, animal_xp_goal):
        self.animal_xp_goal = animal_xp_goal

    # get and set the amount of gained animal xp
    def get_gained_animal_xp(self):
        return self.animal_xp

    def set_gained_animal_xp(self, gained_animal_xp):
        self.animal_xp += gained_animal_xp    
    
    # get and set the dex xp your character has    
    def get_dex_xp(self):
        return self.dex_xp

    def set_dex_xp(self, dex_xp):
        self.dex_xp = dex_xp 

    # get and set the dex xp goal
    def get_dex_xp_goal(self):
        return self.dex_xp_goal        
    
    def set_dex_xp_goal(self, dex_xp_goal):
        self.dex_xp_goal = dex_xp_goal        

    # get and set the amount of gained dex xp
    def get_gained_dex_xp(self):
        return self.dex_xp

    def set_gained_dex_xp(self, gained_dex_xp):
        self.dex_xp += gained_dex_xp 

    # get and set the entertainment xp your character has
    def get_entertainment_xp(self):
        return self.entertainment_xp

    def set_entertainment_xp(self, entertainment_xp):
        self.entertainment_xp = entertainment_xp     

    # get and set the entertainment xp goal
    def get_entertainment_xp_goal(self):
        return self.entertainment_xp_goal        

    def set_entertainment_xp_goal(self, entertainment_xp_goal):
        self.entertainment_xp_goal = entertainment_xp_goal

    # get and set the amount of gained entertainment xp
    def get_gained_entertainment_xp(self):
        return self.entertainment_xp

    def set_gained_entertainment_xp(self, gained_entertainment_xp):
        self.entertainment_xp += gained_entertainment_xp   

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

        # create a goal "goal"
        goal = Goal(goal_name, Goal.get_total_quest_days, Goal.get_gold_goal, Goal.get_animal_xp_goal, Goal.get_dex_xp_goal, Goal.get_entertainment_xp_goal, Goal.get_job_name)

        goal.set_goal_values(goal_name)

        print(goal)

        return goal

    # increase the amount of gold and xp the character has. >>>>> UPDATE this according to new idea    
    def increase_gold_and_xp(self):
        gained_gold = self.get_gained_gold()
        self.set_gained_gold(gained_gold)

        gained_animal_xp = self.get_gained_animal_xp()
        self.set_gained_animal_xp(gained_animal_xp)

        gained_dex_xp = self.get_gained_dex_xp()
        self.set_gained_dex_xp(gained_dex_xp)

        gained_entertainment_xp = self.get_gained_entertainment_xp()
        self.set_gained_entertainment_xp(gained_entertainment_xp)

        print(f"You gained {gained_gold} gold, {gained_animal_xp} animal xp, {gained_dex_xp} dexterity xp and {gained_entertainment_xp} entertainment "
        f"xp by {self.goal.get_job_name()}. The people you helped are very grateful!")

    # check after the last quest day if the character has achieved the goal
    def goal_reached(self): # gold_goal: int, animal_xp_goal: int, dex_xp_goal: int, entertainment_xp_goal: int >>> get goal values to check against acquired gold and xp

        # this method checks if the goal of the current game has been achieved. If yes, it goes to the method "game_won()", otherwise to the method "game_lost()"
        if self.get_gold_goal() >= self.get_gold():
            gold_goal_reached = True
        else:
            gold_goal_reached = False

        if self.get_animal_xp_goal() >= self.get_animal_xp(): # this is not correct, fix it
            animal_goal_reached = True
        else:
            animal_goal_reached = False

        if self.get_dex_xp_goal() >= self.get_dex_xp():
            dex_goal_reached = True
        else:
            dex_goal_reached = False

        if self.get_entertainment_xp_goal() >= self.get_entertainment_xp():
            entertainment_goal_reached = True
        else:
            entertainment_goal_reached = False

        if  gold_goal_reached == True and animal_goal_reached == True and dex_goal_reached == True and entertainment_goal_reached == True:
            print(f'Congratulations, you achieved your goal: "{self.goal.goal_name}"\n\n')

        else:
            print(f'I am sorry, you did not manage to achieve your goal: "{self.goal.goal_name}." '
            f'Feel free to try again any time! You are always welcome again.\n\n')
        
        (f'You gained:\n- {self.get_gold_goal()} of {self.get_gold()} gold\n'
        f'- {self.get_animal_xp_goal()} of {self.get_animal_xp()} animal xp\n'
        f'- {self.get_dex_xp_goal()} of {self.get_dex_xp()} dexterity xp\n'
        f'- {self.get_entertainment_xp_goal()} of {self.get_entertainment_xp()} animal xp\n\n'
        f'Thank you for playing! Come back soon to play again in the wonderful world of Woianzii')
            
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