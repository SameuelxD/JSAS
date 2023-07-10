import os
import json
def AddCode(myProducts:dict):
    codeProduct=int(input("Ingrese el Codigo del Producto a Agregar: "))
    while (myProducts.get(codeProduct)):
        print("¡ERROR! El Codigo del Producto ya fue Agregado... ")
        codeProduct=int(input("Ingrese el Codigo del Producto a Agregar: "))
    product= {
        codeProduct:{
            "Codigo-Producto": codeProduct,
        }
    }
    myProducts.update(product)
def AddName(myProducts:dict):
    codeProduct=int(input("Ingrese el Codigo del Producto para Agregar su Nombre: "))
    confirm=True
    while ((myProducts.get(codeProduct))and(confirm)):
        nameProduct=input(f"Ingrese el Nombre del Producto para el Codigo: ")
        myProducts[codeProduct]["Nombre-Producto"]=nameProduct
        confirm=False
def AddProviders(myProviders:dict):
    codeSupplier=int(input("Ingrese el Codigo del Proveedor a Agregar: "))
    while (myProviders.get(codeSupplier)):
        print("¡ERROR! El Codigo del Proveedor ya fue Agregado... ")
        codeSupplier=int(input("Ingrese el Codigo del Proveedor a Agregar: "))            
    nameSupplier=input("Ingrese el Nombre del Proveedor para Agregar: ")
    supplier={
        codeSupplier:{
            "Codigo-Proveedor": codeSupplier,
            "Nombre-Proveedor": nameSupplier
        }
    }
    myProviders.update(supplier)
def AddShopping(myShopping:dict,myProviders:dict,myProducts:dict):
    referenceShopping=int(input("Ingrese la Referencia de Compra de la Facturacion: "))
    confirm=True
    while (myShopping.get(referenceShopping)):
        print("¡ERROR! El numero de Referencia ya fue Agregado... ")
        referenceShopping=int(input("Ingrese la Referencia de Compra de la Facturacion: "))
    dateShopping=input("Ingrese la Fecha de la Compra: ")
    undProductValue=float(input("Ingrese el Valor por Unidad para Compra del Producto: "))
    codeSupplier=int(input("Ingrese el Codigo del Proveedor para la Compra de Productos al Inventario: "))
    while (myProviders.get(codeSupplier)and(confirm)):
        codeProduct=int(input("Ingrese el Codigo del Producto para la Compra del Inventario: "))
        while (myProducts.get(codeProduct)and(confirm)):
            inventoryAdd=int(input("Ingrese la Cantidad Comprada del Producto para Agregarla al Inventario: "))
            while(inventoryAdd<1):
                print("¡ERROR! La Cantidad Comprada no es logica") 
                inventoryAdd=int(input("Ingrese la Cantidad Comprada del Producto para Agregarla al Inventario: "))
            try:
                unitsAvailable=myProducts[codeProduct]["Unidades-Disponibles"]
                productUnits=(unitsAvailable)+(inventoryAdd)
                myProducts[codeProduct]["Unidades-Disponibles"]=productUnits
            except KeyError:
                productUnits=inventoryAdd    
                myProducts[codeProduct]["Unidades-Disponibles"]=productUnits
            purchaseValue=(undProductValue)*(inventoryAdd)
            shopping={
                referenceShopping:{
                    "Referencia-Compra": referenceShopping,
                    "Codigo-Producto": codeProduct,
                    "Codigo-Proveedor": codeSupplier,
                    "Fecha-Compra": dateShopping,
                    "Valor-Unidad": undProductValue,
                    "Valor-Compra": purchaseValue,
                    "Cantidad-Compra": inventoryAdd
                }
            }
            myShopping.update(shopping)  
            confirm=False
def CheckProductsStatus(myProducts:dict):
    codeProduct=int(input("Ingrese el Codigo del Producto para Verificar el Inventariado: "))
    confirm=True
    while(myProducts.get(codeProduct)and(confirm)):
        unitsAvailable=myProducts[codeProduct]["Unidades-Disponibles"]
        if(unitsAvailable>0):
            print(f"El Producto con Codigo: {codeProduct},tiene una disponibilidad de {unitsAvailable} unidades Disponibles.")
        else:
            print("El producto no tiene unidades Disponibles actualmente.")
        confirm=False
def AddCustomers(myClients:dict):
    customerCode=int(input("Ingrese el Codigo del Cliente para Crear Cuenta en su Facturacion en Ventas: "))
    while (myClients.get(customerCode)):
        print("¡ERROR! El Codigo del Cliente ya fue Agregado... ")
        customerCode=int(input("Ingrese el Codigo del Cliente para Crear Cuenta en su Facturacion en Ventas: "))
    clientName=input("Ingrese el Nombre del Cliente: ")
    customer={
        customerCode:{
            "Codigo-Cliente": customerCode,
            "Nombre-Cliente": clientName
        }
    }
    myClients.update(customer)
def AddSales(mySales:dict,myClients:dict,myProducts:dict,myShopping:dict):
    salesReference=int(input("Ingrese la Referencia de Venta de la Facturacion: "))
    confirm=True
    while (mySales.get(salesReference)):
        print("¡ERROR! El numero de Referencia ya fue Agregado... ")
        salesReference=int(input("Ingrese la Referencia de Venta de la Facturacion: "))
    dateSales=input("Ingrese la Fecha de la Venta: ")
    customerCode=int(input("Ingrese el Codigo del Cliente para la Facturacion: "))
    while (myClients.get(customerCode)and(confirm)):
        undProductValue=float(input("Ingrese el Valor por Unidad para Venta del Producto: "))
        codeProduct=int(input("Ingrese el Codigo del Producto para la Venta en la Facturacion: "))
        while (myProducts.get(codeProduct)and(confirm)):
            discountInventory=int(input("Ingrese la Cantidad Vendida del Producto para Descontarla del Inventario: ")) 
            unitsAvailable=myProducts[codeProduct]["Unidades-Disponibles"]
            productUnits=(unitsAvailable)-(discountInventory)
            while (productUnits<0):
                print("¡ERROR! La Cantidad Vendida del Producto no esta Disponible en el Inventario")
                discountInventory=int(input("Ingrese la Cantidad Vendida del Producto para Descontarla del Inventario: "))
                productUnits=(unitsAvailable)-(discountInventory)
            purchaseValue=(undProductValue)*(discountInventory)
            clientName=myClients[customerCode]["Nombre-Cliente"]
            myProducts[codeProduct]["Unidades-Disponibles"]=productUnits
            sales={
                salesReference:{
                    "Referencia-Venta": salesReference,
                    "Codigo-Producto": codeProduct,
                    "Fecha-Venta": dateSales,
                    "Codigo-Cliente": customerCode,
                    "Nombre-Cliente": clientName,
                    "Valor-Unidad": undProductValue,
                    "Valor-Compra": purchaseValue,
                    "Cantidad-Vendida": discountInventory
                }
            }
            mySales.update(sales)   
            confirm=False
def SaveInformacion(data):
    try:
        with open("datos", "r") as archivo_existente:
            datos_existentes = json.load(archivo_existente)
    except FileNotFoundError:
        datos_existentes = []
    datos_existentes.append(data)
    with open("datos.json", "w") as archivo:
        json.dump(datos_existentes, archivo, indent=4)
