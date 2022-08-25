pasajeros = {}
x = 0
print("MENU")
while True:
  print("(1) Añadir cliente")
  print("(2) Listar todos los clientes")
  print("(3) Listar clientes preferentes")
  print("(4) Salir.")
  menu = input("Seleccione una opción: ") 

  if( menu == "1"):
    ine = input("Ingresa el ID del INE: ")
    nombre = input("Ingresa el Nombre: ")
    edad = input("Ingresa la edad: ")
    destino = input("Ingresa el destino: ")
    cliente_preferente = input("Cliente preferente (Si/NO): ")

    pasajeros.update({ine: [nombre,edad,destino,cliente_preferente]})

  elif menu =="2":
    print("Listar todos los clientes")
    print(pasajeros)
  elif menu == "3":
    print("Listar clientes preferentes")
    for cliente in pasajeros.values():
      print(cliente[3])
      if cliente[3] == "Si":
          print(cliente)      
  elif menu == "4":
    break
