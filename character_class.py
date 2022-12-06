##########################################################################
#                            CHARACTER CLASS                             #
##########################################################################

from AllFunctions import *
from character_class import *
from goal_class import *

# create a character with a name and gender. It keeps track of the amount of gold and experience you have, and the mission day 
class Character:

    def __init__ (self, name: str, gender: str, quest_day: int, gold: int, animal_xp: int, dex_xp: int, entertainment_xp: int, level: int):
        self.name = name
        self.gender = gender
        self.quest_day = quest_day
        self.gold = gold
        self.animal_xp = animal_xp
        self.dex_xp = dex_xp
        self.entertainment_xp = entertainment_xp
        self.level = level

    # print the status of the character
    def __str__(self):
        return f"\n\nYour character's statistics are:\n\nName: {self.name}\nGender: {self.gender}\nDay: {self.quest_day}\nGold: {self.gold}\nAnimal xp: {self.animal_xp}\nDexterity xp: {self.dex_xp}\nEntertainment xp: {self.entertainment_xp}\nLevel: {self.level}" # of {mission_days} quest days" --> add this later

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_quest_day(self):
        return self.quest_day
    
    def get_gold(self):
        return self.gold
    
    def get_animal_xp(self):
        return self.animal_xp
    
    def get_dex_xp(self):
        return self.dex_xp
    
    def get_entertainment_xp(self):
        return self.entertainment_xp
    
    def get_level(self):
        return self.level
    
    
    # increase the xp of the character, and level up if needed
    def gain_animal_xp(self, animal_xp_increase: int):
        self.animal_xp += animal_xp_increase
        if self.animal_xp % 8 == 0: # check if level-up is needed # IS THIS STILL RELEVANT?????? <--------------------^^^*******ÄÄÄÄ
            self.level = round((self.animal_xp + self.dex_xp + self.entertainment_xp) / 8) # level up with the correct amount of levels

    def gain_dex_xp(self, dex_xp_increase: int):
        self.dex_xp += dex_xp_increase
        if self.dex_xp % 8 == 0: # check if level-up is needed
            self.level = round((self.animal_xp + self.dex_xp + self.entertainment_xp) / 8) # level up with the correct amount of levels

    def gain_entertainment_xp(self, entertainment_xp_increase: int):
        self.entertainment_xp += entertainment_xp_increase
        if self.entertainment_xp % 8 == 0: # check if level-up is needed
            self.level = round((self.animal_xp + self.dex_xp + self.entertainment_xp) / 8) # level up with the correct amount of levels                        
