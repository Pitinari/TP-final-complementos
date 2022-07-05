import random
import math
import numpy as np

def randomrango(minimo, maximo):
    """
    randomrango :: (int, int) -> float
    Parametros:
    minimo: minimo del rango
    maximo: maximo del rango
    Calcula un numero aleatorio entre el minimo y el maximo
    """
    delta = maximo-minimo
    numero = minimo + random.uniform(0, 1) * delta
    return numero


def randomize_position (lista_nodos, ancho, alto):
    """
    randomrango :: (list(strings), int, int) -> dict(string: (float, float))
    Parametros:
    lista_nodos:    Lista de los nombres de los nodos
    ancho:          Ancho del canvas
    alto:           Alto del canvas
    Mapea en un dicionario, cada nombre con un punto aleatorio del canvas
    """
    posiciones = {}
    anchomin = -ancho/2
    anchomax = ancho/2
    altomin = -alto/2
    altomax = alto/2
    for nodo in lista_nodos:
        posiciones[nodo] = np.array([randomrango( anchomin , anchomax),randomrango( altomin , altomax)])
    return posiciones

def calculo_repulsion(nodoa, nodob, cantNodos, area, C):
    """
    calculo_repulsion :: ((float, float), (float, float), int, int, float) -> (float, float))
    Parametros:
    nodoa:      Coordenadas del nodo A
    nodob:      Coordenadas del nodo B
    cantNodos:  Cantidad de nodos
    area:       Area del canvas           
    C:          Constante de repulsion
    Calcula la fuerza de repulsion entre dos nodos
    """
    delta = nodob - nodoa
    dist = np.linalg.norm(delta)
    k = -math.sqrt( area / cantNodos ) * C
    fuerza = k*k / dist
    return delta*(fuerza/dist)

def calculo_atraccion(nodoa, nodob, cantNodos, area, C):
    """
    calculo_atraccion :: ((float, float), (float, float), int, int, float) -> (float, float))
    Parametros:
    nodoa:      Coordenadas del nodo A
    nodob:      Coordenadas del nodo B
    cantNodos:  Cantidad de nodos
    area:       Area del canvas           
    C:          Constante de atraccion
    Calcula la fuerza de atraccion entre dos nodos
    """
    delta = nodob - nodoa
    dist = np.linalg.norm(delta)
    k =  math.sqrt( area / cantNodos ) * C
    fuerza = dist*dist / k
    return delta*(fuerza/dist)

def calculo_gravedad(posicion, G):
    """
    calculo_gravedad :: ((float, float), float) -> (float, float)
    Parametros:
    posicion:   Vector con la posicion de un nodo
    G:          Constante gravitatoria
    Calcula la fuerza de gravedad ejercida sobre un nodo
    """
    dist = np.linalg.norm(posicion)
    return posicion* (-G/dist)
        

def leer_grafo_archivo(file_path):
    """
    leer_grafo_archivo :: (string) -> [list(string), list(list(string))]
    Parametros:
    file_path:  Path al archivo a leer
    Lee un grafo de un archivo y lo convierte a un grafo en formato lista
    """
    count = 0
    lista_nodos = []
    lista_aristas = []

    with open(file_path, 'r') as f:
        lineas = f.readlines()
        numNodos = int( lineas.pop(0) )
        for linea in lineas:
            if count < numNodos:
                lista_nodos.append( linea.rstrip('\n') )
            else:
                arista = linea.split(' ')
                lista_aristas.append( (arista[0], arista[1].rstrip('\n') ) )
            count = count + 1

    return [ lista_nodos, lista_aristas ]