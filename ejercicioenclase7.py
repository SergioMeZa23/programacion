

def contar_palabras(frase):
    palabras = frase.split()
    diccionario = {}

    for letras in palabras:
        diccionario[letras] = len(letras)

    return diccionario
frase = str(input("Ingrese frase: "))
resultado = contar_palabras(frase)
print(resultado)
print()
