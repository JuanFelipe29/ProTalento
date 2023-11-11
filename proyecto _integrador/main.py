import readchar

nombre_participante = input("Ingrese su nombre para iniciar: \n")
print(f"Bienvenido al Juego {nombre_participante}")

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