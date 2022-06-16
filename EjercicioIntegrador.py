venta_productos = [
[2, 122], 
[1, 89], 
[1, 22], 
[3, 48], 
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]
ID_producto = 0;
tipo_producto = ""
costo_producto = 0.0


#Entrada
cajas_vender = input("Número de cajas a vender: ")
ID_producto = input("ID del producto: ")

#Buscar Producto
valor = str(ID_producto)
if ID_producto == "1" :
  tipo_producto = "Maíz grano"
  costo_producto = 285.55
elif ID_producto == "2":
  tipo_producto = "Pepino"
  costo_producto = 334.72
elif (ID_producto == "3"):
  tipo_producto = "Tomate verde"
  costo_producto = 129.00
else:
  print("Este producto no se encuentra en el inventario")


#Sumar ventas del dia
ventas_totales = 0
x=0
tamaño_lista=len(venta_productos)

for k in venta_productos:
  
  x=x+1
  if venta_productos[x-1][0] == int(valor):
    ventas_totales = int(cajas_vender) + int(venta_productos[x-1][1] + ventas_totales)
    #print(ventas_totales)

    
    
aplica_descuento = ""
costo_total_pagar = 0.0
#Aplica del descuento de 20%

if ventas_totales < 1500:
    print("Descuento")
    ventas = float(costo_producto) * float(ventas_totales)
    costo_total_pagar = ventas - (ventas * 0.20)
    #print(costo_total_pagar, ventas)
    aplica_descuento = "True"
  
else:
  print("No aplica")
  ventas = float(costo_producto) * float(ventas_totales)
  costo_total_pagar = ventas
  aplica_descuento = "False"
  #print(ventas)




print("El producto es: "+tipo_producto)
print("El precio por caja es: "+str(costo_producto))
print("Aplica descuento del 20%: "+(aplica_descuento))
print("El costo total a pagar: "+str(costo_total_pagar))