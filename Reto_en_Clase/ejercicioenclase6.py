#Obtener los números del rango 10 al 30,incrementando de 2 en 2.,sumar todos los números obtenidos.

num = 10
while num <= 30:
    print(num)
    num+=2
    
listanum= range(10,31,2)
suma=sum(listanum)
print(suma)
