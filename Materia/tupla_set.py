#suma de listas duplas
newtupla = tuple()
grupo1 = ("matias", "marcos", "sergio", 200, 500)
print(type(grupo1))

#acceder a un elemnto de la tupla
print(grupo1[0])

#lista.cuont ver cuantas veces se repite un dato
print(grupo1.count("sergio"))

#muestra el indice del primer elemento
print(grupo1.index ("sergio"))



#obtener una parte de la tupla
grupo2 = ("pedro", "sergio", 100, "diego",2020, "daniela")
print("parte de una tupla ,grupo2{0:3}")

#como modificar una tupla
grupo1 = list(grupo1)
print("la tupla ahora es de tipo:", type(grupo1), "\n")

#sets o conjuntos
conjunto_vacio = set()
conjunto_vacio1 = {} #colocar elemntos separados por comas
print(type(conjunto_vacio1))
conjunto_colores = ("rojo", "verde", "azul")
conjunto_animales = {"gato", "perro", "loro"}

print(type(conjunto_colores))
print(type(conjunto_animales))
print("el conjunto contiene los siguientes colores:", conjunto_colores)
print("el conjunto contiene los siguientes animales:", conjunto_animales)
#no se puede consultar posicion
#estructura fija 

