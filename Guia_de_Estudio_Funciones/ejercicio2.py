def contar_palabras(nombre):
    palabras = nombre.split()
    diccionario = {}

    for letras in palabras:
        diccionario[letras] = len(letras)

    return diccionario
cantidad=int(input("¿cuantos nombres va a ingresar?: "))

for i in range(cantidad):
    nombre = str(input("Ingrese nombre: "))
    resultado = contar_palabras(nombre)


print(resultado)
print()

