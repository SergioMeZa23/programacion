
#mostrar la letra de una palabra de la lista
lista_colores = ["amarillo", "azul","morado","celeste"]
print(lista_colores[1][3])

#cambiar datos dentro de una lista
lista_colores[1]="rojo"
print(lista_colores)

#eliminar un dato con el indice
lista_colores.pop(0)
print(lista_colores)
#remove es con la palabra
#count cuantas veces se repite un elemento
print(lista_colores.count("rojo"))
#index nos da el indice
#sort ordena alfabeticamente
#extend unir dos listas
type(lista_colores)