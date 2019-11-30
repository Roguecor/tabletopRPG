import math
from diceBag import dice
dice = dice()



# Request input for initial parameters
class character:
    # Character sheet generator
    def __init__(self,name,race,clss,hitDie,strength,dexterity,constitution,intelligence,wisdom,charisma):
        self.__name = name
        self.__race = race
        self.__clss = clss
        self.__level = 1 
        self.__XP = 0
        self.__Rested = False
        self.__hitDie = hitDie
        self.__hitPoints = 0
        if self.__clss == "Barbarian" :
            self.__hitPoints = 12
        elif self.__clss == "Fighter" or "Paladin" or "Ranger" :
            self.__hitPoints = 10
        elif self.__clss == "Bard" or "Cleric" or "Druid" or "Monk" or "Rogue" or "Warlock" :
            self.__hitPoints = 8
        elif self.__clss == "Sorcerer" or "Wizard" :
            self.__hitPoints = 6

        # Ability Scores
        # --------------
        self.__strength = strength
        # Strength Modifiers
        if race == "Human" :
            self.__strength = strength + 1
        if race == "Mountain dwarf" or "Dragonborn" or "Half-orc" :
            self.__strength = strength + 2
        self.__dexterity = dexterity
        # Dexterity Modifiers
        if race == "Forest gnome" or "Human" :
            self.__dexterity = dexterity + 1
        if race == "Elf" or "Halfling" :
            self.__dexterity = dexterity + 2
        self.__constitution = constitution
        # Constitution Modifiers
        if race == "Stout halfling" or "Rock gnome" or "Half-orc" or "Human" :
            self.__constitution = constitution + 1
            self.__hitPoints += (math.floor((self.__constitution - 10) / 2))
        if race == "Dwarf" :
            self.__constitution = constitution + 2
            self.__hitPoints += (math.floor((self.__constitution - 10) / 2))
        self.__intelligence = intelligence
        # Intelligence Modifiers
        if race == "High elf" or "Tiefling" or "Human" :
            self.__intelligence = intelligence + 1
        if race == "Gnome" :
            self.__intelligence = intelligence + 2
        self.__wisdom = wisdom
        # Wisdom Modifiers
        if race == "Hill dwarf" or "Human" or "Wood elf" :
            self.__wisdom = wisdom + 1
        self.__charisma = charisma
        # Charisma Modifiers
        if race == "Drow" or "Lightfoot halfling" or "Dragonborn" or "Human" :
            self.__charisma = charisma + 1
        if race == "Half-elf" or "Tiefling" :
            self.__charisma = charisma + 2
    
    
    ###############METHODS###################
    

    # is Methods
    def isRested(self) :
        self.__Rested = True
    def isNotRested(self) :
        self.__Rested = False

    # get Methods

    def getName(self) :
        return self.__name
    def getRace(self) :
        return self.__race
    def getClss(self) :
        return self.__clss
    def getLevel(self) :
        return self.__level
    def getXP(self) :
        return self.__XP
    def getRested(self) :
        return self.__Rested
    def getHitDie(self) :
        return self.__hitDie
    def getHitPoints(self) :
        return self.__hitPoints
    

    def getStrength(self) :
        return self.__strength
    def getDexterity(self) :
        return self.__dexterity
    def getConstitution(self) :
        return self.__constitution
    def getIntelligence(self) :
        return self.__intelligence
    def getWisdom(self) :
        return self.__wisdom
    def getCharisma(self) :
        return self.__charisma

    # Show Methods
    def showAbilityScores(self) :
        print("-------------------")
        print(self.getName()," LVL",self.getLevel(), "", self.getClss())
        print("STR: ",self.getStrength())
        print("DEX: ",self.getDexterity())
        print("CON: ",self.getConstitution())
        print("INT: ",self.getIntelligence())
        print("WIS: ",self.getWisdom())
        print("CHR: ",self.getCharisma())
        print("")
        print("HP : ",self.getHitPoints())



        


def main() :
    strength,dexterity,constitution,intelligence,wisdom,charisma = 15,10,14,8,13,12
    testCharacter = character("Cicero","Dwarf","Fighter",0,strength,dexterity,constitution,intelligence,wisdom,charisma)

    testCharacter.showAbilityScores()

    print(testCharacter.getRested())
    
main()
