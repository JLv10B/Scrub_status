"""
Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

Approach:
- We want to traverse the graph in order to find a link between node A & L
- Can perform depth or breadth first searches
- Can't do bidirectional because it's a directed graph
- Depth first search is easier to implement but is potentially slower
- Breath first search is faster and useful to find the shortest path

ex.
A -- B
|    |
C -- D
|
E -- F -- G -- H
     | \
     O  I -- J -- K
             |
             L

P -- Q
|  /
R

This graph can also be written like this:
Graph = {
A:[B,C],
B:[D],
C:[E],
D:[C],
E:[F],
F:[G,I,O],
G:[H],
H:[],
I:[J],
J:[K,L],
K:[],
L:[],
O:[],
P:[Q],
Q:[R],
R:[P]
}

"""

# Breadth first search: start at starting node
# Initiate visited and paths arrays
# Place starting node in the queue in a list to initiate the first path
# Pop the first element of paths and iterate through the child nodes
# Check each child node to see if they have been visited, 
# Also check each child node to see if it matches the desired end node
# If there is a match append to the current path and in visited and end loop, return a message that there is a path
# If not, append to current path and in visited and append current path to paths array 
#

graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs_shortest_path(graph, start, goal):
    paths = [start]
    visited = []
    
    if start == goal:
        return('start = goal')
    
    while paths:
        current_path = paths.pop(0)
        # print('Current_path:', current_path)
        node = current_path[-1]
        # print(f'Node: {node}, Visted: {visited}')
        if node not in visited:
            children = graph[node]
            for child_node in children:
                new_path = list(current_path) # Start a new path from current path for the new child node
                # print('new_path:', new_path)
                new_path.append(child_node)
                paths.append(new_path)
                # print('All paths:', paths)
                if child_node == goal:
                    return (f'Shortest path from {start} to {goal} is: {new_path}')
            visited.append(node)
    return('No path available')

# Testing
print(bfs_shortest_path(graph, 'G', 'D'))
                

