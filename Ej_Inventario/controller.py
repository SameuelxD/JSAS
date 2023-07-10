import modules
import os
if __name__ == "__main__":
    active=True
    confirm1=True
    confirm2=True
    products={}
    providers={}
    shopping={}
    sales={}
    customers={}
    while(active):
        os.system("clear")
        print('+','-'*45,'+')
        print("|{:^20}{}{:^23}|".format(' ','MENU',' '))
        print('+','-'*45,'+')
        print("      1. REGISTRAR CODIGO DEL PRODUCTO.\n      2. REGISTRAR NOMBRE DEL PRODUCTO.\n      3. STOCK MINIMO.\n      4. STOCK MAXIMO.\n      5. ESTADO.\n      6. REGISTRAR PROVEEDOR.\n      7. REGISTRAR COMPRAS.\n      8. REGISTRAR CLIENTES.\n      9. REGISTRAR VENTAS.\n      10. INFORMACION.\n      11. SALIR.")
        print('+','-'*45,'+')
        option=int(input("Digite la opcion --> "))
        if(option == 1):
            passive=True
            while(passive):
                os.system("clear")
                modules.AddCode(products)   #1. REGISTRAR CODIGO DEL PRODUCTO.
                modules.SaveInformacion(products)
                passive=bool(input("Digite un caracter AlphaNumerico para Ingresar otro Codigo de un Producto o Presione Enter para volver al Menu Principal --> "))
        elif(option == 2):
            passive=True
            while(passive):
                os.system("clear")
                modules.AddName(products)   #2. REGISTRAR NOMBRE DEL PRODUCTO.
                modules.SaveInformacion(products)
                passive=bool(input("Digite un caracter AlphaNumerico para Ingresar otro Nombre de un Producto o Presione Enter para volver al Menu Principal --> "))
        elif((option == 3)and(confirm1)):
            os.system("clear")
            stockMin=int(input("Ingrese la Cantidad Minima de Stock para todos los Productos del Inventario: "))                # 3. STOCK MINIMO.
            input("Presione una tecla para continuar... ")  
            confirm1=False
        elif(( option== 4)and(confirm2)):
            os.system("clear")
            stockMax=int(input("Ingrese la Cantidad Maxima de Stock para todos los Productos del Inventario: "))                #4. STOCK MAXIMO.
            input("Presione una tecla para continuar... ")
            confirm2=False
        elif(option == 5):
            passive=True
            while(passive):
                os.system("clear")
                modules.CheckProductsStatus(products)   #5. Estado Disponibilidad
                modules.SaveInformacion(products) 
                passive=bool(input("Digite un caracter AlphaNumerico para Verificar Disponibilidad de un Producto o Presione Enter para volver al Menu Principal --> "))
        elif(option == 6):
            passive=True
            while(passive):
                os.system("clear")
                modules.AddProviders(providers)     #6. REGISTRAR PROVEEDOR.
                modules.SaveInformacion(providers)
                passive=bool(input("Digite un caracter AlphaNumerico para Ingresar otro Proveedor o Presione Enter para volver al Menu Principal --> "))
        elif(option == 7):
            passive=True
            while(passive):
                os.system("clear")
                modules.AddShopping(shopping,providers,products)    #7. REGISTRAR COMPRAS.
                modules.SaveInformacion(shopping)
                passive=bool(input("Digite un caracter AlphaNumerico para Ingresar mas Compras o Presione Enter para volver al Menu Principal --> "))
        elif(option == 8):
            passive=True
            while(passive):
                os.system("clear")
                modules.AddCustomers(customers)         #8. REGISTRAR CLIENTES.
                modules.SaveInformacion(customers)
                passive=bool(input("Digite un caracter AlphaNumerico para Ingresar mas Clientes o Presione Enter para volver al Menu Principal --> "))
        elif(option == 9):
            passive=True
            while(passive):
                os.system("clear")
                modules.AddSales(sales,customers,products,shopping)     #9. REGISTRAR VENTAS.
                modules.SaveInformacion(sales)
                passive=bool(input("Digite un caracter AlphaNumerico para Ingresar mas Ventas o Presione Enter para volver al Menu Principal --> "))
        elif(option == 10):
            os.system("clear")
            print(f"Productos: {products}\n\n\nProveedores: {providers}\n\n\nCompras: {shopping}\n\n\nVentas: {sales}\n\n\nClientes: {customers}\n\n\n")
            input("Presione una tecla para continuar... ")    #10. INFORMACION     
        elif(option == 11):
            os.system("clear")
            print("CORTANDO EJECUCION")
            input("Presione una tecla para continuar... ")     #11. SALIR
            active=False



            


