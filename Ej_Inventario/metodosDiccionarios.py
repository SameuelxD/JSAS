import os

diccionario = {
    'nombre': 'Juan Jose',
    'apellidos': 'Galan Mendez',
    'ciudad': 'Bucaramanga',
    'edad': 28,
    'empleado': False
}


#------------------------------------------------------------------- METODO UPDATE -------------------------------------------------------------------------------------

#El metodo .update(), se utiliza para actualizar o agregar elementos a un diccionario. Este metodo acepta un diccionario como argumento y luego agrega o actualiza los elementos en el diccionario original.  dict_nombre.update(dictionario)

diccionario2 = {
    'profesion': 'Ingeniero Civil',
    'estado': 'Estudiante',
    'año': 1994
}

# En este caso se agrega la informacion del diccionario2 dentro de diccionario, actualizando la informacion de este mismo

os.system('clear')
diccionario.update(diccionario2)
print('METODO UPDATE')
print(diccionario)

#Tambien es posible definir la informacion o el diccionario que se desea agregar dentro del metodo mismo como se mostrara a contianuacion: 
diccionario.update({'universidad': 'UIS'})
print(diccionario)

#Adicionalmente el metodo .update() tambien permite actualizar los valores de las claves ya existentes dentro del diccionario 
diccionario.update({'nombre': 'Edwin Julian'})
print(diccionario)
os.system('sleep 5')

#------------------------------------------------------------------ METODO KEYS ----------------------------------------------------------------------------------------

#El metodo .keys() muestra las llaves(keys) que conforman a un diccionario. Tambien permite iterar los elementos de un diccionario.

claves = diccionario.keys()
print('METODOS KEYS')
print(claves)
os.system('sleep 10')

#----------------------------------------------------------------- METODO GET ------------------------------------------------------------------------------------------

#El metodo .get() permite buscar o llamar el valor correspondiente a las llaves dentro de un diccionario. En caso de no encontrar la llave arroja el valor 'None' 

os.system('clear')
buscar = diccionario.get('nombre')
print('METODO GET')
print(buscar)
os.system('sleep 10')
 
#------------------------------------------------------------------- METODO CLEAR --------------------------------------------------------------------------------------

#Elimina todos los datos dentro del diccionario. 

#os.system('clear')
#eliminar = diccionario.clear()
#print('METODO CLEAR')
#print(eliminar)
#os.system('sleep 10') 

#------------------------------------------------------------------ METODO POP -----------------------------------------------------------------------------------------

# Permite eliminar un valor, definiendo como parametro la llave del elemento que se desea eliminar

os.system('clear')
diccionario.pop('edad')
print('METODO POP')
print(diccionario)
os.system('sleep 10')

#----------------------------------------------------------------- METODOS ITEMS ---------------------------------------------------------------------------------------

# El metodo .items() transforma el diccionario en un elemento que permite iterar dicho diccionarios, o lo convierte en un diccionario iterable

os.system('clear')
diccionarioIterable = diccionario.items()
print('METODO ITEMS')
print(diccionarioIterable)
print(diccionario)
os.system('sleep 10')
