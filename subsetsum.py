def subset(X, target) :
    if target == 0 :
        return 'Yes'
    
    elif target < 0 :
        return 'No'
    
    elif target > 0 and len(X) == 0 :
        return 'No'
    
    else :
        #부분집합에 포함되는 경우
        include = subset(X[1:], target-X[0])
        #부분집합에 포함되지 않는 경우
        exclude = subset(X[1:], target)

        if include == 'Yes' or exclude == 'Yes' :
            return 'Yes'
        else :
            return 'No'


def main() :
    t = int(input())
    for i in range(0,t) :
        nX = int(input())
        X = list(map(int, input().split()))
        target = int(input())
        print(subset(X, target))

if __name__ == "__main__" :
    main()

