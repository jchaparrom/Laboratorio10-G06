from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as V
from DataStructures.Graph import edge as E


def new_graph(order=20):
    """
    Crea e inicializa un nuevo grafo dirigido vacío.
    """
    return {
        "vertices": mp.new_map(order, 0.5),
        "num_edges": 0,
    }


def insert_vertex(graph, key, value):
    """
    Inserta un vértice con llave 'key' y valor 'value' si no existe aún.
    Retorna el grafo actualizado.
    """
    if not mp.contains(graph["vertices"], key):
        new_v = V.new_vertex(key, value)
        mp.put(graph["vertices"], key, new_v)
    return graph


def contains_vertex(graph, key):
    """
    Retorna True si el vértice con 'key' existe en el grafo, o False en caso contrario.
    """
    return mp.contains(graph["vertices"], key)


def add_edge(graph, vertex_a, vertex_b, weight=0):
    if not (contains_vertex(graph, vertex_a) and contains_vertex(graph, vertex_b)):
        return graph

    v_a = mp.get(graph["vertices"], vertex_a)
    adjacents_map = v_a["adjacents"]

    if not mp.contains(adjacents_map, vertex_b):
        new_e = E.new_edge(vertex_a, vertex_b, weight)
        mp.put(adjacents_map, vertex_b, new_e)
        graph["num_edges"] += 1
    else:
        existing_edge = mp.get(adjacents_map, vertex_b)
        existing_edge["weight"] = weight

    return graph


def order(graph):
    """
    Retorna el número total de vértices del grafo.
    """
    return mp.size(graph["vertices"])


def size(graph):
    """
    Retorna el número total de arcos dirigidos del grafo.
    """
    return graph["num_edges"]