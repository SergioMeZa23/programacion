asignatura = "programacion"
carrera = "ingenieria civil en informatica"
print("la asignatura de",asignatura,"corresponde a la carrera de",carrera)

#otro ejercicio
print("los caracteres de la palabra", asignatura, "es de:", len(asignatura))

#otro ejercicio
estudiantes=["matias","marco","cristobal","sebastian", "marco"] 
num=[1,2,3,4,5]
lenguaje= ["python"]

#falta lista de diferentes elementos
listamixta = ["sergio", {}]



#lista 
data=["osorno", "juan", "pepe","johan","marcelo"]
      
#funcion lent para lista (ver cantidad de datos)
print(len(data))

#mostrar un elemento de la lista 
print(data[3])
print(data[-2])

#mostrar la letra de una palabra de la lista
lista_colores = ["amarillo", "azul"]
print(lista_colores[1][3])
#pedir datos y dar de salida
nombre = input("¿cual es tu nombre?")
print(f"tu nombre es, {nombre}")


#condiciones
altura = 180
if altura >=170:
    print("10cm menor a 180")

#condicion con pedir datos
altura = int(input("¿cual es tu altura?:"))

if altura > 150:
    print("altura es normal")   

else:
    altura <150
    print("altura menor a la normal")

#condcion pedir numero y resultado
print("ingrese un numero entero")
numero = int(input("ingrese un numero:"))

if numero > 0:
    print("el numero es positivo")
elif numero == 0:
    print("el numero es cero")
else:
    numero < 0
    print("el numero es negativo")

#condicion pedir numero(decimal) y resultado
print("ingrese un valor entero o decimal")
numero = float(input("ingrese un numero entero o decimal:"))

if numero > 0:
    print("el numero es positivo")
elif numero == 0:
    print("el numero es cero")
else:
    numero < 0
    print("el numero es negativo")


      

