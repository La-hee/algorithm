def liquid(L, total, n) :
    L = sorted(L, key = lambda x : x[0] / x[1])

    w = 0

    for i in range(0, n) :
        if total <= L[i][0] :
            w += total * L[i][1] // L[i][0]
            return w
        
        else :
            w += L[i][1]
            total -= L[i][0]

    return w



def main() :
    t = int(input())

    for i in range(0, t) :
        n = int(input())
        v = list(map(int, input().split()))
        w = list(map(int, input().split()))
        total = int(input())

        L = []

        for j in range (0, n) :
            L.append((v[j], w[j]))

        print(liquid(L, total, n))


if __name__ == "__main__" :
    main()