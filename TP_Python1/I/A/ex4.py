import random

#4.1

print("exo 4")
tab = [1,2,3,4,5,6,7,8,9]
print(random.randint(1,20))
print(random.randrange(1,10,5))
print(random.choice(tab))
random.shuffle(tab)
print(tab)