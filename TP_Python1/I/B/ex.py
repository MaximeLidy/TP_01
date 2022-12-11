import random
import time

#b

#1

def fonctionRandom(n):
    i=0
    nombres = []
    while i <= n :
        nombres.append(random.randint(1,100))
        print(nombres)
        i=i+1
    return nombres

def fonctionRandom2(n):
    nombres = []
    for i in range(0,n):
        nombres.append(random.randint(1, 100))
        print(nombres)
fonctionRandom(8)

#2

def nom(n):
    nEntiers = []
    for i in range(0,n):
        nEntiers.append((i))
    random.shuffle(nEntiers)
    print(nEntiers)

debut = time.time()
nom(10)
print(time.time()-debut)

#a

#1

def moyenne(n):
    moy = 0
    for i in range(0,len(n)):
        moy = moy + n[i]
    moy = moy/len(n)
    return moy
m = [1,1,1,1,2,2,2,2,3,3,3,3,6,4,8,7,7,11,10]
tableau = fonctionRandom(10)

#2

def compte(n, tab):
    occ = 0
    for i in tab:
        if i == n:
            occ = occ+1
    return occ

print(compte(1,m))

#3

def compte(n, tab):
    occ = 0
    for i in tab:
        if i >= 10:
            occ = occ+1
    return occ

print(compte(1,m))

#4

def mx(tab):
    max = 0
    for i in tab:
        if i > max:
            max = i
    return max

print(mx(m))
print(max(m))

#5

def present(n, tab):
    if n in tab:
        return n ," présent"
    else:
        return n ," pas présent"

print(present(12,m))