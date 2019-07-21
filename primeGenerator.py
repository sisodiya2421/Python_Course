try:
    n=int(input())
    cases = []
    for i in range(n):
        cases.append(input().split(" "))

    for items in cases:
        def SieveOfEratosthenes(n):
            prime = [True for i in range(n+1)]
            p = int(items[0])
            while (p * p <= n):
                if (prime[p] == True):
                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1
            for p in range(int(items[0]), n):
                if prime[p]:
                    print(p)
        SieveOfEratosthenes(int(items[1]))
except:
    pass
