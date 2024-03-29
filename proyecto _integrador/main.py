import readchar
import os
import random

class Juego:
    def __init__(self, mapa, inicio, final):
        self.mapa = mapa
        self.inicio = inicio
        self.final = final

    def limpiar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def imprimir_numero_y_limpiar(self, nombre_participante, numero):
        self.limpiar_terminal()
        print(f"{nombre_participante} presiona la tecla 'n'")
        print(f"Número actual: {numero}")

    def imprimir_laberinto(self):
        for fila in self.mapa:
            print("".join(fila))

    def main_loop(self, nombre_participante):
        px, py = self.inicio
        numero = 0

        while (px, py) != self.final:
            caracter = readchar.readkey()
            print(f"{nombre_participante} presiona la tecla {caracter}")

            if caracter == readchar.key.UP:
                print("¡Tecla hacia arriba presionada! Terminando el juego.")
                break

            if caracter == 'n':
                numero += 1
                self.imprimir_numero_y_limpiar(nombre_participante, numero)

            if numero == 50:
                print("¡Has alcanzado el número 50! Terminando el juego.")
                break

            self.mapa[py][px] = 'P'
            self.limpiar_terminal()
            self.imprimir_laberinto()

            if (
                caracter == readchar.key.UP
                and py > 0
                and self.mapa[py - 1][px] != '#'
            ):
                self.mapa[py][px] = '.'
                py -= 1
            elif (
                caracter == readchar.key.DOWN
                and py < len(self.mapa) - 1
                and self.mapa[py + 1][px] != '#'
            ):
                self.mapa[py][px] = '.'
                py += 1
            elif (
                caracter == readchar.key.LEFT
                and px > 0
                and self.mapa[py][px - 1] != '#'
            ):
                self.mapa[py][px] = '.'
                px -= 1
            elif (
                caracter == readchar.key.RIGHT
                and px < len(self.mapa[0]) - 1
                and self.mapa[py][px + 1] != '#'
            ):
                self.mapa[py][px] = '.'
                px += 1

class JuegoArchivo(Juego):
    def __init__(self, nombre_archivo):
        path_completo = os.path.join(os.path.dirname(__file__), nombre_archivo)
        mapa, inicio, final = self.leer_archivo(path_completo)
        super().__init__(mapa, inicio, final)

    def leer_archivo(self, path):
        with open(path, 'r') as archivo:
            # La primera línea contiene las coordenadas de inicio y final
            inicio_x, inicio_y, final_x, final_y = map(int, archivo.readline().strip().split())

            # El resto del archivo es el mapa
            mapa = [list(line.strip()) for line in archivo]

        inicio = (inicio_x, inicio_y)
        final = (final_x, final_y)

        return mapa, inicio, final


# Obtener el nombre del participante
nombre_participante = input("Ingrese su nombre para iniciar: \n")
print(f"Bienvenido al Juego {nombre_participante}")

# Crear una instancia de JuegoArchivo para el mapa1.txt
juego_archivo1 = JuegoArchivo(nombre_archivo="map1.txt")

# Iniciar el juego desde la instancia de JuegoArchivo
juego_archivo1.main_loop(nombre_participante)

# Crear una instancia de JuegoArchivo para el mapa2.txt
juego_archivo2 = JuegoArchivo(nombre_archivo="map2.txt")

# Iniciar el juego desde la instancia de JuegoArchivo
juego_archivo2.main_loop(nombre_participante)
