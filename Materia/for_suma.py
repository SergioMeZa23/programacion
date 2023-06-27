while True:
    n=int(input("ingrese un numero positivo: "))
    print()
    if n>=1:
     break
    else:
       print("ingrese un numero positivo")

suma=0

for i in range(1,n+1):
   elevado=i*i
   suma= suma+elevado

   print(suma)

#te saca la raiz cuadrada mas el valor ingresado