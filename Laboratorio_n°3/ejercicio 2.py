#ejercicio1 
region1 = {
"ID Región":8,
"Nombre":"BioBío",
"Superficie (Km2)":23890,
"Habitantes 2017)":1556805
}
print()
region2 = {
"ID Región":10,
"Nombre":"Los Lagos",
"Superficie (Km2)":48583,
"Habitantes 2017)":828708
}
print()
#imprimir listas
print(region1)
print(region2)
print()
den = 1556805/23890
den2 = 828708/48583
#densidad poblacional
print("densidad")
print(f"la densidad poblacional de la region del BioBio es: {den:.1f}")
print(f"la densidad poblacional de la region del Los Lagos es: {den2:.1f}")
print()
#agregar capital
print("agregar capital")
region1["Capital"]="Concepcion"
print(region1)
region2["Capital"]="Puerto Montt "
print(region2)
print()
#agregar comunas
print("agregar comunas")
region1["Comunas"]="Lota, Lebu, Los Ángeles"
print(region1)
region2["Comunas"]="Castro, Puerto Varas, Purranque"
print(region2)
print()
#agregar provincias
print("agregar provincias")
region1["Provincias"]=("Biobío, Arauco, Concepción")
print(region1)
region2["Provincias"]=("Osorno, Llanquihue, Chiloé, Palena")
print(region2)
print()
print("imprimir diccionario finalizado")
print(region1)
print()
print(region2)
print()