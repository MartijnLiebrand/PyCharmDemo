#Hoe werken functies in python?

#Debuggen, hoe werkt dat?
#corrupt_data = [1,4,5,33,5,22,44,"A",11,222,134,3,1,1,3]

data = [1,4,5,33,5,22,"a",34,11,222,134,3,1,1,3]

def gemiddelde(lijst):
    totaal = 0
    for gegeven in lijst:
        totaal += gegeven
    result = (totaal / len(lijst))
    return result


gemiddelde(data)























def min(lijst):
    return sorted(lijst)[0]

def max(lijst):
    return sorted(lijst)[len(lijst)]

def mediaan(lijst):
    if lijst % 2 != 0:
        return lijst[round(len(lijst)/2)]+lijst[round(len(lijst)/2-1)]/2
    return lijst[round(len(lijst)/2)]


#for x in data:
    #print(x)



#probeer eens:
#middelste waarde / mediaan
#retourneer de hoogste waarde
#retoutrneer de laagste waarde
#filter lijst met waarden boven/onder een bepaald getal
#check een getal of het priemgetal is
