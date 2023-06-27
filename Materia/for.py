# el iterador (i) recorre elemento por elemento/ lista, bucle y conjuntos
coleccion=[1,2,3,4,5,6]
for i in coleccion:
    print(i)
print()

#puede ser de las dos formas
for i in [1,2,3,4,5,6]:
    print(i)
print()

# iterador en diccionario
diccionario= {"alejandro":22, 
"jose":23, 
"maria":48, 
"luis":12
}
for i in diccionario:
    print(i) #solo imprime las claves
print()

for i in diccionario:
    print(diccionario[i]) #imprime los valores del diccionario
print()

for i in diccionario:
    print(f" {i}:{diccionario[i]}")#imprime valores y claves 
print()

#distinta forma de hacer lo anterior 
for clave,valor in diccionario.items(): #el items recorre todo
    print(f"{clave}:{valor}",end=" ")
print()

#imprimir todo en una linea en vez que sea todo hacia abajo
linea= "sergio"
for i in linea:
    print(f"{i}",end=" ")
