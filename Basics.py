from collections import defaultdict


class Graph:
    def __init__(self):
        self.G = defaultdict(list)

    def addEdge(self, u, v):
        self.G[u].append(v)
        self.G[v].append(u)

    def BFS(self, start):
        visited = []
        q = []

        q.append(start)
        visited.append(start)

        while q:
            node = q.pop(0)
            print(node)

            for i in self.G[node]:
                if i not in visited:
                    q.append(i)
                    visited.append(i)

    def _DFSutil(self, node, visited):
        if node not in visited:
            print(node)
            visited.append(node)
            for i in self.G[node]:
                self._DFSutil(i, visited)


    def DFS(self, start):
        visited = []
        self._DFSutil(start, visited)


g = Graph()
g.addEdge(1,7)
g.addEdge(7,10)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(1,4)
g.addEdge(4,5)
# g.addEdge(5,1)
g.addEdge(4,8)
g.addEdge(8,9)

g.DFS(1)
