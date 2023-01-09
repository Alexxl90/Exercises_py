a = [1, 2, 2, 3, 5, 7, 7, 9]
b = [2, 3,3, 4, 11, 7, 9, 2]
a.sort()
b.sort()
c =[]
for element in a:
    if element in b:
        c.append(element)
c = set(c) #initial nu am facut chestia asta si imi afisa si duplicate. Am inteles destul de bine ce face si ce este "set"
#c = list(set(c))->am gasit si solutia asta pe net dar nu inteleg de ce as schimba din set in lista atat timp cat imi intoarce acelasi rezultat.
print (sorted(c))
