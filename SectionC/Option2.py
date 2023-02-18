from typing import List, Dict, Any

roads = {
  "graph": {
    "directed": False,
    "nodes": [{ "id": 0 }, { "id": 1 }, { "id": 2 }, { "id": 3 }, { "id": 4 }],
    "edges": [
      {
        "source": 0,
        "target": 1,
        "metadata": {
          "distance": 5,
        },
      },
      {
        "source": 1,
        "target": 3,
        "metadata": {
          "distance": 9,
        },
      },
      {
        "source": 3,
        "target": 2,
        "metadata": {
          "distance": 6,
        },
      },
      {
        "source": 2,
        "target": 4,
        "metadata": {
          "distance": 3,
        },
      },
      {
        "source": 4,
        "target": 3,
        "metadata": {
          "distance": 8,
        },
      },
      {
        "source": 4,
        "target": 0,
        "metadata": {
          "distance": 2,
        },
      },
    ],
  },
}


def navigate(roads: Dict[str, Any], start: int, end: int) -> Dict[str, Any]:
    # Creating a dictionary to store the graph
    graph = {}
    
    # Adding each node to the graph with an empty adjacency list
    for node in roads["graph"]["nodes"]:
        graph[node["id"]] = []
        
    # Adding each edge to the graph
    for edge in roads["graph"]["edges"]:
        source = edge["source"]
        target = edge["target"]
        distance = edge["metadata"]["distance"]
        
        graph[source].append((target, distance))
        graph[target].append((source, distance))
    
    # Creating a dictionary to store the distance from the start node to each node in the graph
    distance = {}
    
    # Setting the distance of the start node to 0 and all other nodes to infinity
    for node in graph:
        if node == start:
            distance[node] = 0
        else:
            distance[node] = float("inf")
    
    # Creating a dictionary to store the previous node in the shortest path from the start node to each node in the graph
    previous = {}
    
    # Setting the previous node of all nodes to None
    for node in graph:
        previous[node] = None
    
    # Creating a set of unvisited nodes
    unvisited = set(graph.keys())
    
    # Looping through all unvisited nodes
    while unvisited:
        # Finding the unvisited node with the smallest distance from the start node
        current = None
        for node in unvisited:
            if current is None or distance[node] < distance[current]:
                current = node
        
        # Removing the current node from the set of unvisited nodes
        unvisited.remove(current)
        
        # If the current node is the end node, we're done
        if current == end:
            break
        
        # Looping through all the neighbors of the current node
        for neighbor, distance_to_neighbor in graph[current]:
            # If the distance to the neighbor through the current node is smaller than the current distance to the neighbor, update the distance and previous node
            new_distance = distance[current] + distance_to_neighbor
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                previous[neighbor] = current
    
    # Creating a list of nodes in the shortest path from the end node to the start node
    path = [end]
    node = end
    while previous[node] is not None:
        path.append(previous[node])
        node = previous[node]
    path.reverse()
    
    # Creating a dictionary to store the distance and path
    result = {}
    result["distance"] = distance[end]
    result["path"] = path
    
    return result

print(navigate(roads, 0, 2))
