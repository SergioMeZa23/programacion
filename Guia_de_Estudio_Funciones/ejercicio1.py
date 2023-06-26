

def sumanumeros(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

def suma_pares1(lista):
    suma_pares = 0
    for i in lista:
        if i%2 == 0:
            suma_pares += i
    return suma_pares

def suma_imapares1(lista):
    suma_impares = 0
    for i in lista:
        if i%2 != 0:
         suma_impares += i
        return suma_impares

cant = int(input("¿cuantos numeros quiere ingresar?: "))
numeros = []

for i in range(cant):
    numeros.append(int(input("Ingrese un numero: ")))

suma_numeros = sumanumeros(numeros)
suma_pares = suma_pares1(numeros)
suma_impares = suma_imapares1(numeros)

print("La suma de los numeros ingresados es:",suma_numeros)
print("La suma de los numeros pares es:",suma_pares)
print("La suma de los numeros impares es:",suma_impares)



        




    




