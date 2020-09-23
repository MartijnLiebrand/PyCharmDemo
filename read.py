#Verschillende mogelijkheden om een file te lezen en te schrijven.
#itereren over geretourneerde lijst, of over het file object..
#C:/\Users/\mlaliebran/\Desktop/\Minor/ DS/\Week Theorie/\Python/ Demo/ en/ Opdrachten/\Datasets/\to_merge.txt
#file = open('text.txt', 'r')
#probeer eens de verschillende imports te timen

"""
from datetime import datetime

start = datetime.now()
file = open('C:\\Users\\mlaliebran\\Desktop\\Minor DS\\Week Theorie\\Python Demo en Opdrachten\\Datasets\\to_merge.txt', "r")
file.read()
stop = datetime.now()
print(datetime.timestamp(stop)-datetime.timestamp(start))
file.close()


start = datetime.now()
file = open('C:\\Users\\mlaliebran\\Desktop\\Minor DS\\Week Theorie\\Python Demo en Opdrachten\\Datasets\\to_merge.txt', "r")
file.readline()
stop = datetime.now()
print(datetime.timestamp(stop)-datetime.timestamp(start))
file.close()

start = datetime.now()
file = open('C:\\Users\\mlaliebran\\Desktop\\Minor DS\\Week Theorie\\Python Demo en Opdrachten\\Datasets\\to_merge.txt', "r")
file.readlines()
stop = datetime.now()
print(datetime.timestamp(stop)-datetime.timestamp(start))
file.close()


"""


with open("text.txt", "r") as file:
    for regel in file:
        print(regel)



with open("text.txt", "a") as f:
    f.writelines("test")
