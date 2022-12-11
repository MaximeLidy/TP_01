#1.

#1

print("ex 1.1")

def index_minimum(t,d,f):
    if d < f:
        min = None
        j = 0
        for i in t:
            if j >= d and j<= f:
                if min is None or min > t[j]:
                    min = t[j]
            j+=1
        #print("La valeur la plus basse comprise entre les index ",d," et ",f," est :",min)
        return min
    else:
        print("Faites en sorte que le premier index soit inférieur au deuxième")

tab = [15,44,68,80,41,67,27,91]

print(index_minimum(tab,5,7))

#2
print("ex 1.2")
def tri_a_bulles(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]

tri_a_bulles(tab)

for i in range(len(tab)):
    print("%d" % tab[i])

#2.

#1

print("ex 2.1")

tab_tri = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def recherche(tab, cible):
    i=0
    while tab[i] <= cible:
        i+=1
        if tab[i] == cible:
            print("Cible trouvée !")
        else:
            print("Pas de cible dans la liste")
            break


recherche(tab_tri,21)

#2

print("ex 2.2")

def rechercheDichotomique(tab, cible):
    x = 0
    y = len(tab)-1
    m = (x+y)//2
    while x < y :
        if tab[m] == cible:
            print("Cible trouvée par dichotomie !")
            break
        elif tab[m] > cible:
            y = m-1
        else :
            x = m+1
        m = (x+y)//2

rechercheDichotomique(tab_tri, 19)

#3

print("ex 2.3")

list = [12, 5, 16, 7, 2]

def insertion(e,t,n):
    ancien_hold = None
    nouveau_hold = None
    remplace = False
    for i in range(len(t)):
        if remplace is True:
            ancien_hold = t[i]
            t[i] = nouveau_hold
            nouveau_hold = ancien_hold
        if i == n:
            nouveau_hold = t[i]
            t[i] = e
            remplace = True
        if i == len(t)-1:
            t.append(ancien_hold)
    return(t)

print(insertion(10, list, 2))

#3.

#1

print("ex 3.1")

list = [12, 5, 16, 7, 2]

def tri_extraction(t):
    t_tri = []
    max = len(t)
    i = 0
    while i < max:
        t_tri.append(index_minimum(t,0,len(t)))
        t.remove(index_minimum(t,0,len(t)))
        i += 1
    return(t_tri)

print(tri_extraction(list))

#2

print("ex 3.2")

'''

def tri_insertion(t):
    
print(tri_insertion(test))'''