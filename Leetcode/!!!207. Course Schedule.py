"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You 
are given an array prerequisites where prerequisites = [a, b] indicates that you must take 
course bi first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Input: numCourses = int, prerequisits = array of 2 element arrays [[course, prereq]]
Output: True if you can finish all courses

Time: O(n)
Space: O(n)

Example:
numCourses = 5
prereq = [[1,0], [2,1], [3,0]]
Output = True

numCourses = 5
prereq = [[1,0], [2,1], [0,2]] <-- loop
Output = False
"""

def course_schedule(numCourses, prereq):
    """
    - Create adjacency list with helper_graph
    - Initiate (visited)
    - Traverse through adjacency list using DFS to find cycle
    - If found then return False
    
    helper(prereq) output:
    { pre : [course],
        0: [1],
        1: [2],
        2: [0],
        3: [1,2,3]      
    }

    """
    prereq_graph = helper_graph(prereq)
    visited = ()
    for course in prereq_graph.keys():
        if graph_traversal(prereq_graph, course, visited, course) is False:
            return False
    
def helper_graph(prereq):
    """
    Input prereq and create an adjacency list

    input datastructure:
    [
        [course, pre],
        ...
    ]

    output Datastucture:
    { pre : [course],
        0: [1],
        1: [2],
        2: [0],
        3: [1,2,3]      
    }

    -Initate {prereq_graph}, pre: courses
    -Iterate through prereq array [course, pre]
    -For each element in prereq check if pre in {prereq_graph}
    -If not initate prereq_graph[pre] = course
    -If prereq_graph[pre], then append(course)
    """
    prereq_graph = {}
    for element in prereq:
        if element[1] not in prereq_graph:
            prereq_graph[element[1]] = element[0]
        else:
            prereq_graph[element[1]].append(element[0])
    return prereq_graph

def graph_traversal(prereq_graph, course, visited, start):
    """
    Performs the traveral through the graph given to find cycles
    If cycle is found return False, else True

    Input:
    prereq_graph: {graph}
    course: current node
    visited: (nodes that have been processed)
    start: holds node that DFS was started at

    Output:
    Bool: True if recursive stack ends without cycle, False if there is a cycle
    """

    visited.add(course)

    for element in prereq_graph[course]:
        if element not in visited:
            graph_traversal(prereq_graph, element, visited, start)
        if element in visited and element == start:
            return False
    return True