import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# n : 노드 수, m : 간선 수
n, m, start = map(int, input().split())

# 각 노드 연결 정보를 담은 리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 다익스트라 알고리즘 구현
def dijkstra(start):
    q = []

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 비어 있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드들을 화인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

cnt, max_distance = 0, 0

for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)

# 시작 노드 제외 cnt - 1
print(cnt - 1, max_distance)

