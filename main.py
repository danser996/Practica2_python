from function import *
'''programa principal, trabajo 2 -  lenguajes de programacion 2'''
'''Este programa recibe una frase del usuario y la retorna para ser leida de forma de espiral, 
cada letra tiene un valor y este la asigna e imprime la sumatoria total de los numeros de la 
matriz como un puntaje'''

def main():

    orden_matriz, frase = len_frase()
    matriz_espiral = generar_matriz(orden_matriz, frase)
    copia_matriz_espiral = list(matriz_espiral)
    lista_numerica = matrix_score(copia_matriz_espiral)
    rep_numerica(lista_numerica, orden_matriz)
    score(lista_numerica) 

if __name__ == '__main__':
    main()