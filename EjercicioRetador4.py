tipo_producto = ""
costo_producto = 0.0


cajas_vender = input("Número de cajas a vender: ")
ID_producto = input("ID del producto: ")

print(ID_producto)
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

costo_total_pagar = float(costo_producto) * float(cajas_vender)


print("El producto es: "+tipo_producto)
print("El precio por caja es: "+str(costo_producto))
print("El costo total a pagar: "+str(costo_total_pagar))