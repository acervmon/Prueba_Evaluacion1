from queue import PriorityQueue
import sys

# Agregar un método para dibujar un gráfico de dificultad
def print_difficulty_graph(difficulty):
    for i in range(difficulty):
        print("■", end="")
    print(" " + str(difficulty), end="")
    for i in range(50 - difficulty):
        print(".", end="")
    print("")

# Agregar misiones a la cola con su dificultad
missions_queue = PriorityQueue()
missions_queue.put((17, "Misión 1"))
missions_queue.put((4, "Misión 2"))
missions_queue.put((50, "Misión 3"))
missions_queue.put((1, "Misión 4"))
missions_queue.put((20, "Misión 5"))

# Mostrar las misiones en orden de dificultad con un gráfico
while not missions_queue.empty():
    difficulty, mission = missions_queue.get()
    print_difficulty_graph(difficulty)
    print(mission)
