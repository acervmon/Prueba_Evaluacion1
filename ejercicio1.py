#Ejercicio 1: Extracción de Información de una Receta
#Al extraer texto de un sitio web de recetas, obtuviste una cadena de texto corrupta y al revés. Parece contener el nombre de una receta y la cantidad de calorías. Formatea la cadena para conseguir una estructura como la siguiente:
#La receta de Ale contiene [Número] calorías.
#Ayuda:Para voltear una cadena rápidamente utilizando slicing: cadena[::-1]
import webbrowser

cadena = "alliniav ed etebros noc somtiroglA y sotaD ed atraT"
nombre_receta = cadena[::-1]

calorias = 1500
chef = "Chef Alejandra Cervantes"

# Diccionario de nutrientes
nutrientes = {
    "Creatividad": 200,
    "Carbohidratos": 250,
    "Proteina": 45,
    "Fibra": 5,
    "Alegria": 1000
}

# Formatea la cadena de salida
formatted_string = "La receta de {} preparada por {} contiene {} calorías. Los nutrientes son:\n".format(nombre_receta, chef, calorias)

# Añade los nutrientes y sus cantidades a la cadena de salida
for nutriente, cantidad in nutrientes.items():
    formatted_string += "- {}: {}\n".format(nutriente, cantidad)

# Abre una página web de recetas en el navegador predeterminado
webbrowser.open("https://www.annarecetasfaciles.com/files/tarta-de-manzana-muy-facil-3.jpg")

# Imprime la cadena de salida
print(formatted_string)
