#ejercicio 9
numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
print("numeros de la lista:")
print(numeros)
print("")
numeros.pop(8)
print("se elimina el ultimo elemento")
print(numeros) 
print("")
numeros.insert(0, 2)
print("se agrega el 2 en la posicion del indice 0")
print(numeros)
print("")
numeros1 = set(numeros)
print("se elimina el elemento repetido (3)")
print(numeros1)
print("")
numeros2 = sum(numeros1)/len(numeros1)
print("se saca la media de la lista")
print(f"media de la lista: {numeros2:.1f}")
print("")
mediana = (6+8)/2
print("se saca la mediana de la lista")
print(f"mediana de la lista: {mediana:.1f}")
print("")
print()