
#ejercicio 3

lado1 = float(input("ingrse el primer lado: "))
lado2 = float(input("ingrse el segundo lado: "))
lado3 = float(input("ingrese el tercer lado: "))
p=(lado1+lado2+lado3)/2 
A=(p*(p-lado1)*(p-lado2)*(p-lado3))**(1/2)

if lado1==lado2 and lado1==lado3 and lado2==lado3:
     print("el tiangulo es equilatero")
     print(f"y su area es de {A:.2f}")
elif lado1==lado2 and lado1!=lado3 or lado2==lado1 and lado2!=lado3 or lado3==lado1 and lado3!=lado2 or lado3==lado2 and lado3!=lado1:
     print("el triangulo es isosceles")
     print(f"y su area es de {A:.2f}")
else:
     lado1!=lado2 and lado2!=lado3 and lado3!=lado1
     print("el triangulo es escaleno")
     print(f"y su area es de {A:.2f}")
print("")
print("")