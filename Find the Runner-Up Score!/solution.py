if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ar=list(arr)
    ar.sort()
    max=ar[len(ar)-1]
    count=0
    for i in ar:
        if(i==max):
            count+=1
    runnerup=ar[len(ar)-1-count]
    print(runnerup)
