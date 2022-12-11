#3.1

empty = []
notEmpty = ["oui","non"]

#3.2

print(len(notEmpty))

#3.3

notEmpty[0] = "yes"
notEmpty.remove("non")
notEmpty.append("no")
print(notEmpty)

#3.4

i=0
while i<len(notEmpty):
    print(notEmpty[i])
    i=i+1
i=0
for i in range(0,len(notEmpty)):
    print(notEmpty[i])
    i=i+1