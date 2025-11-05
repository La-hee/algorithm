def search(L, q) :
    left = 0
    right = len(L) - 1

    #리커젼을 하는 건 시간이 많이 걸리므로 반복문을 이용해 범위를 좁혀나감
    while left <= right :
        mid = (left + right) // 2
        if L[mid] == q :
            return mid
        elif L[mid] < q :
            left = mid + 1
        else :
            right = mid - 1
    #못 찾을 경우 -1 리턴
    return -1


def main() :
    t = int(input())
    for i in range(0, t) :
        result = []
        nL, nQ = map(int, input().split())
        L = list(map(int, input().split()))
        Q = list(map(int, input().split()))

        for q in Q :
           index = search(L, q)
           result.append(index)
        print(" ".join(map(str, result)))

if __name__ == "__main__" :
    main()


