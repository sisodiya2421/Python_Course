n=int(input())
cases = []
for i in range(n):
    cases.append(input().split(" "))
def isPrime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if (x%2 == 0 or x%3 ==0):
        return False
    i = 5
    while(i * i <= x):
        if (x % i == 0 or x % (i + 2) == 0):
            return False
    return True
for items in cases:
    for j in range(int(items[0]),int(items[1])+1):
        print(j)
        print(type(j))
        if isPrime(j) == True:
            print(j,end=" ")
    print(end="\n")
