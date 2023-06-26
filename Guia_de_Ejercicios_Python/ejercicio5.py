
#ejercicio 5 

lab1 = float(input("ingrese primera nota: "))
lab2 = float(input("ingrese segunda nota: "))
lab3 = float(input("ingrese tercera nota: "))
promedio = lab1*0.3+lab2*0.4+lab3*0.3
print(f"promedio ponderado: {promedio:.1f}")
print("")
if promedio>=1.0 and promedio<=3.9:
    print("el alumno reprobo")
elif promedio<=5.9 and promedio>=3.9:
    print("el alumno aprobo")
else:
    promedio>=5.9 and promedio==7.0
    print("el alumno aprobo con distincion")
print("")