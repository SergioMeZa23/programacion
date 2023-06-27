diccionario = {}
diccionario = {
"nombre": "sergio",
"institucion": "ulagos",
"edad": "20",
"asignatura": "estructura de datos, programacion"
}
print("diccionario inicial", diccionario)
print("")

#mostrar un dato en especifico
print(diccionario ["edad"])

#añadir nuevos elementos al diccionario
diccionario["año"]=2023 #se coloca la nueva y sus elementos
print(diccionario["año"])

#editar elementos de un diccionario
diccionario["año"]=2033
print(diccionario["año"])

#solo mostrar los programas: nombre institucion etc
for programa in diccionario:
    print(f"-{programa}")#se le coloca diseño