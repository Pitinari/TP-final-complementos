#! /usr/bin/python

# 6ta Practica Laboratorio 
# Complementos Matematicos I
# Ejemplo parseo argumentos

import argparse
import matplotlib.pyplot as plt
import numpy as np

class Graph:
    """Definimos esta clase como ayuda a la implementación del algoritmo de Fleury
    """

    def __init__(self, grafo_lista):
        """Inicializamos el grafo a partir de un grafo en representación de lista
        """

        self.V = grafo_lista[0]
        self.graph = self.listaADiccionario(grafo_lista)

    def listaADiccionario(self, grafo_lista):
        """Toma un grafo no dirigido en representación de lista y retorna un diccionario, en donde las claves
        son vértices y los valores son listas de vértices, representando cada una de las aristas. Por ejemplo:
        {'a': ['b', 'e'],..} representa la existencia de las aristas ('a','b') y ('a','e')
        """
        graph = {v: [] for v in grafo_lista[0]}
        for (u, v) in grafo_lista[1]:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def agregarArista(self, u, v):
        """Dados dos vértices (u y v), agrega la arista (u,v) (y también la arista (v,u) puesto que es un grafo
        no dirigido)"""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def cantidadVerticesAlcanzables(self, v, visitados):
        """Cuenta la cantidad de vértices alcanzables desde v, haciendo una búsqueda en profundidad.
        El argumento visited es un diccionario en donde las claves son los vértices, y los valores
        corresponden a un booleano indicando si el vértice fue visitado o no.
        La primera vez que se llama al método, ningún vértice debe haber sido visitado.
        """
        count = 1
        visitados[v] = True
        for i in self.graph[v]:
            if not visitados[i]:
                count = count + self.cantidadVerticesAlcanzables(i, visitados)
        return count

    def esSiguienteAristaValida(self, u, v):
        """Determina si la arista (u,v) es elegible como próxima arista a visitar."""
        pass


class LayoutGraph:

    def __init__(self, grafo, iters, refresh, c1, c2, verbose=False):
        """
        Parámetros:
        grafo: grafo en formato lista
        iters: cantidad de iteraciones a realizar
        refresh: cada cuántas iteraciones graficar. Si su valor es cero, entonces debe graficarse solo al final.
        c1: constante de repulsión
        c2: constante de atracción
        verbose: si está encendido, activa los comentarios
        """

        # Guardo el grafo
        self.grafo = grafo

        # Inicializo estado
        # Completar
        self.posiciones = {}
        self.fuerzas = {}

        # Guardo opciones
        self.iters = iters
        self.verbose = verbose
        # TODO: faltan opciones
        self.refresh = refresh
        self.c1 = c1
        self.c2 = c2

    def layout(self):
        """
        Aplica el algoritmo de Fruchtermann-Reingold para obtener (y mostrar)
        un layout
        """
        pass


def main():
    # Definimos los argumentos de linea de comando que aceptamos
    parser = argparse.ArgumentParser()

    # Verbosidad, opcional, False por defecto
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Muestra mas informacion al correr el programa'
    )
    # Cantidad de iteraciones, opcional, 50 por defecto
    parser.add_argument(
        '--iters',
        type=int,
        help='Cantidad de iteraciones a efectuar',
        default=50
    )
    # Temperatura inicial
    parser.add_argument(
        '--temp',
        type=float,
        help='Temperatura inicial',
        default=100.0
    )
    # Archivo del cual leer el grafo
    parser.add_argument(
        'file_name',
        help='Archivo del cual leer el grafo a dibujar'
    )

    args = parser.parse_args()

    # Descomentar abajo para ver funcionamiento de argparse
    print(args.verbose)
    print(args.iters)
    print(args.file_name)
    print(args.temp)
    return

    # # TODO: Borrar antes de la entrega
    # grafo1 = ([1, 2, 3, 4, 5, 6, 7],
    #           [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 1)])
    #
    # # Creamos nuestro objeto LayoutGraph
    # layout_gr = LayoutGraph(
    #     grafo1,  # TODO: Cambiar para usar grafo leido de archivo
    #     iters=args.iters,
    #     refresh=1,
    #     c1=0.1,
    #     c2=5.0,
    #     verbose=args.verbose
    # )
    #
    # # Ejecutamos el layout
    # layout_gr.layout()
    # return


if __name__ == '__main__':
    main()
