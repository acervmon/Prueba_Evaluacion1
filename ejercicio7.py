#Ejercicio 7: Añadir Ítems a un Inventario
#Crea una función llamada agregar_item(inventario, item) que reciba una lista de ítems de un inventario y un nuevo ítem a añadir. La función debe añadir el nuevo ítem siempre y cuando no se repita. Si el ítem ya está en el inventario, debe lanzar un error de tipo ValueError.
def agregar_item(inventario, item, cantidad=1, color=""):
    if item in inventario:
        raise ValueError("El ítem ya está en el inventario")
    else:
        inventario.append((item, cantidad, color))

inventario = []
while True:
    item = input("Ingrese un artículo de ropa (o 'salir' para terminar): ").lower()
    if item == "salir":
        break
    cantidad = int(input("Ingrese la cantidad: "))
    color = input("Ingrese el color: ")
    agregar_item(inventario, item, cantidad, color)

print("Inventario:")
for i, (item, cantidad, color) in enumerate(inventario, 1):
    print(f"{i}. {item} ({cantidad}) - {color}")
import matplotlib.pyplot as plt

def mostrar_grafico(inventario):
    nombres = [item[0] for item in inventario]
    cantidades = [item[1] for item in inventario]
    colores = [item[2] for item in inventario]

    plt.bar(nombres, cantidades, color=colores)
    plt.xlabel("Nombre")
    plt.ylabel("Cantidad")
    plt.title("Inventario de ropa")
    plt.show()

mostrar_grafico(inventario)
