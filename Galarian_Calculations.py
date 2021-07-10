import random
import math
from random import randint
from time import sleep
from L import *
import L
"""

"""
def main():
    rand = random.randint(0, 99)
    print(rand)
    
def stat(Base, EV, IV, Level):
    """Arguments: 
       Base: The base stat of the pokemon
       EV: The EV of the specific stat
       IV: The IV of the specific stat
       Level: The Level of the pokemon"""
    Small = 2 * Base + IV
    SecondSmall = EV/4
    Medium = Small + SecondSmall
    SecondMedium = Medium * Level
    Big = SecondMedium / 100
    Bigsta = Big + 5
    Stat = Bigsta
    return round(Stat)

def hp(Base, EV, IV, Level):
    """Arguments: 
       Base: The base HP of the pokemon
       EV: The EV of HP
       IV: The IV of HP
       Level: The Level of the pokemon"""
    Small = 2 * Base + IV
    SecondSmall = EV/4
    Medium = Small + SecondSmall
    SecondMedium = Medium * Level
    Big = SecondMedium / 100
    Bigsta = Big + Level + 10
    HP = Bigsta
    return round(HP)

def stats(Li, EVs, IVs, Level, increase="None", decrease="None"):
    """Arguments:
       Li: The name of the pokemon
       EVs: A list format for EVs in order of the different stats. i.e. [1, 2, 3, 4, 5, 6]
       IVs: A list format for IVs in order of the different stats. i.e. [1, 2, 3, 4, 5, 6]
       Level: The Level of the pokemon
       increase: The increased stat in index order(i.e. attack is 1)
       decrease: The decreased stat in index order"""
    statistics = []
    HP = hp(Li[0], EVs[0], IVs[0], Level)
    statistics.append(HP)
    for i in range(1, len(Li)):
        stoot = stat(Li[i], EVs[i], IVs[i], Level)
        statistics.append(stoot)
    if increase != "None":
        adding = statistics[increase]
        final = adding * 1.1
        statistics[increase] = round(final)
    if decrease != "None":
        lowering = statistics[decrease]
        final = lowering * 0.9
        statistics[decrease] = round(final)
    stats = ["HP", "A", "D", "SA", "SD", "S"]
    finals = []
    for i in range(len(stats)):
        finals.append(str(statistics[i]) + stats[i])
    print("Finals: ", end="")
    for i in range(len(finals) - 1):
        print(finals[i], end="")
        print(", ", end="")
    print(finals[5])        

def trainer(Level, Li, G="no"):
    """Arguments:
       Level: The Level of the pokemon
       Li: The name of the pokemon
       G: if argument is "yes", the trainer is harder"""
    EV = 0
    result = []
    RN = random.randint(0, 24)
    if RN <= 5:
        increase, decrease = "None", "None"
    else:
        increases = [1, 2, 3, 4, 5]
        increase = random.choice(increases)
        decreases = [1, 2, 3, 4, 5]
        decreases.remove(increase)
        decrease = random.choice(decreases)
    if G == "yes":
        IV = random.randint(22, 31)
    else:
        IV = random.randint(1, 31)
    print("Lv:", Level)
    Base = Li[0]
    HP = hp(Base, EV, IV, Level)
    result.append(HP)
    for i in range(1, len(Li)):
        Base = Li[i]
        if G == "yes":
            IV = random.randint(20, 31)
        else:
            IV = random.randint(1, 31)
        statismo = stat(Base, EV, IV, Level)
        result.append(statismo)
    if increase != "None":
        adding = result[increase]
        final = adding * 1.1
        result[increase] = round(final)
    if decrease != "None":
        lowering = result[decrease]
        final = lowering * 0.9
        result[decrease] = round(final)
    return result

def wild(minLevel, maxLevel, Li):
    """Arguments:
       minLevel: The minimum level of the wild pokemon
       maxLevel: The maximum level of the wild pokemon"""
    EV = 0
    IVs = []
    result = []
    RN = random.randint(0, 24)
    if RN <= 5:
        increase, decrease = "None", "None"
    else:
        increases = [1, 2, 3, 4, 5]
        increase = random.choice(increases)
        decreases = [1, 2, 3, 4, 5]
        decreases.remove(increase)
        decrease = random.choice(decreases)
    IV = random.randint(1, 31)
    IVs.append(IV)
    Level = randint(minLevel, maxLevel)
    print("Lv:", Level)
    Base = Li[0]
    HP = hp(Base, EV, IV, Level)
    result.append(HP)
    for i in range(1, len(Li)):
        Base = Li[i]
        IV = random.randint(1, 31)
        IVs.append(IV)
        statismo = stat(Base, EV, IV, Level)
        result.append(statismo)
    if increase != "None":
        adding = result[increase]
        final = adding * 1.1
        result[increase] = round(final)
    if decrease != "None":
        lowering = result[decrease]
        final = lowering * 0.9
        result[decrease] = round(final)
    rand1 = random.uniform(0, 4096)
    var = ""
    if rand1 <= 1:
        var = "SHINY!!!"
    if var == "SHINY!!!":
        return result, IVs, increase, decrease, var
    return result, IVs, increase, decrease

def xp(WOT, Base, WLevel, KOLevel, num=1):
    """Arguments:
       WOT: Wild or trainer. If a wild, insert 1. If trainer, insert 1.5.
       Base: The xp gain of the pokemon
       WLevel: The winning pokemon level
       KOLevel: The losing pokemon level
       """ 
    topRight1 = 2*KOLevel + 10
    topRight = topRight1**2.5
    bottomRight1 = KOLevel + WLevel + 19
    bottomRight = bottomRight1**2.5
    right = topRight/bottomRight
    topLeft = WOT * Base * KOLevel
    bottomLeft = 5 * num
    left = topLeft/bottomLeft
    boom = right * left
    shabang = boom + 1
    return round(shabang)

def dmg(Level, Power, Attack, Defense, Modifier, critStageProb=0, a=2/2, d=2/2):
    l = [0.04167, 0.125, 0.5, 1, 1]
    oof = l[critStageProb]
    random3 = random.random()
    if random3 < oof:
        if a < 1:
            a = 2/2
        if d > 1:
            d = 2/2
    NewAttack = Attack * a
    NewDefense = Defense * d
    Small = 2 * Level
    SecondSmall = Small/5
    Medium = SecondSmall + 2
    SecondMedium = Medium
    Large = SecondMedium * Power
    secondLarge = NewAttack/NewDefense
    Huge = Large * secondLarge
    random1 = 0.85
    random2 = 1.00
    fullModifier1 = Modifier * random1
    fullModifier2 = Modifier * random2
    Humungo = Huge/50
    Ahh = Humungo + 2
    damage1 = round(Ahh * fullModifier1)
    damage2 = round(Ahh * fullModifier2)
    final = random.randint(damage1, damage2)
    oof = l[critStageProb]
    if random3 < oof:
        final = round(1.5 * final)
        returnmessage = "It was a critical hit!"
        return final, returnmessage
    else:
        return final

def catch(CURRENTHP, MAXHP, rate, ballBonus, status):
    paren = (3 * MAXHP - 2 * CURRENTHP)
    topSection = paren * rate * ballBonus
    bottomSection = 3 * MAXHP
    wholeFraction = topSection/bottomSection
    a = wholeFraction * status
    secondParen = 255/a
    right = secondParen**0.1875
    b = 65536/right
    chance = b
    firstRand = random.uniform(0, 65536)
    if firstRand < chance:
        print("It shook!")
        sleep(1.5)
        secondRand = random.uniform(0, 65536)
        if secondRand < chance:
            print("It shook again!")
            sleep(1.5)
            thirdRand = random.uniform(0, 65536)
            if thirdRand < chance:
                print("Another shake!")
                sleep(1.5)
                fourthRand = random.uniform(0, 65536)
                if fourthRand < chance:
                    print("Gotcha! <Pokemon> was caught!")
                else:
                    print("Gah! It was so close too!")
            else:
                print("Aargh! Almost had it!")
        else:
            print("Awww! It appeared to be caught!")
    else:
        print("Oh no! The pokemon broke free!")
        
def shinyTrials(number, shinyCharm=0):
    counter = 0
    for i in range(number):
        rand = random.uniform(0, 4096)
        if shinyCharm == 1:
            rand = random.uniform(0, 2048)
        if rand <= 1:
            counter += 1
    return counter

def genMaxRaids(badges):
    areas = ("Lake of Outrage", "Hammerlocke Hills", "Giant's Cap", "Dusty Bowl", \
             "Giant's Mirror", "Stony Wilderness", "Bridge Field", "Motostoke Riverbank", \
             "Rolling Fields", "Dappled Grove", "Watchtower Ruins", "East Lake Axewell", \
             "West Lake Axewell", "Axew's Eye", "South Lake Miloch", "Giant's Seat", \
             "North Lake Miloch")
    raid1 = [random.choice(areas)]
    raid2 = [random.choice(areas)]
    raid3 = [random.choice(areas)]
    raid4 = [random.choice(areas)]       
    raid5 = [random.choice(areas)]
    raid6 = [random.choice(areas)]
    raid7 = [random.choice(areas)]
    raid8 = [random.choice(areas)]
    listoraids = [raid1, raid2, raid3, raid4, raid5, raid6, raid7, raid8]
    areaDens = {"Lake of Outrage": ["A", "B", "C", "D"], "Hammerlocke Hills": ["A", "B", "C", "D", "E", "F", "G"], \
                "Giant's Cap": ["A", "B", "C", "D", "E"], "Dusty Bowl": ["A", "B", "C", "D", "E", "F", "G", "H"], \
                "Giant's Mirror": ["A", "B", "C", "D", "E"], "Stony Wilderness": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"], \
                "Bridge Field": ["A", "B", "C", "D", "E", "F", "G", "H", "I"], "Motostoke Riverbank": ["A", "B", "C", "D"], \
                "Rolling Fields": ["A", "B", "C", "D", "E", "F", "G", "H", "I"], "Dappled Grove": ["A", "B", "C", "D", "E"], \
                "Watchtower Ruins": ["A", "C"], "East Lake Axewell": ["A", "B", "C", "D", "E"], \
                "West Lake Axewell": ["A", "B", "C", "D", "E", "F"], "Axew's Eye": ["A"], \
                "South Lake Miloch": ["A", "B", "C", "D", "E"], "Giant's Seat": ["A", "B", "C", "D", "E"], \
                "North Lake Miloch": ["A", "B", "C", "D", "E", "F"]}
    for item in listoraids:
        rand = round(100*random.random(), 4)
        if rand <= 20:
            item.append("Wild Area News")
        else:
            rand2 = round(100*random.random(), 4)
            if rand2 <= 12.5:
                item.append("Rare")
            else:
                item.append("Common")
        denArea = item[0]
        item.append(random.choice(areaDens[denArea]))
    if badges == 0: 
        for item in listoraids:
            item.append("★")
    if badges == 1 or badges == 2:
        for item in listoraids:
            rand = round(100*random.random(), 4)
            if rand > 50:
                item.append("★")
            if rand <= 50:
                item.append("★★") 
    if badges == 3:
        for item in listoraids:
            rand = round(100*random.random(), 4)
            if rand > 66.6666:
                item.append("★★★")
            if rand > 33.3333 and rand <= 66.6666:
                item.append("★★")
            if rand<= 33.3333:
                item.append("★")
    if badges == 4 or badges == 5:
        for item in listoraids:
            rand = round(100*random.random(), 4)
            if rand > 50:
                item.append("★★★")
            if rand <= 50:
                item.append("★★")
    if badges == 6 or badges == 7:
        for item in listoraids:
            rand = round(100*random.random(), 4)
            if rand > 50:
                item.append("★★★★")
            if rand <= 50:
                item.append("★★★")
    if badges == 8:
        for item in listoraids:
            rand = round(100*random.random(), 4)
            if rand > 66.6666:
                item.append("★★★★★")
            if rand > 33.3333 and rand <= 66.6666:
                item.append("★★★★")
            if rand<= 33.3333:
                item.append("★★★")
    return listoraids

def wildWeather(gameStatus):
    """
    gameStatus = "None", "Hammerlocke", ""
    """
    areas = [["Lake of Outrage"], ["Hammerlocke Hills"], ["Giant's Cap"], ["Dusty Bowl"], \
             ["Giant's Mirror"], ["Stony Wilderness"], ["Bridge Field"], ["Motostoke Riverbank"], \
             ["Rolling Fields"], ["Dappled Grove"], ["Watchtower Ruins"], ["East Lake Axewell"], \
             ["West Lake Axewell"], ["Axew's Eye"], ["South Lake Miloch"], ["Giant's Seat"], \
             ["North Lake Miloch"]]
    for item in areas:
        if gameStatus == "None":
            weather = random.choice(["Clear", "Cloudy", "Rain", "Thunderstorm", "Snow", "Harsh Sunlight"])
            item.append(weather)
        if gameStatus == "Hammerlocke":
            weather = random.choice(["Clear", "Cloudy", "Rain", "Thunderstorm", "Snow", "Harsh Sunlight", "Blizzard", "Sandstorm"])
            item.append(weather)
        if gameStatus == "Champion":
            weather = random.choice(["Fog", "Clear", "Cloudy", "Rain", "Thunderstorm", "Snow", "Harsh Sunlight", "Blizzard", "Sandstorm"])
            item.append(weather)
    return areas

def drain(HP):
    return math.ceil(random.uniform(0.01, 0.50) * HP)

#Mini functions
timerBall = lambda turns: min((turns * (1229/4096)) + 1, 4)
bars = lambda a,b: round((100 - ((a / b) * 100))/5)

if __name__ == "__main__":
    main()






