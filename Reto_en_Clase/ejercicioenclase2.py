
nombre = input("ingrese el nombre del estudiante: ")
asignatura = input("ingrese nombre de la asginatura: ")
notalab1 = float(input("ingrese nota laboratorio n°1: "))
notalab2 = float(input("ingrese nota laboratorio n°2: "))
ponderacion = float(notalab1*0.30 + notalab2*0.70)


ponderacion = {
"nombre" : nombre,
"asignatura" : asignatura,
"notalab1" : notalab1,
"notalab2" : notalab2,
"poderacion" : ponderacion,
}

print(ponderacion)