edad = 15
num = 0

while num <= 200:
    print(num)
    num+=2
    if num == 200:
        print("la condicion es igual a 200")

while num <= 400:
    print(num)
    num+=2
    if num == 350:
        print("se detiene la ejecucion")
        break
print(num)
print("bucle terminado")

#infinito mas break 
while True:
    parametro =input(">")
    if parametro == "exit":
        break
    else:
        print("parametro")

#for para recorrer listas, la lee hacia abajo
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

#otra forma
nueva_lista=[1,2,3,4,5,6,7,8,9,10]
for i in nueva_lista:
    print(i)

#otra forma
for i in range(1,11):
    print(i)


