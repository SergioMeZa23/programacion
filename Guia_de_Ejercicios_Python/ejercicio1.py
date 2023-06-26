
#ejercicio 1

num1 = int(input("ingrese el primer valor: "))
num2 = int(input("ingrese el segundo valor: "))
num3 = int(input("ingrese el tercer valor: "))

if num1>num2 and num1>num3 and num2>num3:

    print(f"{num3} es el menor, {num1} es el mayor")  
elif num2>num1 and num2>num3 and num1>num3:
    print(f"{num3} es el menor, {num2} es el mayor")

elif num3>num1 and num3>num2 and num2>num1:
    print(f"{num1} es el menor, {num3} es el mayor")
else:
    num2<num1 and num2<num3 and num3>num1
    print(f"{num2} es el menor, {num3} es el mayor")
print("")
print("")