
#ejercicio2
a = [10,9,12,15,18]
b = [21,8,15,3,12]
print(a)
print(b)
print()
#conttenar las dos listas
res=a+b
print(res)
print()
#cambiar numero posicion 2
res[1]=30
print(res)
print()
#falta ordenar la lista
res.sort()
print(res)
#345681012121515,
#agregrar otra lista
lista= [4,5,6]
suma2=res+lista
print(suma2)
print()
#suma de todos los elementos 
res2=sum(suma2)
print(res2)
print()
#media 
media = sum(suma2)/len(suma2)
print(f"La media es: {media:.2f}")
print()
#mediana ta mala falta ordenar
mediana = 15
print(f"La mediana es: {mediana:.2}")
print()