entero = 10
flotante = 3.14
cadena = "Hola Mundo"
booleano = True

resultado = cadena + "  " +str(entero) + " " +str(flotante) + " " +str(booleano)


"""
Límites de enteros y flotantes en Python

Enteros

Los enteros en Python son números sin decimales. En Python 3, no hay límite de tamaño para los enteros. Sin embargo, en la práctica, el límite está limitado por la cantidad de memoria disponible.

Por ejemplo, si asignamos a una variable un entero con un valor de 10^100, es posible que el programa se bloquee o produzca un error. Esto se debe a que la variable necesitaría una gran cantidad de memoria para almacenar el número.

Flotantes

Los flotantes en Python son números con decimales. En Python 3, los flotantes se almacenan en formato IEEE-754 de doble precisión. Esto significa que pueden representar números con una precisión de hasta 15 dígitos decimales.

Los límites de los flotantes en Python son:

Mínimo: 2.2250738585072014e-308
Máximo: 1.7976931348623157e+308
Estos límites se aplican a todos los flotantes, independientemente de la plataforma o el sistema operativo en el que se esté ejecutando Python.

"""
n =  int(input("Ingresa el numero para la opracion: "))
suma_pares = n * (n + 1)


print("Resultado de la concatenación:", resultado)

print("Suma de los primeros", n, "números pares:", suma_pares)