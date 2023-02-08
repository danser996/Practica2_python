def ingrese_oracion():
    '''Esta funcion pide al usuario una oracion y verifica si es alfabetica y retornara la frase
    de lo contrario retornara un 0'''
    frase = input('Ingrese la frase que desea visualizar como espiral: ')
    verificacion = frase.replace(' ', '', 100)
    if verificacion.isalpha() == True:
        return frase
    else: 
        print('Oracion no valida, vuelva a intentarlo...')
        return 0

def len_frase():
    '''Esta funcion pide la frase al usuario y la verifica con ayuda de otra funcion,
    la retornara como un titulo y eliminara los espacios, calculara dependiento de la
    longitud de la frase un orden para su matriz, retorna el orden de la matriz cuadrada
    y la frase'''
    frase = ingrese_oracion()
    while frase == 0:
        frase = ingrese_oracion()
    frase = frase.title()
    frase = frase.replace(' ', '', 1000) 
    tamaño = len(frase)
    if tamaño  < 4:
         n = 2
    else: 
        n = int(tamaño ** (1/2) )
        if n * n == tamaño:
            n = n
        else:
            n = n + 1
    frase = frase + '_' * 1000
    return n, frase

def generar_matriz(n, frase):
    '''Esta funcion recibe el orden de la matriz cuadrada y la frase, pocisionara cada 
    caracter de la frase en forma de espiral y la imprimira en pantalla y la retornara'''
    mat_x = [['_' for i in range(n)] for j in range(n)]# Genere una matriz bidimensional inicial, rellena con '_'
    fila = 0
    posicion = 0 #posición actual
    while posicion < n * n:
        # Cada capa se divide en 4 grupos uniformemente, y el número de cada grupo en el número de capa actual
        aux = n - (fila * 2) - 1
        posicion_temporal = posicion
        for j in range(aux):
            # temPos es el valor del primer grupo del bucle actual, y los otros 3 tiempos se calculan de acuerdo con el tamaño de paso num para el llenado
            mat_x[fila][j + fila] = frase[posicion_temporal] #agrega a la posicion 00 lo que hay en j
            mat_x[fila+j][n - fila - 1] = frase[posicion_temporal + aux] #posicion 03 
            mat_x[n - fila - 1][n - fila - j - 1] = frase[posicion_temporal + aux * 2] # posicion 44
            mat_x[n - fila - j - 1][fila] = frase[posicion_temporal + aux * 3]
            #Para números impares, procesamiento especial una vez
            if aux == 2:
                mat_x[n - fila - j - 1][fila + 1] = frase[posicion_temporal + aux * 3 + 1]
                posicion += 1
            posicion_temporal += 1
        fila += 1
        posicion += aux * 4
    print('La frase en espiral dentro de una matriz luce como: ')
    for j in mat_x:
        print(j)
    return mat_x

def matrix_score(arr):
    '''Esta funcion contiene listas con letras que se usaran para determinar el valor
    numero de cada letra y retornara el arreglo con su respectivo valor numerico'''
    lista_0 = [' ', '_', 'Ñ']
    lista_1 = ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U']
    lista_2 = ['D', 'G']
    lista_3 = ['B', 'C', 'M', 'P']
    lista_4 = ['F', 'H', 'V', 'W', 'Y']
    lista_5 = 'K'
    lista_8 = ['J', 'X']
    lista_10 = ['Q', 'Z']

    aux = []
    for i, j in enumerate(arr):
        #print(i, j)
        for k, l in enumerate(j):
            #print(k , l)
            if l.upper() in lista_0:
                aux.insert(k, 0)
            elif l.upper() in lista_1:
                aux.insert(k, 1)
            elif l.upper() in lista_2:
                aux.insert(k, 2)
            elif l.upper() in lista_3:
                aux.insert(k, 3)
            elif l.upper() in lista_4:
                aux.insert(k, 4)
            elif l.upper() in lista_5:
                aux.insert(k, 5)
            elif l.upper() in lista_8:
                aux.insert(k, 8)
            elif l.upper() in lista_10:
                aux.insert(k, 10)
    #print(arreglo3)
    aux.reverse()
    #print(arreglo3)
    return aux
    
def score(arr):
    '''Esta funcion suma los valores que se encuentran en la matriz que recibe y lo imprime
    en pantalla'''
    puntaje = sum(arr)
    print('El puntaje de la frase es: ', puntaje)

def rep_numerica(mat, n):
    '''Esta funcion recibe una lista y un orden de matriz, crea a partir de la lista
    arias listas y las agrega a una nueva lista quedando asi una lista de listas 
    imprimira en pantalla la listas numericas equivalentes a las letras'''
    i = 0
    aux = []
    mat_nuevo = []
    for j in mat:
        aux.append(j)
        i += 1
        if i % n == 0:
            aux.reverse()
            mat_nuevo.append(list(aux))
            aux.clear()
            i = 0

    print('Su representacion numerica es: ')
    for k in mat_nuevo:
        print(k)