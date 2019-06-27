s=[]
while(True):
    n=int(input())
    if n!=42:
        s.append(n)
        print("\n")
    else:
        break

for i in s:
    print(i)