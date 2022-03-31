from src import *
import random

All=""
for i in [alphabet.upper,alphabet.lower,specialchars.specialchars]:
    for x in i:
        All += x

run = True

while run:
    inp =int( input("enter length of your desired password :"))
    for i in range(inp):
        j = lsfr.lfsr(random.randint(1000,1000000))%len(All)
        print(All[j] , end="")

    break

