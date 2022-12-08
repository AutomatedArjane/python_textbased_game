# all variables and functions needed for the story

def set_goal_values(self, goal_name):
    if goal_name == "buy horse":
        self.set_total_quest_days(7)
        self.set_gold_goal(300)
        self.set_animal_xp_goal(30)
        self.set_dex_xp_goal(10)
        self.set_entertainment_xp_goal(0)

    elif goal_name == "get own house":
        self.set_total_quest_days(10)
        self.set_gold_goal(400)
        self.set_animal_xp_goal(0)
        self.set_dex_xp_goal(50)
        self.set_entertainment_xp_goal(0)

    elif goal_name == "buy lute":
        self.set_total_quest_days(9)
        self.set_gold_goal(200)
        self.set_animal_xp_goal(0)
        self.set_dex_xp_goal(10)
        self.set_entertainment_xp_goal(60)










##########################################################################
#                           TO DO IN THIS FILE                           #
##########################################################################

# Get Character.gain_gold(gained_gold) (and the other versions) working
# Add more comments to the code
# OPTIONAL: add bonuses to towns and/or jobs
# OPTIONAL: make the program print everything into a text file

# Done:
# Add town descriptions to the choose_town() function to make them more interesting and unique
# Add job descriptions to the do_job() function