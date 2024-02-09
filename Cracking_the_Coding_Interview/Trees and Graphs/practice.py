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

Req:
- Find whether or not there is a valid build order
- If there is a valid build order return build order else return an error
- Dependencies must be completed before primary project can be completed, one way relationship

Time: O(n+m)
Space: O(n)

- Use a dictionary to create a one way graph

Edgecase:
-If there is a loop in the dependencies then there is no valid build order
    - We can find a loop in the dependencies by creating a one way graph and performing a find_loop function
    - The find_loop function performs a DFS starting at the input node until it reaches a leaf or finds a loop
    - If a loop is found return True, if not return False and a cache with all the traversed nodes
    - We can use the cache to decrease repitition
    - We can likely create the build order as we search through the graph

buid_order -> returns final build order or error
find_loop -> returns True/False for loop and cache of seen nodes
    -


"""
def create_depend_dict(projects, dependecies):
    depend_dict = {}
    for edge in dependecies:
        if edge[1] in depend_dict:
            depend_dict[edge[1]].append(edge[0])
        else:
            depend_dict[edge[1]] = [edge[0]]
    
    for node in projects:
        if node not in depend_dict:
            depend_dict[node] = []
    
    return depend_dict

def build_order(projects, dependecies):
    depend_dict = create_depend_dict(projects, dependecies)
    
    visited = set()
    build_order = []

    for proj in projects:
        if proj not in visited:
            find_loop(proj, visited, build_order, depend_dict)
    
    if len(build_order) != len(projects):
        return ValueError
    
    return build_order

def find_loop(proj, visited, build_order, depend_dict):
    # Add proj to visited
    # For any dependencies in depend_dict, if the dependency is not in visited recurse
    # If the dependency is in visited but not in build_order then return False
    # append proj to build_order
    # return build_order
    visited.add(proj)

    for depend in depend_dict[proj]:
        if depend not in visited:
            find_loop(depend, visited, build_order, depend_dict)
        elif depend in visited and depend not in build_order:
            return ValueError
        
    build_order.append(proj)

    return build_order

# Testing
if __name__ == "__main__":
    nodes = ['a','b','c','d','e','f']
    dependencies = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']]

    print(build_order(nodes, dependencies))