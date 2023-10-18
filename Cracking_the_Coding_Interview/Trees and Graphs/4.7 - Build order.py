"""
Ask: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.

EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)

Output: f, e, a, b, d, c
"""

# Recursive version:
# Create a graph class with attributes self.graph and self.nodes and self.dependencies
class Graph:
    def __init__(self, nodes, dependencies):
        self.nodes = nodes
        self.graph = {}
        self.dependencies = dependencies

    def createGraph(self, nodes):
        for node in nodes:
            if node not in self.graph:
                self.graph[node] = []
        
    def addEdge(self, dependencies):
    # Adds a dependency from one node to another node
    # Input will be a list of sets with the 2nd element is dependent on the first element.
    # 2nd element is the key and 1st element is the value
        for edge in dependencies:
            self.graph[edge[1]].append(edge[0])

        print('Updated graph with dependecies:', self.graph)

    def topolgicalSortUtil(self, node, visited, stack):
    # Recursive function used by topologicalSort
    # Add current node to visited
    # Recur for all adjacent nodes
    # If the adjecent node is in visted and not in stack
    # Push current node to the start of the stack
        visited.append(node)
        # print('node:', node)
        # print('Visited:', visited)

        for list in self.graph[node]:
            for adjacent in list:
                if adjacent not in visited:
                    self.topolgicalSortUtil(adjacent, visited, stack)
                elif adjacent in visited and adjacent not in stack:
                    return ValueError
                    
        stack.append(node)
        # print('Stack:', stack)
        

    def topologicalSort(self):
    # Initiate visited and stack array to store values
    # Visted stores the nodes that are being processed
    # Stack stores the resulting order
    # Call the recursive helper function to store topological sort
    # return contents of stack
        visited = []
        stack = []

        for project in self.nodes:
            # print('project:', project)
            if project not in visited:
                self.topolgicalSortUtil(project, visited, stack)
            
        if len(stack) != len(self.nodes):
            return("--Error, unable to create build order--")
        else:
            return stack
    
# Testing
# nodes = ['a','b','c','d','e','f']
# dependencies = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']]

# g = Graph(nodes, dependencies)
# g.createGraph(nodes)
# g.addEdge(dependencies)
 
# print ("Following is a Topological Sort of the given graph")
# print(g.topologicalSort())



"""
Non-recursive approach:
-Create graph node to store data, edges/dependencies, and dependency count
-Create queue class
"""
class GraphNode:
    def __init__(self, data):
        self.data = data
        self.edges = []
        self.dependencies_left = 0
    
    def addEdge(self, node):
        self.edges.append(node)
        node.dependencies_left += 1

def build_order(projects, dependencies):
    nodes = {}
    queue = []
    build_order = []

    for project in projects:
        nodes[project] = GraphNode(project)

    for dependecy in dependencies:
        nodes[dependecy[0]].addEdge(nodes[dependecy[1]])
    
    for project in projects:
        current_node = nodes[project]
        if not current_node.dependencies_left:
            queue.append(current_node)

    while len(queue) > 0:
        node = queue.pop(0)
        build_order.append(node.data)
        for dependent in node.edges:
            dependent.dependencies_left -= 1
            if not dependent.dependencies_left:
                queue.append(dependent)

    if len(build_order) < len(projects):
        return Exception("Cycle detected")
    return build_order
    
# Testing:
projects = ["A", "B", "C", "D", "E", "F", "G"]
dependencies = [("C", "A"), ("B", "A"), ("F", "A"), ("F", "B"), ("F", "C"),
        ("A", "E"), ("B", "E"), ("D", "G")]

print(build_order(projects, dependencies))