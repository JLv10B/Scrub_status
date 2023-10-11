"""
Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

Approach:
- We want to traverse the graph in order to find a link between node A & L
- Can perform depth or breadth first searches
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


"""

# 