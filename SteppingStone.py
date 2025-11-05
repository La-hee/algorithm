def stone(n) :
    result = 0

    s = [0] * (n+1)

    #base case, INDEX error방지를 위해 조건을 넣었음.
    s[0] = 1
    if n >= 1 : s[1] = 1
    if n >= 2 : s[2] = 1
    if n >= 3 : s[3] = 2
    if n >= 4 : s[4] = 4

    #N-1~N-4번째 돌을 밟는 경우의 수를 다 더해서 I번째를 구하고 배열에 저장.
    for i in range(5, n+1) :
        s[i] = (s[i-1] + s[i-3] + s[i-4]) % 25919
    
    return s[n]


def main() :
    t = int(input())

    for i in range(0, t) :
        n = int(input())
        print(stone(n))

if __name__ == "__main__" :
    main()
