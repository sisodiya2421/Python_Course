try:
    n=int(input())
    p=0
    for i in range(2,n//2):
        if n%i == 0:
            p=1
    if p == 0:
        print("Prime")
    else:
        print("Not Prime")
except:
    pass
