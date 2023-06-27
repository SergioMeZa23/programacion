

def sum(n):
    suma=n+3
    return suma

print(sum(5))

#distinta forma hacen lo mismo

def sum(n):
    print(n+3)

sum(5)


#tabla de multiplicar

def table_multi(num):
    for i in range(1,11):
        print(num,"*",i,"=",i*num)

table_multi(5)

#seperar elementos dentro de una lista
lista=[3,7,9,5,8,3,1,9,6,7]

def impar(lista):
    lista.sort()
    pares=[]
    impares=[]
    for i in lista:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares

print(impar(lista))