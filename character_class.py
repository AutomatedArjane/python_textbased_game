##########################################################################
#                            CHARACTER CLASS                             #
##########################################################################

from AllFunctions import *
from character_class import *
from goal_class import *

# create a character with a name and gender. It keeps track of the amount of gold and experience you have, and the mission day 
class Character:

    def __init__ (self, name: str, gender: str, current_quest_day: int, gold: int, animal_xp: int, dex_xp: int, entertainment_xp: int):
        self.name = name
        self.gender = gender
        self.current_quest_day = current_quest_day
        self.gold = gold
        self.animal_xp = animal_xp
        self.dex_xp = dex_xp
        self.entertainment_xp = entertainment_xp

    # print the status of the character
    def __str__(self):
        return f"\n\nYour character's statistics are:\n\nName: {self.name}\nGender: {self.gender}\nDay: {self.current_quest_day}\nGold: {self.gold}\nAnimal xp: {self.animal_xp}\nDexterity xp: {self.dex_xp}\nEntertainment xp: {self.entertainment_xp}\n" # of {mission_days} quest days" --> add this later

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

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
    
    # increase the xp of the character
    def gain_animal_xp(self, animal_xp_increase: int):
        self.animal_xp += animal_xp_increase
        print(f"You received {self.animal_xp} animal xp for your hard work.")

    def gain_dex_xp(self, dex_xp_increase: int):
        self.dex_xp += dex_xp_increase
        print(f"You received {self.dex_xp} dexterity xp for your hard work.")

    def gain_entertainment_xp(self, entertainment_xp_increase: int):
        self.entertainment_xp += entertainment_xp_increase
        print(f"You received {self.entertainment_xp} entertainment xp for your hard work.")
    
    def gain_gold(self, gold_increase: int):
        self.gold += gold_increase
        print(f"You received {self.gold_increase} gold for your work.")