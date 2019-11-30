# Request input for initial parameters
class character:
    # Character sheet generator
    def __init__(self,race,clss,level,hitDie,hitPoints,strength,dexterity,constitution,intelligence,wisdom,charisma,):
    self.__race = race
    self.__clss = clss
    self.__level = 1
    self.__XP = 0
    self.__isRested = False
    
    # Ability Scores
    self.__strength = strength
    self.__dexterity = dexterity
    self.__constitution = constitution
    self.__intelligence = intelligence
    self.__wisdom = wisdom
    self.__charisma = charisma

    self.__hitDie = 0
    self.__hitPoints = hitPoints




    # Get Methods
    
    def getRace(self) :
        return self.__race
    def getClss(self) :
        return self.__clss
    def getLevel(self) :
        return self.__level
    def getXP(self) :
        return self.__XP
    def getisRested(self) :
        return self.__isRested

    def getStrength(self) :
        return self.__strength
    def getDexterity(self) :
        return self.__dexterity
    def getConstitution(self) :
        return self.__constitution
    def getIntelligence(self) :
        return self.__intelligence
    def getCharisma(self) :
        return self.__charisma

    def getHitDie(self) :
        return self.__hitDie
    def getHitPoints(self) :
        return hitPoints
    
