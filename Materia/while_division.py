
#divide la cantidad de veces el numero que ingrese por el mismo 

while True:
    n=int(input("ingrese tabla de division a realizar: "))
    print()
    if n>=1:
     break
    else:
       print("ingrese un numero positivo")

for i in range(1,n+1):
    div=n/i
    print(f"{div:.2f}")