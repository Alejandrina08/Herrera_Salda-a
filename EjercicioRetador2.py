municipios = []
habitantes = []
sumatoria_habitantes = 0
promedio_habitantes = 0

contador = 0

while contador <3 :
  nombre_municipio = input('Ingresa el nombre de un municipio: ')
  numero_habitantes = input('Ingresa el el numero de habitantes de '+nombre_municipio+' : ')
  municipios.append(nombre_municipio)
  habitantes.append(numero_habitantes)
  contador = contador+1


sumatoria_habitantes = int(habitantes[0])+int(habitantes[1])+int(habitantes[2])
cadena_sumatoria_habitantes = str(sumatoria_habitantes)

promedio_habitantes = sumatoria_habitantes / 3
cadena_promedio_habitantes = str(promedio_habitantes)

print("El total de habitantes es: "+cadena_sumatoria_habitantes)
print("El promedio de habitantes es: "+cadena_promedio_habitantes)
