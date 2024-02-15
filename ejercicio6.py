#Ejercicio 6: Separar Personajes de Videojuegos
#Crea una función que tome una lista de personajes de videojuegos y devuelva dos listas ordenadas: la primera con personajes humanos y la segunda con personajes no humanos.
def separar_personajes(personajes):
    humanos = []
    no_humanos = []

    for personaje in personajes:
        if isinstance(personaje, str):
            if personaje.lower() in ["alejandra", "sara", "maria isabel", "ruben"]:
                humanos.append(personaje)
            else:
                no_humanos.append(personaje)
        else:
            no_humanos.append(personaje)

    return sorted(humanos), sorted(no_humanos)

# Prueba de la función
personajes = ["Alejandra", "Sara", "dinosaurio", "cabra", "Maria Isabel", "Ruben", "llama"]
humanos, no_humanos = separar_personajes(personajes)
print("Personajes humanos:", humanos)
print("Personajes no humanos:", no_humanos)

# Insertar personaje en la terminal
nuevo_personaje = input("Inserte un nuevo personaje: ")

# Verificar si es humano o no
if nuevo_personaje.lower() in ["alejandra", "sara", "maria isabel", "ruben"]:
    print(f"{nuevo_personaje} es humano.")
else:
    print(f"{nuevo_personaje} no es humano.")
