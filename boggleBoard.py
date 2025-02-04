dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
n = len(dictionary)
M = 3
N = 3

def isWord(Str):
    return any((Str == dictionary[i]) for i in range(n))

def findWordsUtil(boggle, visited, i, j, Str):
    visited[i][j] = True
    Str = Str + boggle[i][j]

    if (isWord(Str)):
        print(Str)

    row = i - 1
    while row <= i + 1 and row < M:
        col = j - 1
        while col <= j + 1 and col < N:
            if (row >= 0 and col >= 0 and not visited[row][col]):
                findWordsUtil(boggle, visited, row, col, Str)
            col+=1
        row+=1

    Str = f'{Str[-1]}'
    visited[i][j] = False

def findWords(boggle):
    visited = [[False for _ in range(N)] for _ in range(M)]

    Str = ""

    for i in range(M):
        for j in range(N):
            findWordsUtil(boggle, visited, i, j, Str)

boggle = [["G", "I", "Z"], ["U", "E", "K"], ["Q", "S", "E"]]

print("Following words of", "dictionary are present")
findWords(boggle)
