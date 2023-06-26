
set1 = {100, 250, 300, 1000}
set2 = {150, 250, 500, 1000}

while True:
    if 100==len(set1) and 100==len(set2):
        print("100 esta en ambas listas")
        break
    if 100==len(set1) or 100!=len(set2):
        print("el 100 solo esta en el set1")
        break
    else:
        print("el 100 no esta en ambas")
        break

while True:
    if 500==len(set1) and 500==len(set2):
        print("el 500 esta en ambas")    
    if 500==len(set1) and 500!=len(set2):
        print("el 500 esta en el set1")      
    else:
        500!=len(set1) and 500==len(set2)
        print("el 500 esta en el set2 ")
        break

print()

#set pasaddos a tuplas
tupla=set1
tupla=tuple(set1)
tupla2=set2
tupla2=tuple(set2)

#tupla1 elevada
for i in tupla:
    elevar=i*i
    print(elevar)
print()
#tupla2 elevada
for i in tupla2:
    elevar2=i*i
    print(elevar2)



print()
#set unidos
unir=set1|set2
print(unir)