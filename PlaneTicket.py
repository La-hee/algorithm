import sys
import heapq

INF = float('inf')

def dijk(start, n, graph) :
    dist = [INF] * n
    dist[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap :
        d, u = heapq.heappop(heap)

        if d > dist[u] :
            continue

        for v, w in graph[u] : 
            if dist[v] > dist[u] + w :
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    
    return dist

def main() :
    t = int(input())

    for i in range(t) :
        n, m = map(int, input().split())
        
        forward = [[] for k in range(n)]
        reverse = [[] for k in range(n)]
        edge = []

        for j in range(m) :
            u, v, w = map(int, input().split())
            forward[u].append((v, w))
            reverse[v].append((u, w))
            edge.append((u, v, w))

        start = dijk(0, n, forward)
        end = dijk(n-1, n, reverse)

        buget = INF
        
        for u, v, w in edge :
            if start[u] != INF and end[v] != INF : 
                current = start[u] + end[v]

                if current < buget :
                    buget = current
        
        print(buget)

if __name__ == "__main__" :
    main()
    

