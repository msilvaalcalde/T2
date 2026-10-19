laberinto = [
    ["F", 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ["I", 1, 3, 1, 0, 1, 1, 1, 1]
]

filas = len(laberinto)
columnas = len(laberinto[0])

visitado = []
camino = []
ruta = []

for i in range(filas):
    visitado.append([False] * columnas)
    camino.append([0] * columnas)

puntosFinales = 0


def imprimirMatriz(matriz):

    for i in range(len(matriz)):

        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")

        print()


def esValida(fila, columna):

    if fila < 0 or fila >= filas:
        return False

    if columna < 0 or columna >= columnas:
        return False

    if laberinto[fila][columna] == 0:
        return False

    if visitado[fila][columna] == True:
        return False

    return True


def backtracking(fila, columna, puntos):

    global puntosFinales

    if esValida(fila, columna) == False:
        return False

    visitado[fila][columna] = True
    camino[fila][columna] = 1

    ruta.append((fila, columna))

    if laberinto[fila][columna] == 3 or laberinto[fila][columna] == 4:
        puntos = puntos + laberinto[fila][columna]


    # LLEGO A LA META

    if fila == 0 and columna == 0:

        if puntos >= 23:

            puntosFinales = puntos
            return True

        else:

            visitado[fila][columna] = False
            camino[fila][columna] = 0
            ruta.pop()

            return False


    # ARRIBA

    if backtracking(fila - 1, columna, puntos):
        return True


    # DERECHA

    if backtracking(fila, columna + 1, puntos):
        return True


    # ABAJO

    if backtracking(fila + 1, columna, puntos):
        return True


    # IZQUIERDA

    if backtracking(fila, columna - 1, puntos):
        return True


    # RETROCESO

    visitado[fila][columna] = False
    camino[fila][columna] = 0
    ruta.pop()

    return False


def mostrarRecorrido():

    recorrido = []

    for i in range(filas):

        filaNueva = []

        for j in range(columnas):
            filaNueva.append(laberinto[i][j])

        recorrido.append(filaNueva)


    for paso in range(len(ruta)):

        fila = ruta[paso][0]
        columna = ruta[paso][1]

        if laberinto[fila][columna] != "I" and laberinto[fila][columna] != "F":
            recorrido[fila][columna] = "X"


        # Muestra solo algunos avances del recorrido

        if paso % 8 == 0 or paso == len(ruta) - 1:

            print()
            print("RECORRIDO HASTA EL PASO", paso + 1)
            print()

            imprimirMatriz(recorrido)


def crearMatrizSalida():

    salida = []

    for i in range(filas):

        filaSalida = []

        for j in range(columnas):

            if i == 8 and j == 0:

                filaSalida.append("I")

            elif i == 0 and j == 0:

                filaSalida.append("F")

            elif camino[i][j] == 1:

                filaSalida.append("X")

            else:

                filaSalida.append(laberinto[i][j])

        salida.append(filaSalida)

    return salida


print("LABERINTO ORIGINAL")
print()

imprimirMatriz(laberinto)


if backtracking(8, 0, 0):

    print()
    print("RECORRIDO DEL RATON")

    mostrarRecorrido()

    print()
    print("RESULTADO FINAL")
    print()

    print("El raton logro salir.")
    print("Puntos acumulados:", puntosFinales)

    print()
    print("CAMINO FINAL")
    print()

    matrizSalida = crearMatrizSalida()

    imprimirMatriz(matrizSalida)

else:

    print()
    print("RESULTADO FINAL")
    print()

    print("El raton no encontro una salida con 23 puntos o mas.")