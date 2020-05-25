seed = 10000000000
pSeedL = list(str(seed))
pSeedL.remove(pSeedL[0])

a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
j = 8
k = 9

while True:
    seedL = list(str(seed))
    seedL.remove(seedL[0])

    if (seedL[c] != pSeedL[c]):
            print(seedL[0] + seedL[1] + "." + seedL[2] + " %")

    
    if int(seedL[g] + seedL[e] + seedL[g]) - int(seedL[h] + seedL[d] + seedL[b]) == int(seedL[e] + seedL[f]):
        
        seed += 1
        if int(seedL[e] + seedL[e] + seedL[g]) - int(seedL[g] + seedL[c] + seedL[e]) == int(seedL[j] + seedL[f] + seedL[a]):
            
            if int(seedL[j] + seedL[c] + seedL[c]) - int(seedL[h] + seedL[k]) == int(seedL[b] + seedL[e] + seedL[f]):
                print("#1 " + seedL[g] + seedL[e] + seedL[g] + " - " + seedL[h] + seedL[d] + seedL[b] + " = " + seedL[e] + seedL[f])
                print("#2 " + seedL[e] + seedL[e] + seedL[g] + " - " + seedL[g] + seedL[c] + seedL[e] + " = " + seedL[j] + seedL[f] + seedL[a])
                print("#3 " + seedL[j] + seedL[c] + seedL[c] + " - " + seedL[h] + seedL[k] + " = " + seedL[b] + seedL[e] + seedL[f])
                if len(seedL) == len(set(seedL)):
                    print("\n \n" + str(seed - 1) + "\n \n")
                    break
    else:
        seed += 100
    pSeedL = seedL   
