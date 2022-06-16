costales_cemento = input("Número de costales de cemento (kg): ")
costales_yeso = input("Número de costales de yeso (kg): ")


capacidad_maxima_camion = 3254


peso_total =  int(costales_cemento) + int(costales_yeso)

if(peso_total < capacidad_maxima_camion and peso_total > (capacidad_maxima_camion/2)):
  condicion_camion = "True"

else:
  condicion_camion = "False"


print("El peso total en kg es: "+str(peso_total))
print("¿Se puede realizar el envío?: "+condicion_camion)
