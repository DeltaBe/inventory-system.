#crea un diccionario con productos cantidades y precios
#permite al usuario agregar modificar productos o ver el inventario
#muestra el inventario al finalizar con el formato adecuado
inventario=[]
opcion=input('deseas ingresar un producto al invetario (si/no) ').lower().strip()
while opcion=='si':
    cantidad=int(input('digite la cantidad de productos nuevos a agregar al inventario '))
    for indice in range(cantidad):
        nombre_producto=input('introduce el nombre del producto ')
        cantidad_producto=int(input('cuantos productos desea agregar: '))
        precio=float(input('el precio del producto: '))
        productos={'id':indice+1,'Nombre': nombre_producto , 'Cantidad':cantidad_producto , 'precio':precio}
        inventario.append(productos)
    
   
    
    modificar=input('desea modificar algun producto (si/no) ').lower().strip()
    
    if modificar=='si':
        buscar=int(input('digite el producto a buscar mediante el id '))
        producto_buscar=None
        for productos in inventario:
            if buscar == productos.get('id'):
                productos['Nombre']= input('digite el nuevo nombre del producto ')
                productos['Cantidad']=int(input('digite la cantidad de productos '))
                productos['precio']=float(input('digite el nuevo precio '))
                
                producto_buscar=productos
                
                
                
        if producto_buscar !=None:
            print('----------------producto modificado----------------\n')
            print(f'''Id: {producto_buscar.get('id')}
            Nombre: {producto_buscar.get('Nombre')}
            Precio: ${producto_buscar.get('precio'):.2f}
            Cantidad: {producto_buscar.get('Cantidad')}''')
            opcion=input('deseas ingresar algun otro producto (si/no) ').lower().strip()
        else:
            print('producto no encontrado ')
            opcion=input('deseas ingresar algun otro producto (si/no) ').lower().strip()
            
    else:
        opcion=input('deseas ingresar algun otro producto (si/no) ').lower().strip()
        
        
   


print(f'\n--- Inventario Detallado ---')
for producto in inventario:
    print(f'''Id: {producto.get('id')}
    Nombre: {producto.get('Nombre')}
    Precio: ${producto.get('precio'):.2f}
    Cantidad: {producto.get('Cantidad')}''')
        
