def conquer(graph):
    row = len(graph)
    col = len(graph[0])

    def dfs(i, j):
        nonlocal component, edge
        row = len(graph)
        col = len(graph[0])
        if i == 0 or i == row-1 or j == 0 or j == col-1:
            edge = True

        graph[i][j] = '-'
        component.append((i,j))

        if i+1 < row and graph[i+1][j] == 'O':
            dfs(i+1, j)
        if i-1 >= 0 and graph[i-1][j] == 'O':
            dfs(i-1, j)
        if j + 1 < col and graph[i][j+1] == 'O':
            dfs(i, j+1)
        if j - 1 >= 0 and graph[i][j-1] == 'O':
            dfs(i, j-1)


    for i in range(row):
        for j in range(col):
            if graph[i][j] == 'O':
                component = []
                edge = False
                dfs(i, j)
                if not edge:
                    for m,n in component:
                        graph[m][n] = 'X'

    return graph

graph = [['O', 'X', 'X', 'O'],
         ['X', 'O', 'O', 'X'],
         ['X', 'O', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X']]

print(conquer(graph))


