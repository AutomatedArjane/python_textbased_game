from introduction import (
    enter_button
)

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
                job_name = input(f"\n\nWelcome to {town_name}, {self.character_title()} {self.name()}! Any hard worker is welcome here. What kind of job would you be interested in today?\nYou can choose between farming, killing monsters, juggling and singing: ")
                
                if job_name not in ("farming", "killing monsters", "juggling", "singing"):
                    if job_name == "quit":
                        print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                        exit()
                    
                    else:
                        print("\nPlease pick one of the available options.\n")

                else:
                    break

            elif town_name == "Oxenfurt":
                job_name = input(f"\n\nWelcome to {town_name}! We are famous for our university, where you are able to study the seven liberal arts.\nMany a famous bard studied here, and it is an excellent city to learn the craft. Would you like to practice your craft and juggle\nor sing for us? Or would you rather do something else? We have hunting, farming, juggling and singing: ")

                if job_name not in ("hunting", "farming", "juggling", "singing"):
                    if job_name == "quit":
                        print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                        exit()
                    
                    else:
                        print("\nPlease pick one of the available options.\n")
                else:
                    break

            elif town_name == "Vengerberg":
                job_name = input(f"\n\nIn {town_name} you can find mysterious witches and formidable sorcerers. Today we need someone more mundane,\nthough we might have monsters roaming around! Are you perhaps in need of a job, {self.character_title()} {self.name()}?\nWe have hunting, building, killing monsters and singing available for you, which job would you like? ")

                if job_name not in ("hunting", "building", "killing monsters", "singing"):
                    if job_name == "quit":
                        print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                        exit()
                    
                    else:
                        print("\nPlease pick one of the available options.\n")

                else:
                    break

            elif town_name == "Brugge":
                job_name = input(f'\n\n {town_name} is well-known for its beautiful old buildings and it has many temples. In this coastal city\nthey speak an unusual form of Nilfgaardian, called “West-Vlaams”. We could use someone to help us build more temples,\nthough we also have other jobs on offer: farming, building, killing monsters and juggling. Take your pick: ')

                if job_name not in ("farming", "building", "killing monsters", "juggling"):
                    if job_name == "quit":
                        print("\nYou have quit the game, thank you for playing. Come back soon to play again!\n")
                        exit()
                    
                    else:
                        print("\nPlease pick one of the available options.\n")

                else:
                    break

            elif town_name == "Hengfors":
                job_name = input(f"\n\n{town_name} is a Skelliger city, where they mainly speak Rutsi. This hard-to-understand language is\nsomewhat related to Nilfgaardian, though it sounds very different. If you happen to know any Hengfors sea-shanties,\nbe welcome to sing them for us! If you rather do something else, that is also possible.\nYou can choose between hunting, building, killing monsters and singing: ")

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
            print(f"\n\nHello there, hunter {self.name()}! I heard you were in need of a job. We are in dire need of some food,\nso could you perhaps hunt us a couple of rabbits, or a nice fat bird? We would reward you handsomely!")
            print(f"------------------------------------------------------------------------------------------")
            enter_button()
            gained_gold = 50
            gained_animal_xp = 6
            gained_dex_xp = 4
        
        elif job_name == "farming ":
            print(f"\n\nBe welcome to this humble farm, {self.character_title()} {self.name()}! We could use your help with the\nharvest today. Of course it goes without saying that you would not work for free!")
            print(f"------------------------------------------------------------------------------------------")
            gained_gold = 40
            gained_animal_xp = 7

        elif job_name == "building":
            print(f"\n\nWe are looking for someone strong that can help us build a new chicken coop.\nWould you be able to do that? We would give you more than just some nice fried eggs for lunch!")
            print(f"------------------------------------------------------------------------------------------")
            gained_gold = 40
            gained_dex_xp = 7

        elif job_name == "killing monsters":
            print(f"\n\nPlease help us, {self.character_title()} {self.name()}! More than 10 people have vanished already, there must be\na horrible monster hiding in the forest. Are you able to kill it for us? All the families involved put money together for a reward.")
            print(f"------------------------------------------------------------------------------------------")
            gained_gold = 60
            gained_animal_xp = 4
            gained_dex_xp = 6

        elif job_name == "juggling":
            print(f"\n\nGood morrow on this good morrow! We are in need of a jester, a juggler who jaunts. Please come to our\nperfect party tonight and entertain us. For a good reward of course!")
            print(f"------------------------------------------------------------------------------------------")
            gained_gold = 25
            gained_dex_xp = 4
            gained_entertainment_xp = 5

        elif job_name == "singing":
            print(f"\n\nAre you perhaps\na singer who claps\nalong\nwith a song\nand sings a lovely tune\nin the merry month of june?\n\nWe would like to invite you to sing for us this eve,\n{self.character_title()} {self.name()}, and we would pay you even before you leave.")
            print(f"------------------------------------------------------------------------------------------")
            gained_gold = 35
            gained_entertainment_xp = 9

        self.gain_gold(gained_gold)
        self.gain_animal_xp(gained_animal_xp)
        self.gain_dex_xp(gained_dex_xp)
        self.gain_entertainment_xp(gained_entertainment_xp)
        print("You gained {gained_gold} gold, {gained_animal_xp} animal xp, {gained_dex_xp} dexterity xp and {gained_entertainment_xp} by {job_name}. The people you helped are very grateful!")
        print(self.character)


    def goal_reached(self, total_quest_days: int, gold_goal: int, animal_xp_goal: int, dex_xp_goal: int, entertainment_xp_goal: int): # get goal values to check against acquired gold and xp

        # check if this method is correct!
        # this method checks if the goal of the current game has been achieved. If yes, it goes to the method "game_won()", otherwise to the method "game_lost()"

        if character.get_current_quest_day() <= total_quest_days:
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

    # Get the goal_reached() function to work
    # Complete the game_won() and game_lost() functions and make sure they work
    # 