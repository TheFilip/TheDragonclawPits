from multiprocessing.pool import ThreadPool
import random, math, time
#import quickPlaying
#The Dragonclaw Pits \240923/

randomMode = 0 # 0 - User Inputs | 1 - Completely Random | 2 - Selective Random

sRandChoice = 4 #2-HP 3-ATK 4-SPD 5-POTIONS

global targetFloor
targetFloor = 5
targetFloorChange = 2





maxDiceRolls = 12
dice=maxDiceRolls/2

#STARTING INTEGERS
global coins
coins = 1 #Maybe add to Character class later?
potionCount = 0

healthCost = 1
damageCost = 1
speedCost = 1
potionCost = 20


potionHeal = 5
potionHealBoost = 1



coinLoss = 2



damageMod = 0
speedMod = 0

def damage(character):
    basicDamageCalc(character.lowRange,character.highRange)
    character.damageDealt = character.damageMod+basicDamage
    print(character.damageDealt)

def basicDamageCalc(low,high):
    global basicDamage
    basicDamage = random.randint(low,high)

def speedCheck(character):
    basicSpeedCalc()
    character.speed = character.speedMod+basicSpeed
    print(character.speed)

def basicSpeedCalc():
    global basicSpeed
    basicSpeed = random.randint(1,maxDiceRolls)


def potionHealCalc():
    global potionHeal
    potionHeal = (random.randint(0,dice))+1



class character_:
    def __init__(self,name,health,damageMod,speedMod,lowRange,highRange):
        self.name = name
        self.health = health
        self.damageMod = damageMod
        self.speedMod = speedMod
        self.lowRange = lowRange
        self.highRange = highRange

        self.basicDamage = random.randint(lowRange,highRange) + self.damageMod
        self.basicSpeed = random.randint(1,maxDiceRolls) + self.speedMod










global hp1
global hp2
global victory
victory = False

def fight(name1,name2,hp1,bonus1_1,bonus1_2,hp2,bonus2_1,bonus2_2):
    global tHP
    #hp1 = tempHealth
    #print(name1, name2)
    #global hp1
    #global winner
    #global hp2
    while hp2 != 0 and hp1 > 0:
        if hp1 < 0:
            #hp2 = 0
            print("Health Lost")
            tHP=hp1

            break
        diceRoll1 = random.randint(1,dice)+random.randint(1,dice)+bonus1_1
        diceRoll2 = random.randint(1,dice)+random.randint(1,dice)+bonus2_1


        while diceRoll1 == diceRoll2:
            diceRoll2 = random.randint(1,dice)+random.randint(1,dice)+bonus2_1

        print("Speed Check")
        print(name1,"-",diceRoll1)
        print(name2,"-",diceRoll2)
        
        #choice = input()
        #if choice == ",":
            #hp1 +=1
        #if  choice == ".":
            #hp2 +=1

        print (name1,"-",hp1)
        print (name2,"-",hp2)
        diceRoll3 = random.randint(1,dice)+random.randint(1,dice)+bonus1_2
        diceRoll4 = random.randint(1,dice)+random.randint(1,dice)+bonus2_2
        while diceRoll3 == diceRoll4:
            diceRoll4 = random.randint(1,dice)+random.randint(1,dice)+bonus2_2

        print("Attack Check")
        print(name1,"-",diceRoll3)
        print(name2,"-",diceRoll4)

        if diceRoll1 > diceRoll2:
            if diceRoll3 > diceRoll4:
                hp2-=1
        else:
            if diceRoll3 < diceRoll4:
                hp1-=1

        print (name1,"-",hp1)
        print (name2,"-",hp2)
        #tempHealth = hp1
        tHP=hp1
    #else:
        #print("Health Lost")
        #location = "Town"
















p1= character_("Player",10,0,0,1,2)



#locations - Town | Dungeon | Floor1 etc.

location = "Town"
coinGain = 0
difficulty = 2
dungeonFloor = 0







def shop():
    print("shop")






def Town():
    global townVisits
    townVisits += 1
    print ("Town Visits:",townVisits)
    global coins
    global healthCost
    global damageCost
    global speedCost
    global potionCost
    global potionCount

    #Give player choice of either going into the dungeon or upgrading stats
    print("1 Dungeon\n2 +1 Max Health - ",healthCost,"\n3 +1 Damage Roll - ",damageCost,"\n4 +1 Speed Roll - ",speedCost,"\n5 Potion - ",potionCost)









    choice = 0

    if randomMode == 0:
        choice = int(input(">>"))

    if randomMode == 1:
        choice = random.randint(1,5) #################################################################


    if randomMode == 2:
        randNum = random.randint(1,2)
        if randNum == 1:
            choice = 1
        if randNum == 2:
            choice = sRandChoice







    
    if choice == 1:
        global location
        victory = True
        location = "Dungeon"

    elif choice == 2:
        if coins < healthCost:
            print("Not enough coins")
        else:
            coins -= healthCost
            healthCost+=1
            p1.health+=1

    elif choice == 3:
        if coins < damageCost:
            print("Not enough coins")
        else:
            coins -= damageCost
            damageCost += 1
            p1.damageMod+=1

    elif choice == 4:
        if coins < speedCost:
            print("Not enough coins")
        else:
            coins -= speedCost
            speedCost += 1
            p1.speedMod+=1
    
    elif choice == 5:
        if coins < potionCost:
            print("Not enough coins")
        else:
            coins -= potionCost
            potionCost = math.floor(potionCost*1.5)
            potionCount=1



def dungeoningDown():
    global tempHealth
    global tempEnemyAmount
    global dungeonFloor
    global tempCoins
    global victory
    dungeonFloor += 1
    #coinGain = 1
    tempEnemyAmount = difficulty*dungeonFloor
    while tempEnemyAmount > 0:
        while tempHealth > 0:
            fighting()
            tempHealth = tHP
            tempEnemyAmount -= 1
            print("Floor Enemies - ",tempEnemyAmount)
            if tempEnemyAmount <= 0:
                break
            print("TEMP HP - ",tempHealth)


        if tempHealth > 0:
            print("Floor",dungeonFloor,"Complete")
            tempCoins += dungeonFloor*coinGain
            victory = True
            break
        if tempHealth <=0:
            print("Dungeon Lost")
            victory = False
            tempCoins = math.floor(tempCoins/coinLoss)
            break


            #not looping, not saving temp health



#WORKING on this, need to have a fight in place
def FloorDown():
    global tempDamageMod
    global tempSpeedMod
    global tempHealth
    global victory
    global dungeonFloor
    global location
    global tempCoins
    global coins
    global targetFloor
    global potionCount
    global coinGain
    tempHealth = p1.health
    tempDamageMod = p1.damageMod
    tempSpeedMod = p1.speedMod
    tempCoins = 0
    coinGain = 1
    #tempEnemyAmount = difficulty*(dungeonFloor+1)
    dungeonFloor = 0
    victory = False
    print("Dungeon")
    if dungeonFloor == 0:
        dungeoningDown()
    while victory == True:
        print("Hp -",tempHealth)






        ################################################################## BOSS FLOOR HERE
        if dungeonFloor == targetFloor:
            #fight(BOSS FIGHT)
            #global dungeonFloor
            global difficulty
            global potionHealBoost
            #global targetFloor
            #global coinGain

            difficulty += 1
            #if dungeonFloor > targetFloor:
            coinGain=math.floor(coinGain*(difficulty/2))
            targetFloor += math.floor(targetFloor*targetFloorChange)
            potionHealBoost += 1
            print("Victory!!")
            print("|",p1.name,"| hp -",p1.health,"| $ -",coins,"| dmg/def -",p1.damageMod,"| spd -",p1.speedMod,"|","| pot -",potionCount,"|")
            print(townVisits)
            input()








        print("---------------")
        print("1 Continue\n2 Potion-",potionCount,"\n3 Back To Town")






        dungeonChoice = 0


        if randomMode == 0:
            dungeonChoice = int(input(">>"))




        if randomMode == 1 or randomMode == 2:
            dungeonChoice = random.randint(1,3) #################################################################










        if dungeonChoice == 1:
            dungeoningDown()
        if dungeonChoice == 2:
            if potionCount > 0:
                potionCount -= 1
                potionHealCalc()
                tempHealth += potionHeal*potionHealBoost
                if tempHealth > p1.health:
                    tempHealth = p1.health
            else:
                print("Not enough potions")
        if dungeonChoice == 3:
            victory = False
            location = "Town"
            coins += tempCoins
            tempCoins = 0
            break
    if victory == False:
        location = "Town"
        coins += tempCoins
        #coins += dungeonFloor


    #CONTINUE DOWN OR GO BACK TO TOWN
    
    








def fighting():
    e1 = character_("Enemy",random.randint(1,dungeonFloor+1),random.randint(0,dungeonFloor),random.randint(0,dungeonFloor),1,random.randint(1,dungeonFloor+1))
    global tempHealth


    if dungeonFloor == targetFloor:
        fight(p1.name,e1.name,tempHealth,p1.damageMod,p1.speedMod,e1.health,e1.damageMod,e1.speedMod)
            #fight(BOSS FIGHT)
            #global dungeonFloor
        #    global difficulty
        #    global tempEnemyAmount
        #    tempEnemyAmount = 1
        #   bossName = ("Big Boss",dungeonFloor)
        #    boss1 = character_(bossName,random.randint(dungeonFloor,dungeonFloor*(difficulty/2)),dungeonFloor,dungeonFloor,dungeonFloor,random.randint(dungeonFloor,(dungeonFloor*(difficulty/2))))
        #    fight(p1.name,boss1.name,tempHealth,p1.damageMod,p1.speedMod,boss1.health,boss1.damageMod,boss1.speedMod)

    if dungeonFloor != targetFloor:
        fight(p1.name,e1.name,tempHealth,p1.damageMod,p1.speedMod,e1.health,e1.damageMod,e1.speedMod)

    #print("fight happens")
    #tempHealth = hp1







townVisits = 0

#damage(p1)
def _main_():


    print("|",p1.name,"| hp -",p1.health,"| $ -",coins,"| dmg/def -",p1.damageMod,"| spd -",p1.speedMod,"|","| pot -",potionCount,"|")
    
    #Check where the player is - Town or in dungeon
    if location == "Town" and victory == False:
        Town()
    if location == "Dungeon":
        FloorDown()








while True:
    _main_()
print("End")