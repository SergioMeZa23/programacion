def vuelto_producto(monto,pago):
    billetes=[10000,5000,2000,1000,500,100,10,5,1]
    desglose={}
    vuelto=pago-monto
    for billete in billetes:
        if vuelto>=billete:
         cantidad=vuelto//billete
         desglose[billete]=cantidad
         vuelto-=cantidad*billete
        
    return desglose

print(">>>>>>>>>> Bienvenido <<<<<<<<<<")

print("ingrese el articulo que quiere llevar: ")   
producto=int(input("1)pelota  2)poleron  3)mochila  4)estuche\n"))

if producto==1:
   print("a seleccionado pelota, su precio es de 15000clp")
   
   pagorealizado=int(input("¿con cuanto desea pagar?: "))
   montototal=15000
   resultado=vuelto_producto(montototal,pagorealizado)
   if pagorealizado>montototal:
      print(f"su vuelto en billetes y monedas es {resultado}")
   elif pagorealizado<montototal:
      print("ingrese un valor valido")
   else:montototal==pagorealizado
   print("gracias por su compra")
   
    

if producto==2:
    print("a seleccionado poleron, su precio es de 10000clp")
    pagorealizado=int(input("¿con cuanto desea pagar?: "))
    
    montototal=10000
    resultado=vuelto_producto(montototal,pagorealizado)
    if pagorealizado>montototal:
      print(f"su vuelto en billetes y monedas es {resultado}")
    elif pagorealizado<montototal:
       print("ingrese un valor valido")
    else:montototal==pagorealizado
    
    print("gracias por su compra")
       
    

if producto==3:
   print("a seleccionado mochila,su precio es de 20000clp")
   
   pagorealizado=int(input("¿con cuanto desea pagar?: "))
   montototal=20000
   resultado=vuelto_producto(montototal,pagorealizado)
   if pagorealizado>montototal:
      print(f"su vuelto en billetes y monedas es {resultado}")
   elif pagorealizado<montototal:
      print("ingrese un valor valido")
   else:
      montototal==pagorealizado
      print("gracias por su compra")


if producto==4:
   print("a seleccionado estuche, su precio es de 1500clp")
   
   pagorealizado=int(input("¿con cuanto desea pagar?: "))
   montototal=1500
   resultado=vuelto_producto(montototal,pagorealizado)
   if pagorealizado>montototal:
      print(f"su vuelto en billetes y monedas es {resultado}")
   elif pagorealizado<montototal:
      print("ingrese un valor valido")
   else:montototal==pagorealizado
   print("gracias por su compra")