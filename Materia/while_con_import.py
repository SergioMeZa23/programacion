
import math
numero=int(input("digite un numero: "))

while numero<0:
    print("error deberia ser un numero positivo")
    numero=int(input("digite un numero postivo: "))

print(f"Su raiz cuadrada es: {(math.sqrt(numero)):.2f}")
print()
