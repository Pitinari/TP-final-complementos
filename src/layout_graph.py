import matplotlib.pyplot as plt
import numpy as np
import random
import utils

class LayoutGraph:

    def __init__(self, grafo, iters, refresh, ancho, alto, c1, c2, t0, ct, g, eps, verbose = False, nodeNames = False, fontsize = 200, axes = False):
        """
        Parámetros:
        grafo:      grafo en formato lista
        iters:      cantidad de iteraciones a realizar
        refresh:    cada cuántas iteraciones graficar. Si su valor es cero, entonces debe graficarse solo al final.
        ancho:      ancho del canvas
        alto:       alto del canvas
        c1:         constante de repulsión
        c2:         constante de atracción
        t0:         temperatura inicial
        ct:         constante de disminucion de temperatura
        g:          constante de gravedad
        eps:        distancia minima entre nodos
        verbose:    si está encendido, activa los comentarios
        nodeNames:  si esta encencido, plotea los nombres de los nodos
        fontsize:   tamaño del nombre de los nodos
        axes:       si esta encendido, plotea los ejes
        """

        # Guardo el grafo
        self.grafo = grafo
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.c1 = c1
        self.c2 = c2
        self.t = t0
        self.ct = ct
        self.g = g
        self.eps = eps

        # Inicializo estado
        # Completar
        self.fuerzas = {}
        self.posiciones = utils.randomize_position(self.grafo[0], self.ancho, self.alto)

        # Guardo opciones
        self.iters = iters
        self.verbose = verbose
        self.refresh = refresh
        self.nodeNames = nodeNames
        self.fontsize = fontsize
        self.axes = axes

    def printPos(self):
        """
        printPos :: () -> ()
        Imprime las posiciones de todos los nodos por consola.
        """
        for nodo in self.grafo[0]:
            print("Nodo "+nodo+" en pos: "+str(self.posiciones[nodo][0])+" "+str(self.posiciones[nodo][1]))
   
    def printFuer(self):
        """
        printFuer :: () -> ()
        Imprime las fuerzas ejercidas sobre cada nodo por consola.
        """
        for nodo in self.grafo[0]:
            print("Nodo "+nodo+" fuerza: ("+str(self.fuerzas[nodo][0])+" "+str(self.fuerzas[nodo][1])+")")
    
    def printDist(self):
        """
        printDist :: () -> ()
        Imprime la distancia entre cada par de nodos por consola.
        """
        lista_nodos = self.grafo[0]
        for i in range( len( lista_nodos ) ):
            for j in range ( len( lista_nodos ) - (i+1) ):
                nodoa = lista_nodos[i]
                nodob = lista_nodos[ (i+1) + j]
                print("Dist de "+nodoa+" a "+nodob+": " +str(np.linalg.norm(self.posiciones[nodob]-self.posiciones[nodoa])))

    def corregir_posiciones(self, nodo):
        """
        corregir_posiciones :: () -> ()
        Pone las posiciones de un nodo en los bordes si se salieron del area.
        """
        if self.posiciones[nodo][0] > (self.ancho)/2:
            self.posiciones[nodo][0] = (self.ancho)/2
        if self.posiciones[nodo][0] < -(self.ancho)/2:
            self.posiciones[nodo][0] = -(self.ancho)/2
        if self.posiciones[nodo][1] > (self.alto)/2:
            self.posiciones[nodo][1] = (self.alto)/2
        if self.posiciones[nodo][1] < -(self.alto)/2:
            self.posiciones[nodo][1] = -(self.alto)/2

    def graficar (self, iter):
        """
        graficar :: (int) -> ()
        Parametros:
        iter:   Numero de la iteracion actual
        Grafica un grafo en pantalla 
        """
        nodos = len( self.grafo[0] )
        lista_aristas = self.grafo[1]
        data = []
        # Ploteamos los nodos
        for nodo in self.grafo[0]:
            x = self.posiciones[nodo][0]
            y = self.posiciones[nodo][1]
            if self.nodeNames:
                plt.scatter(x, y, self.fontsize, '#FF0000', '$'+ nodo +'$') # Nodos con nombres
            else:
                plt.scatter(x, y, self.fontsize, facecolors='#FF0000')      # Nodos anonimos

        # Cargamos las aristas en el formato que requiere plot
        for arista in lista_aristas:
            nodoa = arista[0]
            nodob = arista[1]
            xx1 = self.posiciones[nodoa][0]
            yy1 = self.posiciones[nodoa][1]
            xx2 = self.posiciones[nodob][0]
            yy2 = self.posiciones[nodob][1]
            plt.plot((xx1, xx2), (yy1, yy2), 'black')

        # Agregamos un titulo
        plt.title("Temp= " + str( round(self.t) ) + " iter = " + str(iter) )
        # Fijamos el canvas, agregando un padding del fontsize/50 (fue calculado empiricamente con un ojimetro)
        plt.xlim(-(self.ancho/2 + self.fontsize / 50),(self.ancho/2 + self.fontsize / 50))
        plt.ylim(-(self.alto/2 + self.fontsize / 50),(self.alto/2 + self.fontsize / 50))
        # Elimina los ejes
        if (not self.axes) :
            plt.axis("off") 
        # Muestra el plot en pantalla
        plt.draw()

    def step(self):
        """
        step :: () -> ()
        Calcula un paso del algoritmo
        """
        #inicializa las fuerzas en (0,0)
        for nodo in self.grafo[0]:
            self.fuerzas[nodo] = np.array([0.0, 0.0])

        lista_nodos = self.grafo[0]     #Lista de nodos
        lista_aristas = self.grafo[1]   #Lista de aristas
        cantNodos = len( lista_nodos )  #Cantidad de nodos
        
        # computa fuerzas de atraccion (por aristas)
        for arista in lista_aristas:
            nodoa = arista[0]
            nodob = arista[1]
            fa = utils.calculo_atraccion(self.posiciones[nodoa], self.posiciones[nodob], cantNodos, self.area, self.c2 )
            self.fuerzas[nodoa] += fa   # Sumamos la fuerza en un nodo y restamos en el otro, para simular fuerzas con sentido opuesto
            self.fuerzas[nodob] -= fa

        # computa repulsiones (por nodos)
        for i in range( len( lista_nodos ) ):
            for j in range ( len( lista_nodos ) - (i+1) ):
                nodoa = lista_nodos[i]
                nodob = lista_nodos[ (i+1) + j]
                fr = utils.calculo_repulsion(self.posiciones[nodoa], self.posiciones[nodob], cantNodos, self.area, self.c1 )
                self.fuerzas[nodoa] -= fr
                self.fuerzas[nodob] += fr

        # calculamos la gravedad
        for nodo in lista_nodos:
            fg = utils.calculo_gravedad(self.posiciones[nodo], self.g )
            self.fuerzas[nodo] += fg
                

        # Limitamos la fuerza en base a la temperatura del sistema
        for nodo in lista_nodos:
            mod = np.linalg.norm(self.fuerzas[nodo])
            if mod > self.t:
                self.fuerzas[nodo] *= self.t/mod # Volvemos la fuerza un vector unitario y la multiplicamos por la temperatura

        # Aplicamos las fuerzas y limitamos las posiciones a estar contenidas en el canvas
        for nodo in lista_nodos:
            self.posiciones[nodo] += self.fuerzas[nodo]
            self.corregir_posiciones(nodo)

        # Si se produce una colision (la distancia entre dos nodos es menor al epsilon del sistema)
        # aplicaremos una fuerza aleatoria entre una y dos veces la constante de repulsion
        # Realizaremos esto hasta que no se produzcan colisiones
        colision = True
        while colision: 
            colision = False
            for nodoa in lista_nodos:
                for nodob in lista_nodos:
                    delta = self.posiciones[nodob] - self.posiciones[nodoa]
                    dist = np.linalg.norm(delta)
                    if (dist < self.eps and nodoa != nodob):
                            fuerza = np.array([random.uniform(1, 2) * self.c2, random.uniform(1, 2) * self.c2])
                            self.posiciones[nodoa] += fuerza
                            self.posiciones[nodob] -= fuerza
                            self.corregir_posiciones(nodoa)
                            self.corregir_posiciones(nodob)
                            colision =  True

    def layout(self):
        """
        layout :: () -> ()
        Funcion que realiza el algoritmo y muestra en pantalla
        """       
        
        plt.ion() # con esto permitimos actualizar el cuadro.

        # Loop principal de iteracion
        for iter in range(1, self.iters + 1):
            plt.clf()   # Limpia el plot
            self.step() # Realiza un calculo de un step del algoritmo
            
            self.t = self.ct * self.t   # Actualizamos la temperatura

            # Ploteamos si es la ultima iteracion o 
            # si refresh es distinto de cero ploteamos en las iteraciones multiplos de refresh
            if (iter == self.iters or (self.refresh and iter % self.refresh == 0)):
                self.graficar(iter)
                # Tiempo entre cada frame, al ser tan pequeño es limitado por el tiempo de calculo de un step
                plt.pause(0.0000001)
            
            # Imprime las informacion por consola si se elegio el modo verbose
            if (self.verbose):
                print("Iteracion "+ str(iter))
                self.printPos()
                self.printFuer()
                self.printDist()

        # Muestra el ultimo plot y espera que se presione enter en la consola para terminar
        # plt.show()
        self.graficar(iter)
        print("Pulse enter para continuar...")
        input()
    
        pass