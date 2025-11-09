import heapq

def big(homework) :
    homework = sorted(homework, key = lambda x : x[1])

    heap = []

    for s, d in homework :
        heapq.heappush(heap, s)

        if len(heap) > d :
            heapq.heappop(heap)
    
    return sum(heap)



def main() : 
    t = int(input())

    for t in range(0, t) :
        n = int(input())
        score = list(map(int, input().split()))
        due = list(map(int, input().split()))

        homework = []
        for i in range(0, n) :
            homework.append((score[i], due[i]))

        print(big(homework))


if __name__ == "__main__" :
    main()