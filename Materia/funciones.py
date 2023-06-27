#no entra parcial 3 miercoles31
#realizar codigo en especifico pa

def primera_funcion():
    print("primera funcion")#la tabulacion determina que el print esta dentro de la funcion

primera_funcion()

def concatenar(lista1,lista2):
    return lista1+lista2

#la lista se declara fuera del def(scop local)
lista1=[1,2,3]
lista2=[4,5,6]

#concatenar
print(concatenar(lista1,lista2))

#multiplcacion 
def multiplicacion(num1,num2):
    return num1*num2

#multiplicacion()
print(multiplicacion(5,5))

#funcion suma y resta por teclado

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

a=int(input("ingrese valor: "))
b=int(input("ingrese valor: "))

#se llama a la funcion suma
resultado=suma(a,b)
print(f"la suma es:",{resultado})

#se llamma a la funcion resta
resultado=resta(a,b)
print(f"la resta es:",{resultado})

#cadena palabras  #no esta terminado
def cadena(cad,v=2):
    print(cad*v)
print(,4)