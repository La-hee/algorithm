import heapq

def result(when) :
    when = sorted(when, key = lambda x : x[0])
    heap = []
    MaxNum = 0

    for s, e in when :
        while heap and heap[0] <= s :
            heapq.heappop(heap)
        
        heapq.heappush(heap, e)
        #반드시 최종 힙의 길이가 최소지 않을 가능성이 있으므로 max를 통해 값을 찾아줌
        MaxNum = max(MaxNum, len(heap))

    return MaxNum


def main() :
    t = int(input())

    for i in range(0, t) :
        n = int(input())
        start = list(map(int, input().split()))
        end = list(map(int, input().split()))

        when = []
        for j in range(0, n) :
            when.append((start[j], end[j]))
        
        print(result(when))

if __name__ == "__main__" :
    main()
