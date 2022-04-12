import errno

class Graph:
    """Definimos esta clase como ayuda a la implementación del algoritmo de Fleury
    """

    def __init__(self, graphFile):
        """Inicializamos el grafo a partir de un grafo en representación de archivo
        """
        try:
            file = open(graphFile, 'r')
            self.numOfVertices = int(file.readline().strip())

            #TODO: check for errors in the input

            _graph = {}

            for _ in range(0,self.numOfVertices):
                _graph[str(file.readline().strip())] = []

            for line in file.readlines():
                [x,y] = line.split()
                _graph[x].append(y)
                _graph[y].append(x)

            file.close()
            self.dicEdges = _graph
        
        except (OSError, IOError) as e:
            if getattr(e, 'errno', 0) == errno.ENOENT:
               print("El archivo no existe")
            raise

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

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        'file_name',
        help='Archivo del cual leer el grafo a importar'
    )

    gr = Graph(parser.parse_args().file_name)
    print(gr.dicEdges)
    print(gr.numOfVertices)

if __name__ == '__main__':
    import argparse
    main()
