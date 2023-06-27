
#ver igualdad de conjuntos
a = {1,2,3}
b = {4,5,6}
print(a == b)

#funcion len para ver cuantos elementos hay
print(len(a))

#sumar dos conjuntos
print(a|b)

#diferencia de datos que hay en a respecto a b, datos que hay en a que no estan en b

a = {1,2,3}
b = {3,5,6}
c = a - b 
print(c)

#diferencia simetrica, datos que hay en a y b pero no el que esta en ambos  
a = {1,2,3}
b = {3,5,6}
c = a ^ b
print(c)

#subconjuntos
a = {1,2,3}
b = {4,5,6}
c = {1,2,3,4,5,}
print(a .issubset(c))
print(b .issubset(c))

#superconjunto
a = {1,2,3}
b = {4,5,6}
c = {1,2,3,4,5,}
print(c .issuperset(a))
print(c .issuperset(b))

#conjuntos disconexos, (comparten=false) (no comparten=true) 
a = {1,2,3}
b = {3,5,6}
print(a .isdisjoint(b))
