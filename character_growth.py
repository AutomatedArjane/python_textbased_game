# increase the xp and amount of gold of the character, based on the job they did
def gain_gold(self, gained_gold: int):
    self.gold += gained_gold
    print(f"You received {self.gained_gold} gold for your work.")

def gain_animal_xp(self, gained_animal_xp: int):
    self.animal_xp += gained_animal_xp
    print(f"You received {self.gained_animal_xp} animal xp for your hard work.")

def gain_dex_xp(self, gained_dex_xp: int):
    self.dex_xp += gained_dex_xp
    print(f"You received {self.gained_dex_xp} dexterity xp for your hard work.")

def gain_entertainment_xp(self, gained_entertainment_xp: int):
    self.entertainment_xp += gained_entertainment_xp
    print(f"You received {self.gained_entertainment_xp} entertainment xp for your hard work.")