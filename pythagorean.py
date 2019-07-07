try:
    n = int(input())
    sample = []
    for i in range(n):
        x = int(input())
        sample.append(x)

    def condition(a,b,num):
        if a**2 + b**2 == num:
            return True
        else:
            return False
    for i in sample:
        for j in range(i):
            for k in range(j+1,i+1):
                pairs=[]
                if condition(j,k,i) is True:
                    pairs.append(j)
                    pairs.append(k)
                    print(tuple(pairs),end=" ")
        print(end="\n")
except:
    pass
