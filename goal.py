from introduction import (
    enter_button
)

import character_growth

##########################################################################
#                                GOAL                                    #
##########################################################################

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
        return f"\n------------------------------------------------------------------------------------------\nThe goal you chose is: {self.goal_name}. You have {self.total_quest_days} days to achieve this goal,\nand in order to do this you will have to collect a sufficient amount of gold, and enough xp of various types. This is what you need:\n\n- {self.gold_goal} gold\n- {self.animal_xp_goal} animal xp\n- {self.dex_xp_goal} dexterity xp\n- {self.entertainment_xp_goal} entertainment xp\n\nGood luck!\n------------------------------------------------------------------------------------------\n"

    def get_goal_name(self):
        return self.goal_name

    def set_goal_name(self, goal_name):
        self.goal_name = goal_name

    def get_total_quest_days(self):
        return self.total_quest_days
    
    def set_total_quest_days(self, total_quest_days):
        self.total_quest_days = total_quest_days

    def get_animal_xp_goal(self):
        return self.get_animal_xp_goal

    def set_animal_xp_goal(self, animal_xp_goal):
        self.animal_xp_goal = animal_xp_goal
    
    def get_dex_xp_goal(self):
        return self.dex_xp_goal        
    
    def set_dex_xp_goal(self, dex_xp_goal):
        self.dex_xp_goal = dex_xp_goal        

    def get_entertainment_xp_goal(self):
        return self.entertainment_xp_goal        

    def set_entertainment_xp_goal(self, entertainment_xp_goal):
        self.entertainment_xp_goal = entertainment_xp_goal

    def get_gold_goal(self):
        return self.gold_goal        

    def set_gold_goal(self, gold_goal):
        self.gold_goal = gold_goal
    
    # after asking the user what goal they want to choose for the game, this method sets the related statistics as the goal of the current game
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
#                              CHOOSE TOWN                               #
##########################################################################

    def choose_travel_destination(self):
        
        while True: # add name and character title
            town_name = input(
                f"\nTo which town would you like to travel today? "
                f"You can choose between Novigrad, Oxenfurt, Vengerberg, Brugge and Hengfors: "
            )

            if town_name not in ("Novigrad", "Oxenfurt", "Vengerberg", "Brugge", "Hengfors"):
                if town_name == "quit":
                    print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                    exit()
                
                else:
                    print("\nPlease pick one of the available options.\n")
                
            else:
                break

        self.choose_job(town_name)

##########################################################################
#                               CHOOSE JOB                               #
##########################################################################

    def choose_job(self, town_name): # OPTIONAL: add bonus xp depending on city and job!
        while True:
            if town_name == "Novigrad": # Add more explanation abouot the city, add name and character title
                job_name = input(f"\n\nBe welcome to {town_name} today! Any hard worker is greeted warmly here. "
                f"What kind of job would you be interested in today?\nYou can choose between farming, killing monsters, "
                f"juggling and singing: ")
                
                if job_name not in ("farming", "killing monsters", "juggling", "singing"):
                    if job_name == "quit":
                        print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                        exit()
                    
                    else:
                        print("\nPlease pick one of the available options.\n")

                else:
                    break

            elif town_name == "Oxenfurt":
                job_name = input(f"\n\nWelcome to {town_name}! We are famous for our university, where you are "
                f"able to study the seven liberal arts.\nMany a famous bard studied here, and it is an excellent "
                f"city to learn the craft. Would you like to practice your craft and juggle\nor sing for us? "
                f"Or would you rather do something else? We have hunting, farming, juggling and singing: ")

                if job_name not in ("hunting", "farming", "juggling", "singing"):
                    if job_name == "quit":
                        print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                        exit()
                    
                    else:
                        print("\nPlease pick one of the available options.\n")
                else:
                    break

            elif town_name == "Vengerberg":
                job_name = input(f"\n\nIn {town_name} you can find mysterious witches and formidable sorcerers. "
                f"Today we need someone more mundane,\nthough we might have monsters roaming around! Are you "
                f"perhaps in need of a job?\nWe have hunting, building, killing monsters and singing available "
                f"for you, which job would you like? ")

                if job_name not in ("hunting", "building", "killing monsters", "singing"):
                    if job_name == "quit":
                        print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                        exit()
                    
                    else:
                        print("\nPlease pick one of the available options.\n")

                else:
                    break

            elif town_name == "Brugge":
                job_name = input(f'\n\n{town_name} is well-known for its beautiful old buildings and it has '
                f'many temples. In this coastal city\nthey speak an unusual form of Nilfgaardian, called '
                f'“West-Vlaams”. We could use someone to help us build more temples,\nthough we also have '
                f'other jobs on offer: farming, building, killing monsters and juggling. Take your pick: ')

                if job_name not in ("farming", "building", "killing monsters", "juggling"):
                    if job_name == "quit":
                        print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                        exit()
                    
                    else:
                        print("\nPlease pick one of the available options.\n")

                else:
                    break

            elif town_name == "Hengfors":
                job_name = input(f"\n\n{town_name} is a Skelliger city, where they mainly speak Rutsi. "
                f"This hard-to-understand language is\nsomewhat related to Nilfgaardian, though it sounds "
                f"very different. If you happen to know any Hengfors sea-shanties,\nbe welcome to sing "
                f"them for us! If you rather do something else, that is also possible.\nYou can choose "
                f"between hunting, building, killing monsters and singing: ")

                if job_name not in ("hunting", "building", "killing monsters", "singing"):
                    if job_name == "quit":
                        print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                        exit()
                    
                    else:
                        print("\nPlease pick one of the available options.\n")
                else:
                    break

        self.do_job(job_name)


##########################################################################
#                                 DO JOB                                 #
##########################################################################


    def do_job(self, job_name):
        print(f'\nyou entered the do_job function with the job "{job_name}"\n')
        
        gained_gold = 0
        gained_animal_xp = 0
        gained_dex_xp = 0
        gained_entertainment_xp = 0
        
        if job_name == "hunting": # add bonus?
            print(f"\n\nHello there, hunter! I heard you were in need of a job. We are in dire need of some food,\n"
            f"so could you perhaps hunt us a couple of rabbits, or a nice fat bird? We would reward you handsomely!")
            print(f"------------------------------------------------------------------------------------------")
            enter_button()
            gained_gold = 50
            gained_animal_xp = 6
            gained_dex_xp = 4
        
        elif job_name == "farming ":
            print(f"\n\nBe welcome to this humble farm! We could use "
            f"your help with the\nharvest today. Of course it goes without saying that you would not work for free!")
            print(f"------------------------------------------------------------------------------------------")
            gained_gold = 40
            gained_animal_xp = 7

        elif job_name == "building":
            print(f"\n\nWe are looking for someone strong that can help us build a new chicken coop.\nWould you "
            f"be able to do that? We would give you more than just some nice fried eggs for lunch!\n"
            f"------------------------------------------------------------------------------------------")
            gained_gold = 40
            gained_dex_xp = 7

        elif job_name == "killing monsters":
            print(f"\n\nPlease help us! More than 10 people have "
            f"vanished already, there must be\na horrible monster hiding in the forest. Are you able to "
            f"kill it for us? All the families involved put money together for a reward.\n"
            f"------------------------------------------------------------------------------------------")
            gained_gold = 60
            gained_animal_xp = 4
            gained_dex_xp = 6

        elif job_name == "juggling":
            print(f"\n\nGood morrow on this good morrow! We are in need of a jester, a juggler who jaunts. "
            f"Please come to our\nperfect party tonight and entertain us. For a good reward of course!"
            f"------------------------------------------------------------------------------------------")
            gained_gold = 25
            gained_dex_xp = 4
            gained_entertainment_xp = 5

        elif job_name == "singing":
            print(f"\n\nAre you perhaps\na singer who claps\nalong\nwith a song\nand sings a lovely tune\n"
            f"in the merry month of june?\n\nWe would like to invite you to sing for us this eve,\nand we "
            f"would pay you even before you leave.\n"
            f"------------------------------------------------------------------------------------------")
            gained_gold = 35
            gained_entertainment_xp = 9

        self.goal.gain_gold(gained_gold)
        character_growth.gain_animal_xp(gained_animal_xp)
        character_growth.gain_dex_xp(gained_dex_xp)
        character_growth.gain_entertainment_xp(gained_entertainment_xp)
        print("gained_gold")
        print(f"You gained {gained_gold} gold, {gained_animal_xp} animal xp, {gained_dex_xp} dexterity xp and {gained_entertainment_xp} by {job_name}. The people you helped are very grateful!")




    ##########################################################################
    #                           TO DO IN THIS FILE                           #
    ##########################################################################

    # Get the goal_reached() function to work
    # Complete the game_won() and game_lost() functions and make sure they work
    # 