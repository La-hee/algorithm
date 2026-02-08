
def postorder(u, graph, visit, order) :
    visit[u] = True

    for v, w in graph[u] :
        if not visit[v] :
            postorder(v, graph, visit, order)
    
    #자식들 처리 이후 나를 넣음
    order.append(u)




def main() :
    t = int(input())

    for i in range(t) :
        n, m = map(int, input().split())
        
        #그래프 추가
        graph = [[] for k in range(n) ]

        for j in range(m) :
            u, v, w = map(int, input().split())
            graph[u].append((v, w))
        
        #위상정렬
        visit = [False] * n
        order = []

        for j in range(n) :
            if not visit[j] :
                postorder(j, graph, visit, order)
        
        order.reverse()

        INF = -float('inf')
        dist = [INF] * n
        dist[0] = 0

        for u in order :
            if dist[u] == INF :
                continue

            for v, w in graph[u] :
                if dist[v] < dist[u] + w :
                    dist[v] = dist[u] + w
        
        
        print(dist[n-1])

if __name__ == "__main__" :
    main()
