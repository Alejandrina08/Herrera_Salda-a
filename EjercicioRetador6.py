Nombre = ""

tupla_pasajero = tuple()
while True:
  Nombre = input("Nombre: ")
  if Nombre != "X":
    Edad = input("Edad: ")  
    IATA_del_Destino = input("Destino: ")
    tupla_pasajero = tupla_pasajero + (Nombre, Edad,IATA_del_Destino )
  else:
    break


#print("Pasajeros: ",tupla_pasajero)
destino = ['BJX', 'GDL', 'JAL']

numDestino= 0
edadPasajero = 0
tupla_detalle = tuple()
tupla_edadPromedio = tuple()


for Cdestino in destino:
  numDestino =0
  pasajeros =0
  test = 1
  for Cpasajero in tupla_pasajero:
    if Cdestino == Cpasajero:
      pasajeros += 1
      numDestino += 1
      print("PRUEBA",test)
      edadPasajero += int(tupla_pasajero[test])
      test = test +3
      print("EDAD PASAJEROS", edadPasajero)
      print("PASAJEROS",pasajeros)
  tupla_detalle = tupla_detalle + (Cdestino, numDestino)
  if (pasajeros > 0):
    Promedio = edadPasajero/pasajeros
    print("PROMEDIO",Promedio)
    cadenaPromedio = str(Promedio)
    tupla_edadPromedio = tupla_edadPromedio + (Cdestino, cadenaPromedio)


print("Detalles de vuelos:",tupla_detalle)

print("Edad promedio por vuelo:",tupla_edadPromedio)