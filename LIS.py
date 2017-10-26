#Longest increasing sequence
import networkx as nx

n = input()
n = int(n)
array = [0]*n
for i in range(0,n):
    m = input()
    array[i] = int(m)

g = nx.DiGraph()
g.add_nodes_from(array)

#O(n^2)
for i in range(0,n-1):
    for j in range(i+1,n):
        if (array[i] < array[j]):
            g.add_edge(array[i],array[j])

L = [0]*n
#O(n^2)
for j in range(1,n):
    for i in range(0,j):
        if ((array[i],array[j]) in g.edges()):
            maxlen = L[i] + 1
            if (maxlen > L[j]):
                L[j] = maxlen
#Overall complexity O(n^2)
print(max(L))