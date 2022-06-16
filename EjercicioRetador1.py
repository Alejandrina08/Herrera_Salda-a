superficie_Sinaloa = 57365
temperatura_media_anual = 25.45
precipitacion_anual_promedio =  790.1

lista_tipo_clima = ["calido", "subhumedo", "seco","semiseco"]

poblacion_mujeres =  1532128 
población_hombres = 1494815 

porcentaje_habitantes_Culiacan = 33.15
porcentaje_habitantes_Mazatlan =  16.57

poblacion_total_Sinaloa = población_hombres + poblacion_mujeres
porcentaje_total_de_población = porcentaje_habitantes_Culiacan + porcentaje_habitantes_Mazatlan

cadena_poblacion_total_Sinaloa = str(poblacion_total_Sinaloa)
cadena_porcentaje_total_de_población = str(porcentaje_total_de_población)
cadena_temperatura_media_anual= str(temperatura_media_anual)


print("1.- Población total de Sinaloa de Hombres y Mujeres: "+cadena_poblacion_total_Sinaloa)
print("2.- Porcentaje total de poblacion de Culiacán y Mazatlán: "+cadena_porcentaje_total_de_población+"%")
print("3.- La temperatura media anual es: " + cadena_temperatura_media_anual + " y los tipos de clima son: "+lista_tipo_clima[0]+","+lista_tipo_clima[1]+","+lista_tipo_clima[2]+","+lista_tipo_clima[3])
