def util(boggle, word, index, i, j):
    neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1),
                 (i, j-1), (i, j+1),
                 (i+1, j-1), (i+1, j), (i+1, j+1)]

    for r, c in neighbors:
        if 0 <= r < len(boggle) and 0 <= c < len(boggle[0]):
            if boggle[r][c] == word[index]:
                if index == len(word) - 1:
                    return True
                return util(boggle, word, index+1, r, c)
    return False


def searchWord(boggle, word):
    for i in range(len(boggle)):
        for j in range(len(boggle[0])):
            if boggle[i][j] == word[0]:
                return util(boggle, word, 1, i, j)


if __name__=="__main__":
    words = ["GEEKS", "FOR", "QUIZ", "GO"]
    boggle = [['G', 'I', 'Z'],
              ['U', 'E', 'K'],
              ['Q', 'S', 'E']]
    ans = []
    for w in words:
        if searchWord(boggle, w):
            ans.append(w)

    print(ans)