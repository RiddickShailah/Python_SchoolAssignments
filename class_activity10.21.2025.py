class Graph:
    def __init__(self, num_vertices):
        self.num_vertices= num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range (num_vertices)]

    def add_edge(self, u, v):
        if u < 0 or v < 0 or u>= self.num_vertices or v>= self.num_vertices:
            print("Invalid vertex index")
            return
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def print_matrix(self):
        print("Adjacency Matrix")
        for row in self.adj_matix:
            print(row)