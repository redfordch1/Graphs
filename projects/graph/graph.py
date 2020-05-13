# Breadth-First Traversal
# Add starting node to a queue
# While queue isn't empty:
#     Dequeue the first vert
#     If that vert isn't visited:
#         Mark as visited
#         Add all its unvisited neighbors to the queue
# Depth-First Traversal
# Add starting node to a stack
# While stack isn't empty:
#     Pop the first vert
#     If that vert isn't visited:
#         Mark as visited
#         Push all its unvisited neighbors to the stack

# class Graph:
# ​
# 	def __init__(self):
# 		self.vertices = {}
# ​
# 	def add_vertex(self, vertex_id):
# 		self.vertices[vertex_id] = set()  # set of edges
# ​
# 	def add_edge(self, v1, v2):
# 		"""Add edge from v1 to v2."""
# ​
# 		# If they're both in the graph
# 		if v1 in self.vertices and v2 in self.vertices:
# 			self.vertices[v1].add(v2)
# ​
# 		else:
# 			raise IndexError("Vertex does not exist in graph")
# ​
# 	def get_neighbors(self, vertex_id):
# 		return self.vertices[vertex_id]
# ​
# 	def bft(self, starting_vertex_id):
# 		"""Breadth-first Traversal."""
# ​
# 		q = Queue()
# 		q.enqueue(starting_vertex_id)
# ​
# 		# Keep track of visited nodes
# 		visited = set()
# ​
# 		# Repeat until queue is empty
# 		while q.size() > 0:

# 			# Dequeue first vert
# 			v = q.dequeue()
# ​
# 			# If it's not visited:
# 			if v not in visited:
# 				print(v)
# ​
# 				# Mark visited
# 				visited.add(v)
# ​
# 				for next_vert in self.get_neighbors(v):
# 					q.enqueue(next_vert)
# * ============================ Everything above this is Notes!! =====================================
import collections

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self, V):
        self.vertices = {}
        self.V = V
        self.adj = [[] for i in range(V)]

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()  # set of edges

    def add_edge(self, v1, v2):
        # adding edge from v1 to v2
        # if they are both in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in the graph")
        self.adj[v1].append(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # Breadth-First-Traversal
        q = Queue()
        q.enqueue(starting_vertex_id)    # adding the first vertex to the queue
        visited = set()    # Keep track of visited nodes
        while q.size() > 0:   # Repeat until queue is empty
            v = q.dequeue()   # Dequeue first vertex or node
            if v not in visited:   # if its not visited
                print(v)
                visited.add(v)     # mark as visited
                # getting all the neighbors of the last visited vertex
                for next_vert in self.get_neighbors(v):
                    # adding the neighboring vertexes to the queue
                    q.enqueue(next_vert)

    def dft(self, starting_vertex_id):
        # Depth-First-Traversal
        V = starting_vertex_id
        s = Stack()
        s.push(V)
        visited = [False for i in range(self.V)]
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.append(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex):
        pass

    def bfs(self, starting_vertex, destination_vertex):
        # Breadth-First-Search
        visited, queue = set(), collections.deque([starting_vertex])
        visited.add(starting_vertex)
        while queue:
            vertex = queue.pop()
            if vertex == destination_vertex:
                return
            print(vertex)
            for neighbor in self.vertices[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        # visited = [False] * (len(self.vertices))
        # q = []
        # q.append(starting_vertex)
        # visited[starting_vertex] = True
        # while q:
        #     s = q.pop(0)
        #     print(s, end = " ")
        #     for i in self.vertices[s]:
        #         print("This ==> ", visited[i])
        #         if visited[i] == False:
        #             q.append(i)
        #             visited[i] = True

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph(10)  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    graph.bfs(1, 6)

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
