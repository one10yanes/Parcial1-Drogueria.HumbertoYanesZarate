
#----------------------CLIENTES--------------------------#
def listarClientes(clientes):
    print("\n******Clientes Creados***** \n")
    for cl in clientes:
        datos = "Id: {0} | Nombre Cliente: {1} | Telefono: {2} "
        print(datos.format( cl[0], cl[1], cl[2]))
    print(" ")
    
def crearClientes():
    nomCl = input("Ingrese el nombre del Cliente: ")
    nroTel = input("Ingrese su numero Telefonico: ")
    datos = (nomCl, nroTel)
    return datos

def eliminarClientes(clientes):
    listarClientes(clientes)
    existeCliente=False
    idCl = int(input("Ingrese el ID del cliente a eliminar: "))
    for cl in clientes:
        if cl[0] == idCl:
            existeCliente=True
            break
    if not existeCliente:
        idCl = ""
    return idCl

def actualizarClientes(clientes):
    listarClientes(clientes)
    existeCliente=False
    idClact = int(input("Ingrese el ID del cliente a modificar: "))
    for cl in clientes:
        if cl[0] == idClact:
            existeCliente=True
            break
        
    if existeCliente:
        nomCl = input("Ingrese el nombre nuevo del cliente a modificar: ")
        nroTel = input("Ingrese un nuevo numero Telefonico: ")
        cliente = ( idClact, nomCl, nroTel)
        
    else:
        cliente=None
    
    return cliente

#----------------------PRODUCTOS--------------------------#
def listarProductos(productos):
    print("\n******productos Creados***** \n")
   
    for pr in productos:
        datos = "Id: {0} | Codigo Articulo: {1} | Nombre: {2} | Cliente: {3} | Proveedor: {4} "
        print(datos.format( pr[0], pr[1], pr[2], pr[3], pr[4]))
    print(" ")
    
def crearProductos(clientes, proveedores):
    codPro=int(input("Ingrese el codigo del producto: "))
    nomPro = input("Ingrese el nombre del producto: ")
    listarClientes(clientes)
    print("***De Acuerdo al Id del cliente, ingrese el cliente al que pertenece el producto***")
    idCl = int(input("Ingrese el codigo del cliente: "))
    listarProveedores(proveedores)
    print("***De Acuerdo al Id del proveedor, ingrese el proveedor al que pertenece el producto***")
    idPr = int(input("Ingrese el codigo del proveedor: "))
    datos = (codPro, nomPro, idCl, idPr)
    return datos

def eliminarProductos(productos):
    listarProductos(productos)
    existeProducto=False
    idPr = int(input("Ingrese el ID del producto a eliminar: "))
    for pr in productos:
        if pr[0] == idPr:
            existeProducto=True
            break
    if not existeProducto:
        idPr = ""
    return idPr

def actualizarProductos(productos, clientes, proveedores):
    listarProductos(productos)
    existeProducto=False
    idPrAct = int(input("Ingrese el ID del producto a modificar: "))
    for pr in productos:
        if pr[0] == idPrAct:
            existeProducto=True
            break
    if existeProducto:
        codPro=int(input("Ingrese el codigo del producto: "))
        nomPro = input("Ingrese el nombre del producto: ")
        listarClientes(clientes)
        print("***De Acuerdo al Id del cliente, ingrese el cliente al que pertenece el producto***")
        idCl = int(input("Ingrese el codigo del cliente: "))
        listarProveedores(proveedores)
        print("***De Acuerdo al Id del proveedor, ingrese el proveedor al que pertenece el producto***")
        idPr = int(input("Ingrese el codigo del proveedor: "))
        producto  = (idPrAct, codPro, nomPro, idCl, idPr)
    else:
        producto=None
    
    return producto

#----------------------PROVEEDORES--------------------------#
def listarProveedores(proveedores):
    print("\n******Proveedores Creados***** \n")
   
    for prov in proveedores:
        datos = "Id: {0} | Nombre Proveedor: {1} | Telefono: {2} "
        print(datos.format( prov[0], prov[1], prov[2]))
    print(" ")

def crearProveedores():
    nomPr = input("Ingrese el nombre del Proveedor: ")
    nroPr = input("Ingrese su numero Telefonico: ")
    datos = (nomPr, nroPr)
    return datos

def eliminarProveedores(proveedores):
    listarProveedores(proveedores)
    existeProv=False
    idPr = int(input("Ingrese el ID del cliente a eliminar: "))
    for prov in proveedores:
        if prov[0] == idPr:
            existeProv=True
            break
    if not existeProv:
        idPr = ""
    return idPr

def actualizarProveedores(proveedores):
    listarProveedores(proveedores)
    existeProveedor=False
    idPr = int(input("Ingrese el ID del Proveedor a modificar: "))
    for prov in proveedores:
        if prov[0] == idPr:
            existeProveedor=True
            break
    if existeProveedor:
        nomPr = input("Ingrese el nombre nuevo del proveedor a modificar: ")
        nroPro = input("Ingrese un nuevo numero Telefonico: ")
        proveedor = (idPr, nomPr, nroPro)
    else:
        proveedor=None
    return proveedor
