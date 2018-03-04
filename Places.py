import time
from Animates import Player

class Place:
    
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class MiiRecoverii(Place):

    def __init__(self, name):
        super().__init__(name)

    def onVisit(self, player):
        while True:
            heal = input("Welcome to MiiRecoverii! Would you like to be healed? (Y/N)").upper()
            if heal == "Y":
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1...Aaaaand voila! You have been healed")
                player.hitPoints = player.getFullHitPoints()
                print("Your health is now " + str(player.getFullHitPoints()))
                break
            elif heal == "N":
                print("See you soon then!")
                break
            else:
                print("I'm sorry... I don't understand you...")
