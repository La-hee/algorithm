def long(S, n) :
    l = [[0] * (n+2) for i in range(n+2)]

    for i in range(1, n+1) :
        l[i][i] = 1

    for i in range(1, n) :
        if S[i-1] == S[i] :
            l[i][i+1] = 2
        else :
            l[i][i+1] = 1
    
    for length in range(3, n+1) :
        for i in range(1, n - length + 2) :
            j = i + length - 1
            if S[i-1] == S[j-1] :
                l[i][j] = max(l[i+1][j], l[i][j-1], l[i+1][j-1]+2)
            else :
                l[i][j] = max(l[i+1][j], l[i][j-1])
    
    return l[1][n]


    


def main() :
    t = int(input())

    for i in range(0,t) :
        n = int(input())
        S = list(input())

        print(long(S, n))

if __name__ == "__main__" :
    main()