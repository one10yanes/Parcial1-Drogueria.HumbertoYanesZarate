import mysql.connector
from mysql.connector import Error
from sqlite3 import *

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='bdyanes.cqrqixqfc5md.us-east-1.rds.amazonaws.com',
                port=3306,
                user='root',
                password='rootroot',
                db='drogueria'
            )
            if self.conexion.is_connected():
                print ("CONEXION EXITOSA")
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))
            

#----------------------CLIENTES--------------------------#
    def listarClientes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('listar_clientes')
                for result in cursor.stored_results():
                    return result.fetchall()
            except Error as ex:
                print("Error al intentar la conexión a la BD al listar los Usuarios: {0}".format(ex))
                
    def crearClientes(self, clientes):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('crear_cliente', (clientes[0], clientes[1]))
                self.conexion.commit()
                print("¡Cliente Registrado!\n")
            except Error as ex:
                print("Error en BD al crear el cliente: {0}".format(ex))

    def actualizarClientes(self, clientes):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('actualizar_cliente', (clientes[1], clientes[2], clientes[0]))
                self.conexion.commit()
                print("¡Cliente Actualizado!\n")
            except Error as ex:
                print("Error en BD al actualizar el cliente: {0}".format(ex))

    def eliminarClientes(self, idClienteElim):
         if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('eliminar_cliente', (idClienteElim,))
                self.conexion.commit()
                print("¡Cliente eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
#----------------------PRODUCTO--------------------------#    
    def listarProductos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                #cursor.execute("SELECT pr.`productoId`,pr.`codigoProducto`,pr.`nombreProducto`,cl.`nombreCliente` cliente,pro.`nombreProveedor` proveedor FROM productos pr JOIN clientes cl ON pr.`clienteId` = cl.`clienteId` JOIN proveedores pro ON pr.`proveedorId` = pro.`proveedorId`")
                cursor.callproc('listar_productos')
                for result in cursor.stored_results():
                    return result.fetchall()
               
            except Error as ex:
                print("Error al intentar la conexión a la BD al listar los Usuarios: {0}".format(ex))
                
    def crearProductos(self, productos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('crear_producto', (productos[0], productos[1], productos[2], productos[3]))
                self.conexion.commit()
                print("¡Producto Registrado!\n")
            except Error as ex:
                print("Error en BD al crear el producto: {0}".format(ex))

    def actualizarProductos(self, productos):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('actualizar_producto', (productos[1], productos[2], productos[3], productos[4], productos[0]))
                self.conexion.commit()
                print("¡Producto Actualizado!\n")
            except Error as ex:
                print("Error en BD al actualizar el producto: {0}".format(ex))

    def eliminarProductos(self, idProductoElim):
        if self.conexion.is_connected():        
                try:
                    cursor = self.conexion.cursor()
                    cursor.callproc('eliminar_producto',(idProductoElim,))
                    self.conexion.commit()
                    print("¡Producto eliminado!\n")
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))
    
#----------------------PROVEEDORES--------------------------#
    def crearProveedores(self, proveedores):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('crear_proveedor', (proveedores[0], proveedores[1]))
                self.conexion.commit()
                print("¡Proveedor Registrado!\n")
            except Error as ex:
                print("Error en BD al la factura {0}".format(ex))            

    def listarProveedores(self):
        if self.conexion.is_connected():
            try:
                 cursor = self.conexion.cursor()
                 cursor.callproc('listar_proveedores')
                 for result in cursor.stored_results():
                    return result.fetchall()
            except Error as ex:
                print("Error al intentar la conexión a la BD al listar los proveedores: {0}".format(ex))
    
    def eliminarProveedores(self, idProveedorElim):
         if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('eliminar_proveedor', (idProveedorElim,))
                self.conexion.commit()
                print("¡Proveedor Eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
                
    def actualizarProveedores(self, proveedores):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('actualizar_proveedor', (proveedores[1], proveedores[2], proveedores[0]))
                self.conexion.commit()
                print("¡Proveedor Actualizado!\n")
            except Error as ex:
                print("Error en BD al actualizar el proveedor: {0}".format(ex))
                