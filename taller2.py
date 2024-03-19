import os
import random
# funcion para limpiar el terminal
def clear_screen(opcion):
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():  # funcion que me muestra el menu de opciones
    print("\n\nMenú de Gestión de Inventario")
    print("1. Agregar producto")
    print("2. Simular consumo")
    print("3. Mostrar reporte de inventario")
    print("4. Calcular Inventario total")
    print("5. Verificar alertas de reorden")
    print("6. Reabastecer producto")
    print("7. Salir")
    
"""simula el consumo de productos de un inventario"""
def agregar_producto(inventario):
    while True:
    nombre_producto = input("Ingrese el nombre del nuevo producto: ")
    if nombre_producto in inventario:
        print("El producto ya existe en el inventario. Por favor, ingrese un nombre diferente.")
            else:
        break
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad inicial del producto: "))
            if cantidad <= 0:                                    
                raise ValueError("La cantidad inicial debe ser un número entero positivo.")
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico positivo para la cantidad.")
    while True:
        try:
            umbral = int(input("Ingrese el umbral minimo del producto: "))
            if umbral <= 0:                                           
                raise ValueError("El umbral mínimo debe ser un número entero positivo.")
            break 
        except ValueError:
            print("Por favor, ingrese un valor numérico numérico positivo para el umbral minimo.")
    inventario[nombre_producto] = [cantidad, umbral]
    print(f"\nProducto '{nombre_producto}' agregado al inventario.")

# funcion para simular el consumo del inventario
def simular_consumo(inventario):
    if not inventario:
        print("\033[94m El inventario está vacío.\033[0m") # si no hay nada en el diccionario se muestra el mensaje
        return

    for producto, detalles in inventario.items():
        cantidad_disponible, _ = detalles
        if cantidad_disponible == 0:
            print(f"\033[91m No hay suficiente {producto} en el inventario.\033[0m")
            continue                      # Continuar con el siguiente producto si el actual está agotado
        cantidad_consumida = min(random.randint(1, cantidad_disponible), cantidad_disponible) # Limita el valor aleatorio a la cantidad disponible
        print(f"Consumo simulado de {cantidad_consumida} unidades del producto '{producto}'.")
        inventario[producto][0] -= cantidad_consumida

    print("Inventario actualizado después del consumo:")
 # funcion que me muestra lo que hay en el inventario
def mostrar_reporte(inventario):
    print("Reporte de inventario:")
    print("Estado actual del inventario\n\n")
    print("{:<20} {:<10} {:<10}".format("\033[93mProducto", "Cantidad", "Umbral\033[0m"))
    print("_"*40)
    for producto, detalle in inventario.items():  
        if inventario[producto][0] < inventario[producto][1]:
            print("\033[91m{:<20} {:<10} {:<10}\033[0m".format(producto, detalle[0], detalle[1]))      
        else:
            print("{:<20} {:<10} {:<10}".format(producto, detalle[0], detalle[1]))
 # funcion para sumas las cantidades de cada producto del inventario   
def calcular_inventario_total(inventario):
    total = sum(detalles[0] for detalles in inventario.values()) # accede al primer elemento de cada tupla que es la cantidad disponible y la suma
    print(f"El valor total del inventario es: {total}")
# funcion para verificar las cantidades que estan por debajo del humbral
def verificar_alertas_reorden(inventario):
    print("Verificación de alertas de reorden:")
    for producto, detalles in inventario.items():
        cantidad_disponible, umbral = detalles
        if cantidad_disponible < umbral:
            print(f"\n\033[91m¡Alerta de reorden! El producto '{producto}' está por debajo del umbral.\033[0m")
# funcion para reabastecer el inventario
def reabastecer_producto(inventario):
    producto = input("Ingrese el nombre del producto a reabastecer: ")
    if producto in inventario:
        cantidad = int(input("Ingrese la cantidad a reabastecer: "))
        inventario[producto][0] += cantidad
        print(f"Se han reabastecido {cantidad} unidades del producto '{producto}'.")
    else:
        print("\033[91m El producto especificado no existe en el inventario.\033[0m")

# Inventario inicial
inventario = {"tornillos":[1000,500],
"placas":[300, 200],
"cables":[800, 300],
}


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción del menú: ")
    clear_screen(opcion)
    if opcion == '1':
        agregar_producto(inventario)
    elif opcion == '2':
        simular_consumo(inventario)
    elif opcion == '3':
        mostrar_reporte(inventario)
    elif opcion == '4':
        calcular_inventario_total(inventario)
    elif opcion == '5':
        verificar_alertas_reorden(inventario)
    elif opcion == '6':
        reabastecer_producto(inventario)
    elif opcion == '7':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")
        
