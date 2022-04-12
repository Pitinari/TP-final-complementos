import matplotlib.pyplot as plt
import numpy as np

X_MAX=500
Y_MAX=500

class LayoutGraph:

    def __init__(self, grafo, iters, refresh, C, verbose=False):
        """
        Parámetros:
        grafo: grafo en formato diccionario de vertices con sus aristas
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
        self.initPos()
        self.fuerzas = {}
        self.initK(C)

        # Guardo opciones
        self.iters = iters
        self.verbose = verbose
        # TODO: faltan opciones
        self.refresh = refresh
        

    def initK(self, C):
        self.k = C * np.sqrt( (X_MAX * Y_MAX * (2/3)) / self.grafo.numOfVertices )

    def initPos(self):
        self.posiciones = {}
        for vert in self.grafo.dicEdges.keys():
            self.posiciones[vert] = {}
            self.posiciones[vert] = {"x": np.random.randint(0, X_MAX+1), "y": np.random.randint(0, Y_MAX+1)}
    
    def distanceVert(v1, v2):
        return np.sqrt( np.power(self.posiciones[v1]["x"] - self.posiciones[v2]["x"], 2) + np.power(self.posiciones[v1]["y"] - self.posiciones[v2]["y"], 2) )

    def attractionForce(dist):
        return (dist * dist) / self.k

    def repulsionForce(dist):
        return (self.k * self.k) / dist

    def initAccumForces(self):
        for vert in self.grafo.dicEdges.keys():
            self.accumForces[vert] = {"x": 0, "y": 0}

    def step():


    def layout(self):
        """
        Aplica el algoritmo de Fruchtermann-Reingold para obtener (y mostrar)
        un layout
        """
        for _ in range(self.iters):
            self.initAccumForces()
            for vert1 in self.grafo.dicEdges.keys():
                for vert2 in self.grafo.dicEdges.keys():
                    if(vert1 != vert2):
                        distance = self.distanceVert(vert1, vert2)
                        mod_fr = self.repulsionForce(distance)
                        self.accumForces[vert1]["x"] += (mod_fr * (self.posiciones[vert1]["x"] - self.posiciones[vert2]["x"])) / distance
                        self.accumForces[vert1]["y"] += (mod_fr * (self.posiciones[vert1]["y"] - self.posiciones[vert2]["y"])) / distance
            
            for 

        pass