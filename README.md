# Dijestra-Algorithm
This code defines a class Graph that represents a graph and contains methods to perform Dijkstra's algorithm to find the shortest distance from a given starting node to all other nodes in the graph.

The __init__ method initializes the size of the graph and sets the matrix that represents the graph to None.

The initialize method sets the matrix of the graph to a given matrix.

The find_minimum_cost method takes in an array of distances from the starting node to each node in the graph, and an array of booleans that indicates whether a node has been visited or not. It then finds the unvisited node with the minimum distance from the starting node and returns its index.

The dijkstra method takes in the starting node and performs Dijkstra's algorithm to find the shortest distance from the starting node to all other nodes in the graph. It initializes an array of distances to each node as infinity except for the starting node, which is initialized to 0. It then iterates over all the nodes in the graph, finding the node with the minimum distance that has not been visited yet. For each unvisited neighbor of this node, it calculates a new distance from the starting node to that neighbor node and updates its distance if the new distance is smaller than the old distance.

The if __name__ == "__main__": block creates two instances of the Graph class and initializes them with different matrices. It then calls the dijkstra method on each of them with a starting node of 0, and prints out the resulting shortest distance arrays.
