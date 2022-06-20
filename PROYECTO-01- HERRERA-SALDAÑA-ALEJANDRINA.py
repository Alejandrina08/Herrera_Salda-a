import lifestore_file


#Login de usuario-administrador:

print("Registro de usuario", '\n')
usuario = input("Ingrese el nombre de usuario: ")
contraseña = input("Ingrese la contraseña: ")
print('\n')

if usuario == "emtech" and contraseña == "caso1":
    print ("Datos ingresados correctamente")
    #Productos más vendidos y productos rezagados:
    print(".::Productos más vendidos y productos rezagados::.")
    print('\n')
    print('\n')
    
    
    ventaDeProductos=[]
    from collections import Counter
    
    for pro in range(0,len(lifestore_file.lifestore_sales)-1):
      ventaDeProductos.append(lifestore_file.lifestore_sales[pro][1])
      cantProductos = Counter(ventaDeProductos)
      listaProductos = cantProductos.most_common(1) 
          
    for pro in range(0,len(lifestore_file.lifestore_searches)-1):
      ventaDeProductos.append(lifestore_file.lifestore_searches[pro][1]) 
      cantProductos = Counter(ventaDeProductos)
      listaProductos = cantProductos.most_common()  
    
    
    
    print("Top 5 Productos mas vendidos")
    print('\n')
    for top in range(0,4):
      print("el producto más vendido es: ", lifestore_file.lifestore_products[listaProductos[top][0]-1])
      print('\n')
    
    
    print("Top 10 Productos mas buscados")
    print('\n')
    for top in range(0,10):
      print("el producto más buscados es: ", lifestore_file.lifestore_products[listaProductos[top][0]-1])
      print('\n')
    
    
    #Productos más vendidos y productos rezagados:
    print(".::Productos más buscados y productos menos vendidos::.")
    print('\n')
    print('\n')
    
    
    
    listaProdcutos = []
    for pro in (lifestore_file.lifestore_products):
            listaProdcutos.append(pro[0])
    
    busquedas = []
    for pro in(lifestore_file.lifestore_searches):
            busquedas.append(pro[1])
    
    totalProductos = []
    for producto in(listaProdcutos):
            totalProductos.append([producto,busquedas.count(producto),lifestore_file.lifestore_products[producto-1]])
    
    totalProd = len(totalProductos)
    
    
    for total in range(0, totalProd-1):
      for total2 in range(total+1, totalProd):
        if totalProductos[total2][1]>totalProductos[total][1]:
            var = totalProductos[total]
            totalProductos[total] = totalProductos[total2]
            totalProductos[total2] = var
    
    listaProductos = []
    for producto in(lifestore_file.lifestore_products):
      listaProductos.append([producto[0],producto[3],0,producto[1]])
    
    CategoriaProducto = []
    for cantCategoria in(lifestore_file.lifestore_products):
      CategoriaProducto.append(cantCategoria[3])
    
    tipoCategoria = []
    for nomCategoria in(CategoriaProducto):
      if not (tipoCategoria.count(nomCategoria)):
         tipoCategoria.append(nomCategoria)
    
    
    for k in(lifestore_file.lifestore_sales):
      listaProductos[k[1]-1][2] +=1
    
    tamListaProductos = len(listaProductos)
    
    
    for var1 in range(0, tamListaProductos-1):
      for var2 in range(var1+1, tamListaProductos):
        if listaProductos[var2][2]<listaProductos[var1][2]:
            var = listaProductos[var1]
            listaProductos[var1] = listaProductos[var2]
            listaProductos[var2] = var
    
    
    print(".::Listado con los 5 productos con menores ventas::.")
    print('\n')
    for top in range(0, 5):
      print("Producto" + str(totalProductos[top][2][1]))
      print('\n')
      print('\n')
      print("Busquedas totales: " + str(totalProductos[top][1]))
    print(".::Top 10 productos con menos ventas por categoria::.")
    print('\n')
    
    
    for nombreCategoria in(tipoCategoria):
      print("Categoria: "+nombreCategoria)
      cantidad = 0
      for id in(listaProductos):
        print('\n')
        cantidad = cantidad +1
        if cantidad>10:
          print("\n\n")
          break
        else:
          print("Producto "+str(cantidad))
          print("Nombre del producto: " + str(id[3]))
          print('\n')
else:
  print("Datos incorrectos, Intente nuevamente")

