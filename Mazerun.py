import sys
from collections import deque

INF = float('inf') #파이썬의 무한대 표현 방식
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(n, m, maze) : 
    dist = [[INF] * m for i in range(n)] #거리 테이블 무한대로 초기화
    startx, starty = 0,0
    dist[startx][starty] = 0 #시작하는 칸 1로 초기화

    queue = deque()
    queue.append((startx, starty))

    while queue :
        x, y = queue.popleft()

        #도착점에 도달 시 거리 반환
        if x == n-1 and y == m-1 :
            return dist[x][y]
        
        #상하좌우 4방향 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            #벽인지 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            if maze[nx][ny] == 0 :
                continue

            if dist[nx][ny] > dist[x][y] + 1 :
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    
    return -1





def main() :
    t = int(input())

    for i in range(t) :
        n, m = map(int, input().split())

        maze = []
        for j in range(n) :
            maze.append(list(map(int, input().split())))
        
        print(bfs(n, m, maze))

if __name__ == "__main__" :
    main()