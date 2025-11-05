def Long(L, n) :

    #base case, 전체를 1로 초기화해줌
    Result = [1] * n

    for i in range(1, n) :
        for j in range(0,i) :
            #L[i]가 L[j]보다 크고, Result[i]가 Result[j]+1보다 작은 경우
            if L[i] > L[j] and Result[i] < Result[j] + 1:
                Result[i] = Result[j]+1
    
    return max(Result)

def main() :
    t = int(input())

    for i in range(0, t) :
        n = int(input())
        L = list(map(int, input().split()))

        print(Long(L, n))

if __name__ == "__main__" :
    main()
