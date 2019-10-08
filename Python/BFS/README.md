Graph traversal means visiting every vertex and edge exactly once in a well-defined order. While using certain graph algorithms, 
you must ensure that each vertex of the graph is visited exactly once.
The order in which the vertices are visited are important and may depend upon the algorithm or question that you are solving.

Breadth First Search (BFS)

BFS is a traversing algorithm where you should start traversing from a selected node (source or starting node) and traverse the graph 
layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node). You must then move towards the next-level 
neighbour nodes.

As the name BFS suggests, you are required to traverse the graph breadthwise as follows:

1) First move horizontally and visit all the nodes of the current layer
2) Move to the next layer

A graph can contain cycles, which may bring you to the same node again while traversing the graph. 
To avoid processing of same node again, use a boolean array which marks the node after it is processed. While visiting the nodes in the 
layer of a graph, store them in a manner such that you can traverse the corresponding child nodes in a similar order.
