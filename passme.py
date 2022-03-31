from src import *
import random
import sys
import pickle

try:
    open("log","x").close()
except:
    pass

All=""
for i in [alphabet.upper,alphabet.lower,specialchars.specialchars]:
    for x in i:
        All += x

try:
    if sys.argv[1] :
        pass
    target = input("enter target : ")

    with open('log',"rb") as fd:
        data = fd.read()
        base = pickle.loads(data)
        print(base[target])

except EOFError:

    base ={}
    base[target] = result

    with open('log','wb') as fd:
        pickld = pickle.dumps(base)
        fd.write(pickld)

except IndexError:
    inp = int(input("enter your passwords desired length : "))
    target = input("this pasaword is for ? : ")
    result =""

    for i in range(inp):
        tmp =All[( lsfr.lfsr(random.randint(1000,1000000))%len(All))]
        result += tmp
    print(result)


    with open('log','rb') as fd:
        data = fd.read()
        try:
            base = pickle.loads(data)
            base[target] = result
        except EOFError:

            base ={}
            base[target] = result

            with open('log','wb') as fd:
                pickld = pickle.dumps(base)
                fd.write(pickld)

    with open('log','wb') as fd:
        pickld = pickle.dumps(base)
        fd.write(pickld)
