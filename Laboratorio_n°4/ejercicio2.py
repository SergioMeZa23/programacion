a = ["Rojo", "Verde", "Celeste", "Violeta"]
b = ["Osorno", "Puerto Montt", "Puerto Varas", "Valdivia"]

def palabra_mas_larga(lista):
    max_len = 0
    palabra = ""
    for i in lista:
        if len(i) > max_len:
            max_len = len(i)
            palabra = i
    return palabra

print("La palabra más larga de la lista a es:", palabra_mas_larga(a))


def palabra_mas_corta(lista):
    min_len = float('inf')
    palabra = ""
    for i in lista:
        if len(i) < min_len:
            min_len = len(i)
            palabra = i
    return palabra

print("La palabra más corta de la lista b es:", palabra_mas_corta(b))


def concatenar_listas(lista1, lista2):
    return lista1 + lista2

concatenadas = concatenar_listas(a, b)
print("listas concatenadas:", concatenadas)


def convertir_a_mayusculas(lista):
    return [i.upper() for i in lista]

a_mayusculas = convertir_a_mayusculas(a)
b_mayusculas = convertir_a_mayusculas(b)
print("Lista a en mayusculas:", a_mayusculas)
print("Lista b en mayusculas:", b_mayusculas)


def ordenar_lista(lista):
    return sorted(lista)

a_ordenada = ordenar_lista(a)
b_ordenada = ordenar_lista(b)
print("Lista a ordenada:", a_ordenada)
print("Lista b ordenada:", b_ordenada)