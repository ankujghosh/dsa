from collections import defaultdict, deque

def topological_sort_bfs(graph):
    in_degree = defaultdict(int)
    for node in graph:
        in_degree[node]  # Initialize in-degrees with zero
    
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = deque([node for node in in_degree if in_degree[node] == 0]) #nodes with 0 indegree
    
    result = []
    count = 0 #count of visited nodes.

    while queue:
        node = queue.popleft()
        result.append(node)
        count +=1

        if node in graph: #check if the node has neighbors.
          for neighbor in graph[node]:
              in_degree[neighbor] -= 1
              if in_degree[neighbor] == 0:
                  queue.append(neighbor)

    if count != len(in_degree): # if count does not equal the number of nodes, it indicates a cycle.
        return []  # Cycle detected

    return result

graph_number = {
    0: [2],
    1: [2, 4],
    2: [3],
    4: [5],
    5: [3]
}
sorted_nodes_number = topological_sort_bfs(graph_number)
print('sorted_nodes_number:', sorted_nodes_number)

graph_number_cycle = {
    1: [0],
    0: [2],
    2: [3],
    3: [5],
    4: [1],
    5: [4]
}
sorted_nodes_number_cycle = topological_sort_bfs(graph_number_cycle)
print('sorted_nodes_number_cycle:',sorted_nodes_number_cycle)

'''OTHER Example:
# Example usage:
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

sorted_nodes = topological_sort_bfs(graph)
print(sorted_nodes)  # Output: ['A', 'B', 'C', 'D', 'E', 'F'] or another valid topological sort.

# Example with a cycle:
graph_cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

sorted_nodes_cycle = topological_sort_bfs(graph_cycle)
print(sorted_nodes_cycle) # Output: []

#Example with empty graph:
graph_empty = {}

sorted_nodes_empty = topological_sort_bfs(graph_empty)
print(sorted_nodes_empty) # Output: []
'''
