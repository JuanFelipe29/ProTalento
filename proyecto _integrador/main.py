import readchar
import os

def limpiar_terminal():
    # Borrar la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_numero_y_limpiar(nombre_participante, numero):
    limpiar_terminal()
    print(f"{nombre_participante} presiona la tecla 'n'")
    print(f"Número actual: {numero}")

nombre_participante = input("Ingrese su nombre para iniciar: \n")
print(f"Bienvenido al Juego {nombre_participante}")


numero = 0

# Bucle infinito
while True:

    # Lee un caracter del teclado
    caracter = readchar.readkey()

    # Imprime el caracter leído
    print(f"{nombre_participante} presiona la tecla {caracter}")

    # Termina el bucle si se presiona la tecla ↑
    if caracter == readchar.key.UP :
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