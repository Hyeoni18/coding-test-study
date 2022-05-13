# DFS, 깊이 우선 탐색, 스택 자료구조(혹은 재귀 함수)를 이용한다.
# 구체적인 동작 과정
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 2번의 과정을 수행할 수 없을 때까지 반복한다.

# <예제>
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: # 인접한 노드가 방문되지 않은 상태라면 방문한다.
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# 일반적으로 그래프 문제가 출제되면, 노드의 번호가 1번부터 시작하기에 index = 0 에 대한 정보는 비워놓는다.
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visites = [False] * 9
# 정의된 DFS 함수 호출
dfs(graph, 1, visites)