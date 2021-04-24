# Given some adjacency list structre
g = []

maxScore = 0
visited = [False] * numNodes


def calculateMaxScore(s: node):
    visited[s] = True
    maxScore = max(s, maxScore)
    for connected in g[s]:
        if not visited[connected]:
            dfs(connected)
