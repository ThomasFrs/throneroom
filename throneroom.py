# Modules
import threading
import time
from os import system, name
import sys
import winsound

version = 1.1
project_starting_date = "26/05/2020"
current_version_release_date = "14/02/2020"

class ThroneRoom():
    def __init__(self, *args):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

        self.verbose = False
        if "-v" in args:
            self.verbose = True

        # Resources
        self.wood = 100
        self.stone = 100
        self.food = 100
        self.money = 0

        # Buildings
        self.sawmill = 1
        self.quarry = 1
        self.crop = 1
        self.soldier = 0
        self.barrack = 0
        self.expansion = 0
        self.buildlimit = 10
        self.woodprod = 1
        self.stoneprod = 1
        self.foodprod = 1

        # War
        self.glory = 0
        self.battle = 0
        self.victory = 0
        self.rank = "Knight"
        self.title = ""
        self.lordname = "Fred"
        self.opponent = 0
        self.requiredsoldier = 0

        if self.verbose:
            self.throneroom()
        else:
            self.menu()

    def run(self):
        while True:
            time.sleep(1)
            self.resource_buildup()

    def throneroom(self):
        self.clear()
        print("\n                               |)))                        |))) \n\
                               |                           | \n\
                           _  _|_  _                   _  _|_  _\n\
                          | |_| |_| |                 | |_| |_| |\n\
                          \  .      /                 \ .    .  /\n\
                           \    ,  /                   \    .  /\n\
                            | .   |_   _   _   _   _   _| ,   |\n\
                            |    .| |_| |_| |_| |_| |_| |  .  |\n\
                            | ,   | .    .     .      . |    .|\n\
                            |   . |  .     . .   .  |   |.    |\n\
                ___----_____| .   |.   ,  _______   |   |   , |---~_____\n\
           _---~            |     |  .   /+++++++\    . | .   |         ~---_\n\
                            |.    | .    |+++++++| .    |   . |              ~-_\n\
                         __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_\n\
                ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__\n\
           -~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~\n\
              _______ _    _ _____   ____  _   _ ______ _____   ____   ____  __  __ \n\
             |__   __| |  | |  __ \ / __ \| \ | |  ____|  __ \ / __ \ / __ \|  \/  |\n\
                | |  | |__| | |__) | |  | |  \| | |__  | |__) | |  | | |  | | \  / |\n\
                | |  |  __  |  _  /| |  | | . ` |  __| |  _  /| |  | | |  | | |\/| |\n\
                | |  | |  | | | \ \| |__| | |\  | |____| | \ \| |__| | |__| | |  | |\n\
                |_|  |_|  |_|_|  \_\(____/|_| \_|______|_|  \_\(____/ \____/|_|  |_|\n\
        ")
        self.start()

    def start(self):
        choice = input("\n1)> PLAY\n2)>> TUTORIAL\n3)> CREDIT\n4)> QUIT\n---> ")
        if choice == "1":
            self.clear()
            self.intro()
        elif choice == "2":
            self.clear()
            self.tutorial()
        elif choice == "3":
            self.clear()
            self.credit()
        elif choice == "4":
            quit()
        else:
            self.throneroom()

    def tutorial(self):
        print(" -- WELCOME TO THE TUTORIAL --")
        print("\n1> Basics:\n\
        - Enter the number of the choice you want\n\
        Ex: 1) Sawmill ---> 1\n\
        - Go back to the Menu by pressing any other Key\n\
        Ex: 1) Sawmill ---> m")
        print("\n2> Production:\n\
        - Gain resources by buying buildings in the Market\n\
        Ex: Menu > Market > Sawmill > Yes\n\
        - See the amount of resources in Stats\n\
        Ex: Menu > Stats\n\
        - Upgrade buildings to boost your production\n\
        Ex: Menu > Market > Upgrade\n\
        - Sell resources to gain money\n\
        Ex: Menu > Market > Sell\n\
        - Watch Out for Error messages!\n\
        Ex: You are short on Wood")
        print("\n3> War:\n\
        -Buy Soldiers with Money\n\
        Ex: Menu > Market > Soldier\n\
        - Your title depends on your Glory Points\n\
        Ex: Knight ---> <50 Glory Points\n\
        - Your Glory Points determine your enemy's strength\n\
        Ex: Wolves ---> <50 Glory Points (5 Soldier Required)")
        gotomainmenu = input("\n> Go to Main menu?\n1) Yes\n2) No\n---> ")
        self.clear()
        self.throneroom()

    def credit(self):
        self.clear()
        print("           -- CREDITS --")
        print("\n-- Throne Room made by ThomasFrs --\n-- Project started on: {} --\n-- Released on: {} --\n-- Version {} --".format(project_starting_date, current_version_release_date, version))
        gotomainmenu = input("\n> Go to Main menu?\n1) Yes\n2) No\n---> ")
        self.clear()
        self.throneroom()

    def intro(self):
        self.clear()
        lord = input("How do we call our saviour?\n---> ")
        self.clear()
        self.lordname = lord

        variable_name = "Your father was a honourable man, he was living and ruling over his realm in a peaceful manner.\nA few years ago, for now trivial reasons, he was slain, leaving his realm split into multiple regions continuously fighting each other to gain more territory whilst its people are desperatly trying to survive through wars and starvation.\nA small group of noblemen and women once close to your father, before his demise, were able to settle in a remote area of the realm with hope to restore this once prosperous monarchy, with your help.\nAs of today, it is time for you to reclaim your throne."
        time.sleep(1)
        words = (char for char in variable_name.split())
        for char in words:
            print(char)
            time.sleep(0.5)
        time.sleep(5)

        self.clear()
        self.menu()

    def menu(self):
        category = int(input("\n     __  __                    \n### |  \/  | ___ __  _ _  _  ###\n### | |\/| |/ -_)| |\|| || | ###\n### |_|  |_|\___||_||_|\_,_| ###\n> Where would you like to go?\n1) Market\n2) War\n3) Stats\n4) Quit\n---> "))
        categories = [self.market, self.war, self.stats, quit]
        if category > 0 and category <= len(categories):
            self.clear()
            categories[category-1]()
        else:
            self.clear()
            self.menu()

    def market(self):
        marketing = int(input("\n     __  __             _         _    \n### |  \/  | __ _  _ _ | |__ ___ | |_  ###\n### | |\/| |/ _` || '_|| / // -_)|  _| ###\n### |_|  |_|\__,_||_|  |_\_\|___| \__| ###\n> What would you like to do?\n|1) Sawmill |4) Soldier   |7) Sell    | \n|2) Quarry  |5) Barrack   |8) Upgrade |\n|3) Crop    |6) Expansion |0) Menu    |\n---> "))
        if marketing == 1:
            self.clear()
            buildsawmill = int(input("\n                          _ _ _ \n    ___ __ ___ __ ___ __ (_) | |\n## (_-</ _` \ V  V / '  \| | | | ##\n## /__/\__,_|\_/\_/|_|_|_|_|_|_| ##\n-----------------------------------\n> Build a Sawmill?(-50 Wood)\n1) Yes\n2) No\n---> "))
            if buildsawmill == 1 and self.wood >= 50 and self.buildlimit >= 1:
                self.wood -= 50
                self.sawmill += 1
                self.buildlimit -= 1
                self.clear()
                self.stats()
            elif buildsawmill == 2:
                self.clear()
                self.menu()
            elif buildsawmill == 1 and self.buildlimit < 1:
                self.maxbuildlimit()
            else:
                print("You are short on Wood!")
                time.sleep(2)
                self.stats()

        elif marketing == 2:
            self.clear()
            buildquarry = int(input("\n      __ _ _   _  __ _ _ __ _ __ _   _ \n##   / _` | | | |/ _` | '__| '__| | | | ##\n##  | (_| | |_| | (_| | |  | |  | |_| | ##\n##   \__, |\__,_|\__,_|_|  |_|   \__, | ##\n--------|_|----------------------|___/----\n> Build a Quarry?(-50 Stone)\n1) Yes\n2) No\n---> "))
            if buildquarry == 1 and self.stone >= 50 and self.buildlimit >= 1:
                self.stone -= 50
                self.quarry += 1
                self.buildlimit -= 1
                self.clear()
                self.stats()
            elif buildquarry == 2:
                self.clear()
                self.menu()
            elif buildquarry == 1 and self.buildlimit < 1:
                self.maxbuildlimit()
            else:
                print("You are short on Stone!")
                time.sleep(2)
                self.stats()

        elif marketing == 3:
            self.clear()
            buildcrop = int(input("\n      ___  _ __  ___   _ __     \n##   / __|| '__|/ _ \ | '_ \  ##\n##  | (__ | |  | (_) || |_) | ##\n##   \___||_|   \___/ | .__/  ##\n----------------------|_|-------\n> Build a Crop?(-25 Wood/Stone)\n1) Yes\n2) No\n---> "))
            if buildcrop == 1 and self.wood >= 25 and self.stone >= 25 and self.buildlimit >= 1:
                self.wood -= 25
                self.stone -= 25
                self.crop += 1
                self.buildlimit -= 1
                self.clear()
                self.stats()
            elif buildcrop == 2:
                self.clear()
                self.menu()
            elif buildcrop == 1 and self.buildlimit < 1:
                self.maxbuildlimit()
            else:
                print("You are short on Wood/Stone!")
                time.sleep(2)
                self.clear()
                self.menu()


        elif marketing == 4:
            self.clear()
            buysoldier = int(input("\n                 _      _  _             \n    ___   ___  | |  __| |(_)  ___  _ __    \n##  / __| / _ \ | | / _` || | / _ \| '__| ##\n##  \__ \| (_) || || (_| || ||  __/| |    ##\n##  |___/ \___/ |_| \__,_||_| \___||_|    ##\n--------------------------------------------\n> Buy Soldier(s)?(-2$/)\n1) Yes\n2) No\n---> "))
            if buysoldier == 1 and self.barrack >= 1:
                amountsoldier = int(input("> How many?\n---> "))
                if self.money >= amountsoldier * 2 and amountsoldier > 0:
                    self.money -= 2 * amountsoldier
                    self.soldier += amountsoldier
                    self.clear()
                    self.stats()
                else:
                    print("You are short on Money!")
                    time.sleep(2)
                    self.stats()
            elif buysoldier == 2:
                self.clear()
                self.menu()
            elif buysoldier == 1 and self.barrack < 1:
                print("You need to build a barrack!")
                time.sleep(2)
                self.clear()
                self.menu()
            else:
                self.clear()
                self.menu()

        elif marketing == 5:
            self.clear()
            buildbarrack = int(input("\n     _                                     _    \n    | |__    __ _  _ __  _ __  __ _   ___ | | __\n##  | '_ \  / _` || '__|| '__|/ _` | / __|| |/ / ##\n##  | |_) || (_| || |   | |  | (_| || (__ |   <  ##\n##  |_.__/  \__,_||_|   |_|   \__,_| \___||_|\_( ##\n---------------------------------------------------\n> Build a Barrack?(-100 Wood)\n1) Yes\n2) No\n---> "))
            if buildbarrack == 1 and self.wood >= 100 and self.barrack < 1 and self.buildlimit >= 1:
                self.wood -= 100
                self.barrack += 1
                self.buildlimit -= 1
                self.clear()
                self.stats()
            elif buildbarrack == 2:
                self.clear()
                self.menu()
            elif buildbarrack == 1 and self.wood < 100:
                print("You are short on Wood!")
                time.sleep(2)
                self.stats()
            elif buildbarrack == 1 and self.barrack >= 1:
                print("You can only build this building once!")
                time.sleep(2)
                self.clear()
                self.menu()
            elif buildbarrack == 1 and self.buildlimit < 1:
                self.maxbuildlimit()
            else:
                self.clear()
                self.menu()

        elif marketing == 6:
            self.clear()
            buildexp = int(input("\n      ___ __  __ _ __    __ _  _ __   ___ (_)  ___   _ __  \n##   / _ )\ \/ /| '_ \  / _` || '_ \ / __|| | / _ \ | '_ \  ##\n##  |  __/ >  < | |_) || (_| || | | |\__ \| || (_) || | | | ##\n##   \___|/_/\_\| .__/  \__,_||_| |_||___/|_| \___/ |_| |_| ##\n----------------|_|-------------------------------------------\n> Build an Expansion?(-100 Wood/Stone)\n1) Yes\n2) No\n---> "))
            if buildexp == 1 and self.wood >= 100 and self.stone >= 100:
                self.wood -= 100
                self.stone -= 100
                self.expansion += 1
                self.buildlimit += 10
                self.clear()
                self.stats()
            elif buildexp == 2:
                self.clear()
                self.menu()
            else:
                print("You are short on Wood/Stone!")
                time.sleep(2)
                self.stats()

        elif marketing ==  7:
            self.clear()
            selling = int(input("\n                _  _ \n    ___   ___ | || |\n##  / __| / _ \| || | ##\n##  \__ \|  __/| || | ##\n##  |___/ \___||_||_| ##\n------------------------\n> What do you want to sell?\n1) Wood\n2) Stone\n0) Menu\n---> "))
            if selling == 1:
                wquantity = int(input("> How much Wood do you want to sell?(1$/10 Wood)\n---> "))
                if wquantity >= 0 and wquantity <= self.wood:
                    self.wood -= wquantity
                    self.money += 0.1 * wquantity
                    self.stats()
                else:
                    print("You are short on Wood!")
                    time.sleep(2)
                    self.stats()

            elif selling == 2:
                squantity = input("> How much Stone do you want to sell?(1$/10 Stone)\n---> ")
                if squantity >= 0 and squantity <= self.stone:
                    self.stone -= 1 * squantity
                    self.money += 0.1 * squantity
                    self.stats()
                else:
                    print("You are short on Stone!")
                    time.sleep(2)
                    self.stats()
            else:
                self.clear()
                self.menu()

        elif marketing == 8:
            self.clear()
            upgrading = int(input("\n     _   _  _ __    __ _  _ __  __ _   __| |  ___ \n##  | | | || '_ \  / _` || '__|/ _` | / _` | / _ ) ##\n##  | |_| || |_) || (_| || |  | (_| || (_| ||  __/ ##\n##   \__,_|| .__/  \__, ||_|   \__,_| \__,_| \___| ##\n-----------|_|-----|___/-----------------------------\n> What do you want to upgrade?\n1) Sawmill\n2) Quarry\n3) Crop\n0) Menu\n---> "))
            if upgrading == 1:
                upgrades = int(input("> Do you want to upgrade your Sawmills?(-1000 Wood)\n1) Yes\n2) No\n---> "))
                if upgrades == 1 and self.wood >= 1000:
                    self.wood -= 1000
                    self.woodprod *= 2
                    self.clear()
                    self.stats()
                    self.menu()
                elif self.wood < 1000:
                    print("You are short on Wood!")
                    time.sleep(2)
                    self.clear()
                    self.stats()
                    self.menu()
                else:
                    self.clear()
                    self.stats()
                    self.menu()

            elif upgrading == 2:
                upgradeq = int(input("> Do you want to upgrade your Quarries?(-1000 Stone)\n1) Yes\n2) No\n---> "))
                if upgradeq == 1 and self.stone >= 1000:
                    self.stone -= 1000
                    self.stoneprod *= 2
                    self.clear()
                    self.stats()
                    self.menu()
                elif self.stone < 1000:
                    print("You are short on Stone!")
                    time.sleep(2)
                    self.clear()
                    self.stats()
                    self.menu()
                else:
                    self.clear()
                    self.stats()
                    self.menu()

            elif upgrading == 3:
                upgradec = int(input("> Do you want to upgrade your Crops?(-1000 Wood/Stone)\n1) Yes\n2) No\n---> "))
                if upgradec == 1 and self.wood >= 1000 and self.stone >= 1000:
                    self.wood -= 1000
                    self.stone -= 1000
                    self.foodprod *= 2
                    self.clear()
                    self.stats()
                    self.menu()
                elif self.wood < 1000 or self.stone < 1000:
                    print("You are short on Wood/Stone!")
                    time.sleep(2)
                    self.clear()
                    self.stats()
                    self.menu()
                else:
                    self.clear()
                    self.stats()
                    self.menu()
            else:
                self.clear()
                self.menu()

        else:
            self.clear()
            self.menu()

    def war(self):
        if self.glory < 50:
            self.rank = "Knight"
            self.title = "Ser"
            self.opponent = "Wolves"
            self.requiredsoldier = 5
        elif self.glory >= 50 and self.glory < 500:
            self.rank = "Baron"
            self.title = "Baron"
            self.opponent = "Peasants"
            self.requiredsoldier = 100
        elif self.glory >= 500 and self.glory < 2000:
            self.rank = "Duke"
            self.title = "Duke"
            self.opponent = "Rebels"
            self.requiredsoldier = 1000
        elif self.glory >= 2000 and self.glory < 2500:
            self.rank = "Prince"
            self.title = "Prince"
            self.opponent = "Lord"
            self.requiredsoldier = 5000
        elif self.glory >= 2500 and self.glory < 10000:
            self.rank = "King"
            self.title = "King"
            self.opponent = "Lord with Dragon"
            self.requiredsoldier = 10000
        elif self.glory >= 10000:
            self.rank = "Emperor"
            self.title = "Emperor"
            self.opponent = "Giant King"
            self.requiredsoldier = 100000
        print("\n    __      __             \n### \ \    / /__ _  _ _  ###\n###  \ \/\/ // _` || '_| ###\n###   \_/\_/ \__,_||_|   ###")
        print("> YOU ARE THE " + self.rank + " " + str(self.lordname) + "!<")
        print("\nYou have " + str(self.glory) + " Glory points")
        print("You have launched " + str(self.battle) + " Battle(s)")
        print("You have won " + str(self.victory) + " Victory")
        print("")
        war = int(input("> Do you want to start a War?\nYou will fight the " + str(self.opponent) + ". \nYou will need " + str(self.requiredsoldier) + " Soldiers.\n1) Yes\n2) No\n---> "))
        if war == 1 and self.soldier == 0:
            print("You need soldiers to fight!")
            time.sleep(2)
            self.clear()
            self.menu()
        elif war == 1 and self.glory < 50 and self.soldier > 0:
            self.clear()
            print("\n   ____                            _   \n  |  _ \  ___  _ __    ___   _ __ | |_ \n# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n# |  _ <|  __/| |_) || (_) || |   | |_  #\n# |_| \_)\___|| .__/  \___/ |_|    \__| #\n--------------|_|-----------------------")
            print("You have started a battle against some wolves")
            if self.soldier >= 5:
                print("You won against the wolves!\nYou have gained 10 Glory points!")
                self.glory += 10
                self.battle += 1
                self.victory += 1
                self.gotomenu()
            else:
                print("You lost and your soldiers were devoured alive...\nA fair treatment!\nFortunately, you didn't lose any Glory point...")
                self.battle += 1
                self.gotomenu()

        elif war == 1 and self.glory >= 50 and self.glory < 500:
            print("\n   ____                            _   \n  |  _ \  ___  _ __    ___   _ __ | |_ \n# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n# |  _ <|  __/| |_) || (_) || |   | |_  #\n# |_| \_)\___|| .__/  \___/ |_|    \__| #\n--------------|_|-----------------------")
            print("You have declared War to some peasants")
            if self.soldier >= 100:
                print("You have defeated these ignorant heretics!\nYou only had " + str(self.soldier * 0.05) + " casualties\nAnd you have gained 25 Glory Points!")
                self.soldier -= self.soldier* 0.05
                self.glory += 25
                self.battle += 1
                self.victory += 1
                self.clear()
                self.menu()
            else:
                print("You lost and your soldiers were slaughtered and were a feast to your starving vassals... \nA fair treatment!\nYou lost 10 Glory point...")
                self.soldier = 0
                self.glory -= 10
                self.battle +=1
                self.clear()
                self.menu()

        elif war == 1 and self.glory >= 500 and self.glory < 2000:
            print("\n   ____                            _   \n  |  _ \  ___  _ __    ___   _ __ | |_ \n# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n# |  _ <|  __/| |_) || (_) || |   | |_  #\n# |_| \_)\___|| .__/  \___/ |_|    \__| #\n--------------|_|-----------------------")
            print("You have started a War against some Rebels")
            if self.soldier >= 1000:
                print("You have defeated these filthy Rebels!\nYou only had " + str(self.soldier * 0.2) + " casualties\nAnd you have gained 50 Glory Points!")
                self.soldier -= self.soldier * 0.2
                self.glory += 50
                self.battle += 1
                self.victory += 1
                self.clear()
                self.menu()
            else:
                print("You lost and your soldiers' corpses were hung by rebels on various buildings for display... \nA fair treatment!\nSadly, you lost 50 Glory points...")
                self.soldier = 0
                self.glory -= 50
                self.battle += 1
                self.gotomenu()

        elif war == 1 and self.glory >= 2000 and self.glory < 2500:
            print("\n   ____                            _   \n  |  _ \  ___  _ __    ___   _ __ | |_ \n# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n# |  _ <|  __/| |_) || (_) || |   | |_  #\n# |_| \_)\___|| .__/  \___/ |_|    \__| #\n--------------|_|-----------------------")
            print("You have started a War against a foreign Lord")
            if self.soldier >= 5000:
                print("You have gloriously defeated him!\nYou only had " + str(self.soldier * 0.3) + " casualties\nAnd you have gained 200 Glory Points!")
                self.soldier -= self.soldier * 0.3
                self.glory += 200
                self.battle += 1
                self.victory += 1
                self.gotomenu()
            else:
                print("You lost and your soldiers were burned alive, their withering skin reflects their combat skills... \nA fair treatment!\nHowever, you lost 200 Glory points...")
                self.soldier = 0
                self.glory -= 200
                self.battle += 1
                self.gotomenu()

        elif war == 1 and self.glory >= 2500 and self.glory < 10000:
            print("\n   ____                            _   \n  |  _ \  ___  _ __    ___   _ __ | |_ \n# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n# |  _ <|  __/| |_) || (_) || |   | |_  #\n# |_| \_)\___|| .__/  \___/ |_|    \__| #\n--------------|_|-----------------------")
            print("You have started a War against a Lord with a Dragon")
            if self.soldier >= 10000:
                print("You have defeated the Lord and his Dragon!\nYou only had " + str(self.soldier * 0.5) + " casualties\nAnd you have gained 1000 Glory Points!")
                self.soldier -= self.soldier * 0.5
                self.glory += 1000
                self.battle += 1
                self.victory += 1
                self.gotomenu()
            else:
                print("You lost and your soldiers were skinned alive, their screams are still echoing through the realm... \nA fair treatment!\nUnfortunately, you lost 1500 Glory points...")
                self.soldier = 0
                self.glory -= 1500
                self.battle += 1
                self.gotomenu()

        elif war == 1 and self.glory >= 10000:
            print("\n   ____                            _   \n  |  _ \  ___  _ __    ___   _ __ | |_ \n# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n# |  _ <|  __/| |_) || (_) || |   | |_  #\n# |_| \_)\___|| .__/  \___/ |_|    \__| #\n--------------|_|-----------------------")
            print("You have started a War against The Giant King")
            time.sleep(2)
            print("You have defeated the Giant King!")
            if self.soldier >= 100000:
                self.soldier -= self.soldier * 0.9
                self.glory += 100000
                self.battle += 1
                self.victory += 1
                time.sleep(2)
                variable_name2= "\nCommander: The War is over! You have managed to bring peace and freedom amongst your people!\nAs you built enough buildings and supplied enough supplies for the many years to come,\nit is finally the time to retire in your cas-...\n" + str(self.title) + " " + str(self.lordname) + ": Indeed, I have provided for my realm, MY realm, when you pathetic simple-minded fools think of me, all you see is a God, bound to his human flesh.\nI am trapped into my mortal self, from now on, I shall  to become the omniscient entity I once had dreamed to become but I had not been granted the potency to achieve my expectations.\nFrom your blood and the blood of my people, my father now dwelling amongst celestial beings shall deem me worthy of my inscribed plight. Now brace yourself for the grim future that is ahead of-\nCommander: *Stabbing " + str(self.title) + " " + str(self.lordname) + "* Rejoin your feeble gods... Now you won't cause any more damage to anyone...\nNow look me in the eyes... It's over..."
                for char in variable_name2:
                    time.sleep(0.1)
                    sys.stdout.write(char)
                time.sleep(2)
                self.clear()
                self.throneroom()
            else:
                print("You Lost and your soldiers were hanged upside-down as an example, their severed heads are either spiked onto our walls or fed to our pigs... \nA fair treatment!\nBecause of them, you lost 10000 Glory points...")
                self.soldier = 0
                self.glory -= 10000
                self.battle += 1
                self.gotomenu()

        else:
            self.clear()
            self.menu()

    def stats(self):
        print("\n     ___  _          _         \n## / __|| |_  __ _ | |_  ___ ###\n### \__ \|  _|/ _` ||  _|(_-< ###\n### |___/ \__|\__,_| \__|/__/ ###\n")

        # Wood
        print("### Wood ### ")
        print("You have " + str(self.wood) + " Wood")
        print("You have " + str(self.sawmill) + " Sawmill(s)")
        print("You produce " + str(self.sawmill * self.woodprod) + " Wood per second")
        print("")

        # Stone
        print("### Stone ### ")
        print("You have " + str(self.stone) + " Stone")
        print("You have " + str(self.quarry) + " Quarry")
        print("You produce " + str(self.quarry * self.stoneprod) + " Stone per second")
        print("")

        # Food
        print("### Food ### ")
        print("You have " + str(self.food) + " Food")
        print("You have " + str(self.crop) + " Crop(s)")
        print("You produce " + str(self.foodprod * 100) + " Food per second")
        print("You can feed " + str((self.crop * self.foodprod) * 100) + " Soldier(s)")
        print("")

        # Money
        print("### Money ### ")
        print("You have " + str(self.money) + " Money")
        print("")

        # Soldier
        print("### Soldier ### ")
        print("You have " + str(self.soldier) + " Soldier(s)")
        print("")

        # Expansion
        print("### Expansion ### ")
        print("You have " + str(self.expansion) + " Expansion(s)")
        print("You can build " + str(self.buildlimit) + " more Building(s)")

        self.gotomenu()

    # Background
    def resource_buildup(self):
        self.wood += (self.woodprod * self.sawmill)
        self.stone += (self.stoneprod * self.quarry)
        self.food += (self.foodprod * self.crop)
        self.food -= (0.01 * self.soldier)

        self.foodcomsuption()

    def foodcomsuption(self):
        if self.food <= int(0) and self.crop > 0:
            self.soldier = self.crop * 100
            self.food = 0
            print("")
            print("You lost many soldiers due to starvation\nBuild more Crops! ")
            time.sleep(2)
            self.stats()
        elif self.food <= int(0) and self.crop <= 0:
            self.soldier = 0
            self.food = 0
            print("")
            print("You lost many soldiers due to starvation\nBuild more Crops! ")
            time.sleep(2)
            self.stats()

    def gotomenu(self):
        gotomenu = input("\n> Go to menu?\nPress enter\n---> ")
        self.clear()
        self.menu()

    def maxbuildlimit(self):
        print("You are out of space!\nBuy an Expansion!")
        time.sleep(2)
        self.stats()

    def clear(self):
        if name == 'nt':
            _ = system('cls')
            print('\n' * 50)


#winsound.PlaySound("BrownFoxInn.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
throneroom = ThroneRoom("-v")