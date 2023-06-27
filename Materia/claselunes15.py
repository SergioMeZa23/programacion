# para la prueba dupla, set, lista, diccionario

#opradores
a = 2
b = 3
#modulo para saber si  es operacion exacta 
print(a % b)
#cociente
print(a // b )

#complex numeros complejos
c2 = complex (3,-5)
print(c2) 
print(c2.real)#imprime numero real
print(c2.imag)#imprime numero imaginario

#multiplicar atring con un numero 
print("hola" * 5)
#se puede multiplicar mientras no sea un decimal

#opradores de comparacion
print(a==b)#igual 
print(a | b)#distinto  de
print(a>b)#mayor que
print(a<b)#menor que 
print(a>=b)#mayor o igual 
print(a<=b)#menor o igual 
#siempre dan como resultado un booliano (true o false)
#codigo ASCII valor que se le da a la letras (A / a)

#opradores logicos 
# not, and y or
encendido = True
bencina = False
edad = 10
if not bencina or (bencina and edad >= 18):
    print("el veiculo no puede avazar")
else:
    print("el veiculo no puede avanzar")

# = asignar 
# == comparar 
