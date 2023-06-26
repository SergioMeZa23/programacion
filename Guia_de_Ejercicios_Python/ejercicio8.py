#ejercicio 8
print("Ingrese un mes para saber la estacion")
estacion = input("Mes: ")
verano = ("diciembre","enero","febrero")
otoño = ("marzo","abril","mayo","junio")
invierno= ("julio","agosto","septiembre")
primavera=("octubre","noviembre")
print("")
print("")
if estacion in ("diciembre","enero","febrero"):
    print("este mes se encuentra en verano")
elif estacion in ("marzo","abril","mayo","junio"):
    print("este mes se encuentra en otoño")
elif estacion in ("julio","agosto","septiembre"):
    print("este mes se encuentra en invierno")
else:
    estacion in ("octubre","noviembre")
    print("este mes se encuentra en primavera")
print("")
print("")