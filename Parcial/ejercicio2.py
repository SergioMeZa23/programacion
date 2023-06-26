lista=[]
lista2=[]
n=int(input("ingrese cantidad de notas: "))


for i in range(n):
    num=int(input("ingrese las notas:"))
    if num%2==0:

        lista.insert(i,num)
        lista.sort()

    else:
        lista2.insert(i,num)
        lista2.sort(reverse=True)



print(lista)
print(lista2)