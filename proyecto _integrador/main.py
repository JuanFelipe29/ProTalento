import readchar
import os

def limpiar_terminal():
    # Borrar la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_numero_y_limpiar(nombre_participante, numero):
    limpiar_terminal()
    print(f"{nombre_participante} presiona la tecla 'n'")
    print(f"Número actual: {numero}")

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print("".join(fila))

def main_loop(laberinto, inicio, final):
    px, py = inicio
    numero = 0

    while (px, py) != final:

        # Lee un caracter del teclado
        caracter = readchar.readkey()

        # Imprime el caracter leído
        print(f"{nombre_participante} presiona la tecla {caracter}")

        # Termina el bucle si se presiona la tecla ↑
        if caracter == readchar.key.UP:
            print("¡Tecla hacia arriba presionada! Terminando el juego.")
            break

        # Incrementar el número si se presiona la tecla 'n'
        if caracter == 'n':
            numero += 1
            imprimir_numero_y_limpiar(nombre_participante, numero)

        # Rompe el bucle si se alcanza el número 50
        if numero == 50:
            print("¡Has alcanzado el número 50! Terminando el juego.")
            break

        laberinto[py][px] = 'P'
        limpiar_terminal()
        imprimir_laberinto(laberinto)

        if caracter == readchar.key.UP and py > 0 and laberinto[py - 1][px] != '#':
            laberinto[py][px] = '.'
            py -= 1
        elif caracter == readchar.key.DOWN and py < len(laberinto) - 1 and laberinto[py + 1][px] != '#':
            laberinto[py][px] = '.'
            py += 1
        elif caracter == readchar.key.LEFT and px > 0 and laberinto[py][px - 1] != '#':
            laberinto[py][px] = '.'
            px -= 1
        elif caracter == readchar.key.RIGHT and px < len(laberinto[0]) - 1 and laberinto[py][px + 1] != '#':
            laberinto[py][px] = '.'
            px += 1

nombre_participante = input("Ingrese su nombre para iniciar: \n")
print(f"Bienvenido al Juego {nombre_participante}")

# Mapa del laberinto
laberinto_str = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

# Convertir el mapa a una matriz de caracteres
laberinto = [list(fila) for fila in laberinto_str.split("\n")]

# Coordenadas de inicio y final
inicio = (0, 0)
final = (len(laberinto[0]) - 1, len(laberinto) - 1)

# Iniciar el juego
main_loop(laberinto, inicio, final)
