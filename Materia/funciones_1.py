

def notas(num1,num2,num3):
    suma=(num1+num2+num3)/3
    return suma
   

num1=float(input("nota 1: "))
num2=float(input("nota 2: "))
num3=float(input("nota 3: "))

print(f"{notas(num1,num2,num3):.1f}")

