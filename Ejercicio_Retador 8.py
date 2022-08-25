pasajeros = {}
x = 0

pasajeros= {"45471":["Luis Perez",45,"BJX",True],"8944411":["Fernanda Garcia",25,"JAL", True], "15223":["Alejandra Ortiz",33,"JDL", False]}

#FUNCIONES

def agregarClientes():
  ine = input("Ingresa el ID del INE: ")
  nombre = input("Ingresa el Nombre: ")
  edad = input("Ingresa la edad: ")
  destino = input("Ingresa el destino: ")
  cliente_preferente = input("Cliente preferente (Si/NO): ")
  pasajeros.update({ine: [nombre, edad, destino, cliente_preferente]})

def eliminarClientes():
  print("Eliminar un cliente mediante ID del INE")
  ine = input("Ingresa el ID del INE a eliminar: ")
  del pasajeros[ine]
  print(pasajeros)

  
def edadPromedio():
  print("Edad promedio de todos los clientes")
  edadPromedio = 0
  for pasajero in pasajeros.items():
    edadPromedio = edadPromedio + int(pasajero[1][1])
    print(edadPromedio)
  edadPromedio = edadPromedio / len(pasajeros)
  print("La edad promedio: " + str(edadPromedio))
  print("***********************")

def edadPromedioPreferentes():
  print("Edad promedio de todos los clientes")
  edadPromedio = 0
  contador = 0
  for pasajero in pasajeros.items():
    if pasajero[1][3]:
      contador = contador + 1
      edadPromedio = edadPromedio + int(pasajero[1][1])
      print(edadPromedio)
      print(contador)
  edadPromedio = edadPromedio / contador 
  print("La edad promedio: " + str(edadPromedio))
  print("***********************")
  
def mostrarClientes():
  print("Listar todos los clientes")
  print(pasajeros)
  
def mostrarClientesPreferentes():
  print("Listar clientes preferentes")
  for cliente in pasajeros.values():
    print(cliente[3])
    if cliente[3] == "Si":
      print(cliente)


  
print("MENU")



while True:
    print("(1) Añadir cliente")
    print("(2) Listar todos los clientes")
    print("(3) Listar clientes preferentes")
    print("(4) Eliminar un cliente mediante ID del INE")
    print("(5) Edad promedio de todos los clientes")
    print("(6) Edad promedio de clientes preferentes")
    print("(7) Salir.")
    menu = input("Seleccione una opción: ")

    if (menu == "1"):
      agregarClientes()
    elif menu == "2":
      mostrarClientes()
    elif menu == "3":
      mostrarClientesPreferentes()
    elif menu == "4":
      eliminarClientes()
    elif menu == "5":
      edadPromedio()
    elif menu == "6":
      edadPromedioPreferentes()
    elif menu == "7":
      print("Salir")
      break



