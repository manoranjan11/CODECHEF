# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    mod=1000000007
    sum=2*arr[0]
    p=1
    ans=0
    for i in range(1,n+1):
        p=(2*p)%mod
        ans=(2*ans + sum*arr[i])%mod
        sum=(sum+p*arr[i])%mod
    print(ans)
