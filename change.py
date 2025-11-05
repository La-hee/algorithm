def charge(money) :
    result = 0
    
    result += money // 50000
    money = money % 50000

    result += money // 10000
    money = money % 10000

    result += money // 5000
    money = money % 5000

    result += money // 1000
    money = money % 1000

    return result





def main() :
    t = int(input())

    for i in range(0, t) :
        money = int(input())
        print(charge(money))


if __name__ == '__main__' :
    main()