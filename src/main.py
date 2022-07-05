#! /usr/bin/python

import argparse
import layout_graph
import utils

from matplotlib.patches import Ellipse
from matplotlib import collections  as mc

def main():
    """
    Inicia el programa
    """
    # Definimos los argumentos de linea de comando que aceptamos
    # Los valores por defecto fueron calculados de forma empirica
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
        default=100
    )
    # Cada cuantas iteraciones se replotea
    parser.add_argument(
        '--refresh',
        type=int,
        help='Cada cuantas iteraciones se refrescara la imagen',
        default=1
    )
    # Altura del canvas
    parser.add_argument(
        '-H','--height',
        type=int,
        help='Altura del canvas',
        default=800
    )
    # Anchura del canvas
    parser.add_argument(
        '-w','--width',
        type=int,
        help='Ancho del canvas',
        default=800
    )
    # Archivo del cual leer el grafo
    parser.add_argument(
        'file_name',
        help='Archivo del cual leer el grafo a dibujar'
    )
    # Constante de la fuerza de repulsion
    parser.add_argument(
        '-r','--repulsion',
        type=float,
        help='Constante de la fuerza de repulsion',
        default= 0.1
    )
    # Constante de la fuerza de atraccion
    parser.add_argument(
        '-a','--atraccion',
        type=float,
        help='Constante de la fuerza de atraccion',
        default= 10
    )
    # Temperatura inicial
    parser.add_argument(
        '-t','--temp',
        type=float,
        help='Temperatura incial del sistema',
        default= 150.0
    )
    # Constante de disminucion de temperatura
    parser.add_argument(
        '-T','--constTemp',
        type=float,
        help='Constante de disminucion de la temperatura',
        default= 0.99
    )
    # Constante de gravedad
    parser.add_argument(
        '-g','--gravity',
        type=float,
        help='Constante de la fuerza de gravedad',
        default= 0.06
    )
    # Distancia minima entre 2 nodos
    parser.add_argument(
        '-e','--eps',
        type=float,
        help='Distancia minima entre nodos',
        default= 0.001
    )
    # Mostrar nombres de los nodos
    parser.add_argument(
        '-n', '--names',
        action='store_true',
        help='Muestra los nombres de los nodos del grafo'
    )
    # Mostrar Ejes del grafo
    parser.add_argument(
        '--axes',
        action='store_true',
        help='Muestra los ejes donde se grafica el grafo'
    )
    # Tamaño de letra
    parser.add_argument(
        '--fontsize',
        type=float,
        help='Tamaño de letra',
        default=200.0
    )

    args = parser.parse_args()
    
    # Carga el grafo desde el archivo ingresado por consola
    grafo = utils.leer_grafo_archivo( args.file_name )

    layout_gr = layout_graph.LayoutGraph(
         grafo, 
         iters = args.iters,
         refresh = args.refresh, 
         ancho = args.height,
         alto = args.width,
         c1 = args.repulsion,
         c2 = args.atraccion,
         t0 = args.temp,
         ct = args.constTemp,
         g = args.gravity,
         eps = args.eps,
         verbose=args.verbose,
         nodeNames = args.names,
         fontsize = args.fontsize,
         axes = args.axes
     )

    layout_gr.layout()
    return


if __name__ == '__main__':
    main()
