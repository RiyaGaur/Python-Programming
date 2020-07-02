n=int(input())
l=list(map(int,input().split()))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
all([n>0,rev==n])
