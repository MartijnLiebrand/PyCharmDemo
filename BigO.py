#In welke mate neemt het aantal operaties toe,
# in het geval x toeneemt:

#Voorbeeld 1
def eenFunctie(x):
    return x * 0.75 + 6

#Voorbeeld 2
def isPriem(x):
    priem = True
    for i in range(2, x):
        if (((x / i) % 1)==0):
            priem = False
    return priem

#Voorbeeld 3
def loopLijst(x):
    for i in x:
        for j in x:
            print(i+j)

x = [1,2,3,4,5,6]
loopLijst(x)