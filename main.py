from collections import deque

grafo = {}

grafo['A'] = ['B', 'C', 'D']
grafo['B'] = ['A', 'H']
grafo['C'] = ['F', 'G']
grafo['D'] = ['A', 'E']
grafo['E'] = ['D', 'K']
grafo['F'] = ['C', 'J']
grafo['G'] = ['C', 'J']
grafo['H'] = ['B', 'I']
grafo['I'] = ['H', 'J']
grafo['J'] = ['F', 'G', 'I', 'K']
grafo['K'] = ['E', 'J']

origen = 'A'

pila = []
visitados = []
recorrido = []

pila.append(origen)
visitados.append(origen)


while len(pila) > 0:
    vertice = pila[-1]
    recorrido.append(vertice)
    pila.pop()
    adyacente = grafo[vertice]
    for i in adyacente:
        ady = i
        if not ady in visitados:
            visitados.append(ady)
            pila.append(ady)
    print("Visitados: ", visitados)
    print("Faltantes: ", pila)
    print("Recorrido: ", recorrido)
