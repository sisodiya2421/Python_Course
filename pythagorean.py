n = int(input())
sample = []
for i in range(n):
    x = int(input())
    sample.append(x)
def condition(a,b):
    return a**2+b**2
items = [[[(i,j) for j in range(i,n+1) if condition(i,j) == n] for i in range(n) if [(i,j) for j in range(i,n+1) if condition(i,j) == n]] for n in sample if [[(i,j) for j in range(i,n+1) if condition(i,j) == n] for i in range(n) if [(i,j) for j in range(i,n+1) if condition(i,j) == n]]]
for i in items:
    print(i)
