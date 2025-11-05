def score(L, n, m):
    result = []

    #결과값을 저장할 배열 초기화
    for i in range(0, n):
        result.append([0] * m)
    
    result[0][0] = L[0][0]

    #첫 행들 초기화
    for i in range(1, n):
        result[i][0] = result[i-1][0] + L[i][0]

    #첫 열들 초기화
    for i in range(1, m):
        result[0][i] = result[0][i-1] + L[0][i]
    
    #전부 다 계산
    for i in range(1, n):
        for j in range(1, m):
            result[i][j] = max(result[i-1][j], result[i][j-1]) + L[i][j]
    
    return result[n-1][m-1]
    


def main() :
    t = int(input())
    for i in range(0, t) :
        matrix = []

        n, m = map(int, input().split())

        for i in range(0,n) :
            row = list(map(int, input().split()))
            matrix.append(row)
        
        print(score(matrix, n, m))


if __name__ == "__main__" :
    main()