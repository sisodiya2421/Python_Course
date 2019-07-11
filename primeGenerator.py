n=int(input())
cases = []
for i in range(n):
    cases.append(input().split(" "))
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True
for items in cases:
    for j in range(int(items[0]),int(items[1])+1):
        if isPrime(j) == True:
            print(j,end=" ")
    print(end="\n")
