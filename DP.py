def editDistance(s1, s2):
    ed = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0:
                ed[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                ed[i][j] = ed[i-1][j-1]
            else:
                ed[i][j] = abs(j-i) + min(ed[i-1][j-1], ed[i-1][j], ed[i][j-1])
    return ed[-1][-1]

s1 = 'geek'
s2 = 'gesek'
print(editDistance(s1, s2))