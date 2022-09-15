from itertools import product
import funciones
from conexion import DAO


#--------------MENU PRINCIPAL--------------------# 
def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("====================DROGUERIA LA PRINCIPAL====================")
            print("1.- CLIENTES")
            print("2.- PRODUCTOS")
            print("3.- PROVEEDORES")
            print("0.- SALIR")
            print("========================================================")
            opcion = int(input("SELECCIONE UNA OPCION: "))
            
            if opcion < 0 or opcion > 3:
                print("OPCION INCORRECTA, INTENTE NUEVAMENTE...")
            elif opcion == 0:
                continuar = False
                print("¡GRACIAS POR USAR ESTE SERVICIO!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcionMP(opcion)

#--------------DISPARADOR MENU PRINCIPAL----------------------# 
def ejecutarOpcionMP(opcion):
#--------------OPCION CLIENTES---------------------#
    if opcion == 1:
        continuar= True
        while(continuar):
            opcionCorrecta = False
            while(not opcionCorrecta):
                print("====================MODULO CLIENTES====================")
                print("1.- LISTAR CLIENTES")
                print("2.- CREAR CLIENTES")
                print("3.- ACTUALIZAR CLIENTES")
                print("4.- ELIMINAR CLIENTES")
                print("0.- SALIR")
                print("==============================================================")
                opcion = int(input("SELECCIONE UNA OPCION: "))
                if opcion < 0 or opcion > 4:
                    print("OPCION INCORRECTA, INTENTE NUEVAMENTE...")
                elif opcion == 0:
                    continuar = False
                    break
                else:
                    opcionCorrecta = True
                    subMenuCliente(opcion)
                    
#--------------OPCION PRODUCTOS--------------------#
    if opcion == 2:
        continuar = True
        while(continuar):
            opcionCorrecta = False
            while(not opcionCorrecta):
                print("====================MODULO PRODUCTOS====================")
                print("1.- LISTAR PRODUCTOS")
                print("2.- CREAR PRODUCTOS")
                print("3.- ACTUALIZAR PRODUCTOS")
                print("4.- ELIMINAR PRODUCTOS")
                print("0.- REGRESAR")
                print("==============================================================")
                opcion = int(input("SELECCIONE UNA OPCION: "))
                if opcion < 0 or opcion > 4:
                    print("OPCION INCORRECTA, INTENTE NUEVAMENTE...")
                elif opcion == 0:
                    continuar = False
                    break
                else:
                    opcionCorrecta = True
                    subMenuProducto(opcion)
                    
#--------------OPCION PROVEEDORES------------------#            
    if opcion == 3:
        continuar = True
        while(continuar):
            opcionCorrecta = False
            while(not opcionCorrecta):
                print("==================MODULO PROVEEDORES====================")
                print("1.- LISTAR PROVEEDORES")
                print("2.- CREAR PROVEEDORES")
                print("3.- ACTUALIZAR PROVEEDORES")
                print("4.- ELIMINAR PROVEEDORES")
                print("0.- REGRESAR")
                print("==============================================================")
                opcion = int(input("SELECCIONES UNA OPCION: "))
                if opcion < 0 or opcion > 4:
                    print("OPCION INCORRECTA, INTENTE NUEVAMENTE...")
                elif opcion == 0:
                    continuar = False
                    break
                else:
                    opcionCorrecta = True
                    subMenuProveedor(opcion)        


#--------------DISPARADOR SUBMENU CLIENTES--------------------#                        
def subMenuCliente(opcion):
    dao = DAO()
#--------------OPCION LISTAR CLIENTES--------------#
    if opcion == 1:
        try:
            clientes = dao.listarClientes()
            if len(clientes) > 0:
                funciones.listarClientes(clientes)
            else:
                print("NO SE ENCONTRARON CLIENTES CREADOS...")
        except:
            print("OCURRIO UN ERROR...")
            
#--------------OPCION CREAR CLIENTES---------------#
    elif opcion == 2:
        clNuevo = funciones.crearClientes()
        try:
            dao.crearClientes(clNuevo)
        except:
            print("OCURRIO UN ERROR...")
            
#--------------OPCION ACTUALIZAR CLIENTES----------#
    elif opcion == 3:
        try:
            clientes=dao.listarClientes()
            if len(clientes) > 0:
                cliente=funciones.actualizarClientes(clientes)
                if cliente:
                    dao.actualizarClientes(cliente)
                else:
                    print("ID DEL CLIENTE A ACTUALIZAR NO EXISTE...") 
            else:
                print("NO SE ENCONTRARON CLIENTES CREADOS...")             
        except:
            print("OCURRIO UN ERROR...")

#--------------OPCION ELIMINAR CLIENTES------------#
    elif opcion == 4:
        try:
            clientes=dao.listarClientes()
            if len(clientes) > 0:
                idEliminar=funciones.eliminarClientes(clientes)
                if not(idEliminar==""):
                    dao.eliminarClientes(idEliminar)
                else:
                    print("ID DEL CLIENTE NO EXISTE...")
            else:
                print("NO SE ENCONTRARON CLIENTES CREADOS...")             
        except:
            print("OCURRIO UN ERROR...")
                                  
#--------------DISPARADOR SUBMENU PRODUCTOS-----------------#      
def subMenuProducto(opcion):
    dao = DAO()
#--------------OPCION LISTAR PRODUCTOS--------------#
    if opcion == 1:
        try:
            productos = dao.listarProductos()
            if len(productos) > 0:
                funciones.listarProductos(productos)
            else:
                print("NO SE ENCONTRARON PRODUCTOS CREADOS...")
        except:
            print("OCURRIO UN ERROR...")

#--------------OPCION CREAR PRODUCTOS---------------#
    elif opcion == 2:
        cl=dao.listarClientes()
        pr=dao.listarProveedores()
        try:
            if len(cl) > 0 and len(pr) > 0:
                prNuevo = funciones.crearProductos(cl,pr)
                if prNuevo:
                    dao.crearProductos(prNuevo)
            else: 
                print("NO SE ENCONTRARON CLIENTES O PROVEEDORES CREADOS...")
        except:
            print("OCURRIO UN ERROR...")
      
#--------------OPCION ACTUALIZAR PRODUCTOS----------#
    elif opcion == 3:
        try:
            productos=dao.listarProductos()
            cl=dao.listarClientes()
            pr=dao.listarProveedores()
            if len(productos) > 0 and len(cl)>0 and len(pr)>0:
                actualizarProducto=funciones.actualizarProductos(productos,cl,pr)
                if actualizarProducto:
                    dao.actualizarProductos(actualizarProducto)
                else:
                    print("ID PRODUCTO A ACTUALIZAR NO EXISTE...") 
            else:
                print("NO SE ENCONTRARON PRODUCTOS, CLIENTE O PROVEEDORES CREADOS...")             
        except:
            print("OCURRIO UN ERROR...")

#--------------OPCION ELIMINAR PRODUCTOS------------#
    elif opcion == 4:
        try:
            productos=dao.listarProductos()
            if len(productos) > 0:
                idEliminar=funciones.eliminarProductos(productos)
                if not(idEliminar==""):
                    dao.eliminarProductos(idEliminar)
                else:
                    print("ID PRODUCTO NO ENCONTRADO..")
            else:
                print("NO SE ENCONTRARON PRODUCTOS CREADOS...")             
        except:
            print("OCURRIO UN ERROR...")

#--------------DISPARADOR SUBMENU PROVEEDORES--------------------# 
def subMenuProveedor(opcion):
    dao = DAO()
#--------------OPCION LISTAR PROVEEDORES--------------#
    if opcion == 1:
        try:
            proveedores = dao.listarProveedores()
            if len(proveedores) > 0:
                funciones.listarProveedores(proveedores)
            else:
                print("NO SE ENCONTRARON PROVEEDORES CREADOS...")
        except:
            print("OCURRIO UN ERROR...")
            
#--------------OPCION CREAR PROVEEDORES---------------#
    elif opcion == 2:
        prNuevo = funciones.crearProveedores()
        try:
            dao.crearProveedores(prNuevo)
        except:
            print("OCURRIO UN ERROR...")   

#--------------OPCION ACTUALIZAR PROVEEDORES----------#
    elif opcion == 3:
        try:
            proveedores=dao.listarProveedores()
            if len(proveedores) > 0:
                proveedor=funciones.actualizarProveedores(proveedores)
                if proveedor:
                    dao.actualizarProveedores(proveedor)
                else:
                    print("ID PROVEEDOR A ACTUALIZAR NO EXISTE..") 
            else:
                print("NO SE ENCONTRARON PROVEEDORES..")             
        except:
            print("OCURRIO UN ERROR...")

#--------------OPCION ELIMINAR PROVEEDORES------------#
    elif opcion == 4:
        try:
            proveedores=dao.listarProveedores()
            if len(proveedores) > 0:
                idEliminar=funciones.eliminarProveedores(proveedores)
                if not(idEliminar==""):
                    dao.eliminarProveedores(idEliminar)
                else:
                    print("ID PROVEEDOR NO EXISTE...")
            else:
                print("NO SE ENCONTRARON PROVEEDORES...")             
        except:
            print("OCURRIO UN ERROR...")

menuPrincipal()
