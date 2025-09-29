def pow(n, k) :
   if k == 0 :
       return 1
   
   elif k == 1 :
       return n % 25919
   
   #k가 짝수인 경우
   elif k % 2 == 0 :
      k = k // 2
      n = n % 25919
      half = pow(n, k)
      return (half * half) % 25919
   
   #n이 홀수인 경우
   else :
       k = (k-1) // 2
       n = n % 25919
       half = pow(n, k)
       return (half * half *  n) % 25919
       

def main() :
    t = int(input())
    for i in range(0, t) :
        n, k = map(int, input().split())
        result = pow(n, k)
        print(result)




if __name__  == "__main__" :
    main()