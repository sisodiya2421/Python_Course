try:
    n = int(input())
    k = n-1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print("*"*k,end="")
        k -= 1
        print(end="\n")
except:
    pass
