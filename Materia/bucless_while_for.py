


# WHILE
num = 0
while num <= 200 :
     print (num)
     num += 2
else: print("Mi condición es igual o mayor a 200")
print()

while num <= 300 :
     print (num)
     num += 2
     if num == 250: #si el if se corre a la izquiera no lo lee
        print("Mi condición es igual a 250")
print()
while num <= 400 :
    print(num)
    num +=2
    if num == 350:
        print("numero igual a 350")
        break
print("fin recorrido")
print()


while True :
    parametro = input (">")
    if parametro == "exit": 
        break
    else: 
        print(parametro)
print() 
# FOR       

lista_nueva = [1,2,3,4,5,6,7,8,9,10] 
for i in lista_nueva:
    print(i)
    
for i in range(11): 
    print(i)
    
for i in range(1,11): 
    print(i)
