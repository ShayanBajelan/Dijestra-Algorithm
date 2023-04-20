# %%
import sys

class Graph():
    def __init__(self, size):
        self.__size = size
        self.__matrix = None
        pass

    def initialize(self, matrix):
        self.__matrix = matrix
        pass

    def find_minimum_cost(self, distances, visited):
        min_cost = sys.maxsize
        min_node = None
        for node in range(self.__size):
            if distances[node] < min_cost and not visited[node]:
                min_cost = distances[node]
                min_node = node
        return min_node

    def dijkstra(self, start_node):
        visited = [False] * self.__size
        distances = [sys.maxsize] * self.__size
        distances[start_node] = 0

        for i in range(self.__size):
            current_node = self.find_minimum_cost(distances, visited)
            visited[current_node] = True

            for neighbor_node in range(self.__size):
                cost = self.__matrix[current_node][neighbor_node]
                if cost != 0 and not visited[neighbor_node]:
                    new_cost = distances[current_node] + cost
                    if new_cost < distances[neighbor_node]:
                        distances[neighbor_node] = new_cost
        return distances


if __name__ == "__main__":
    g = Graph(5)
    matrix = [[0, 1, 6, 0, 0],
              [1, 0, 2, 1, 0],
              [6, 2, 0, 2, 5],
              [0, 1, 2, 0, 5],
              [0, 0, 5, 5, 0]]
    g.initialize(matrix)
    shortest_distance = g.dijkstra(0)
    print(shortest_distance)

    g2 = Graph(9)
    matrix2 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    g2.initialize(matrix2)
    shortest_distance2 = g2.dijkstra(0)
    print(shortest_distance2)