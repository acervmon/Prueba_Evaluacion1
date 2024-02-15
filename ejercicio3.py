#Ejercicio 3: Encontrar Palabras Comunes
#Dadas dos listas de palabras, genera una tercera lista con todas las palabras que se repitan en ambas listas, sin repetición en la nueva lista.
lista1 = ["algoritmos", "es", "mi", "asignatura", "favorita"]
lista2 = ["Ruben", "es", "buen", "profesor", "de","algoritmos"]

lista3 = list(set(lista1) & set(lista2))

print(lista3)

lista3 = [word for word in lista1 if word in lista2]

print(lista3)
