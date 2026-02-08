
def  virus(v, graph, infect) :
    bag = [v] #스택
    infect[v] = True #현재 노드 감염 처리

    while bag : #스택에 남아있는 동안
        u = bag.pop() #현재 노드를 꺼냄
        for v in graph[u] : #현재 노드와 연결된 다른 노드들 모두
            if not infect[v] : #감염되어 있지 않다면 감염시키고
                infect[v] = True
                bag.append(v) #그것과 연결된 노드를 스택에 추가함

def main() :
    t = int(input())

    #t번만큼 테스트 반복
    for i in range(0, t) :
        n, m = map(int, input().split())

        #그래프 생성 및 각 간선이 잇고 있는 노드 정보 추가
        graph = [[] for k in range(n)]

        for j in range(0, m) :
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        
        #감염 여부 확인
        infect = [False] * n
        hack = 0 #필요한 해킹 횟수

        #서버를 돌면서 감염에 필요한 횟수를 구함
        for j in range(n) :
            #감염되지 않은 서버를 발견한 경우
            if not infect[j] :
                hack += 1 #공격 횟수 +1
                virus(j, graph, infect)
        
        print(hack)


if __name__ == "__main__" :
    main()