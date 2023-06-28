
def estatura_minima(pacientes):
    estatura_min = pacientes[0][1]
    for paciente in pacientes:
     if paciente[1] < estatura_min:
      estatura_min = paciente[1]
    return round(estatura_min, 1)

def insertar_paciente(pacientes, nombre, estatura):
    pacientes.append([nombre, estatura])
    return pacientes

def encontrar_paciente(pacientes, nombre):
    for paciente in pacientes:
     if paciente[0] == nombre:
      return (paciente[0], paciente[1])
    return "No se encuentra el paciente"

pacientes = [["Pedro", 1.78], ["Constanza", 1.56], ["Amanda", 1.62], ["Dario", 1.89], ["Fernanda", 1.67]]
print("Estatura mínima: ", estatura_minima(pacientes))

pacientes = insertar_paciente(pacientes, "Ricardo", 1.71)
print("Pacientes actualizado: ", pacientes)

encontrado = encontrar_paciente(pacientes, "Dario")
if encontrado != "No se encuentra el paciente":
    print("Dario: ", encontrado[0], encontrado[1])
else:
    print(encontrado)