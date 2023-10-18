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

Notes:
-Given list of tuples we must find what order projects must get done, (first, second)
-This is essentially giving us a parent/child relationship so we can likely use a tree/graph to solve
1.) Create a graph
    -Each node represents a project
    -Each edge represents a 1 way relationship
2.) Traverse graph to create result array
    -Some nodes may not have edges
"""
                 
# In order to build a graph we need to know the relationships and all projects
# Import all projects and dependencies
# Initiate a graph as an empty dictionary to store project:dependents
# Iterate through projects to make sure they are all in the graph in case of no dependencies

def build_order(projects, dependencies):
    projects = projects
    graph = {}
    visited = []
    order = []

    for project, dependent in dependencies:
        if dependent not in graph:
            graph[dependent] = [project]
        else:
            graph[project].append(dependent)

    for element in projects:
        if element not in graph:
            graph[project] = []

    for graph_proj, graph_dep in graph:
        if graph_dep is None:
            order.append(graph_proj)
        else:
            for proj in graph_dep:
                