
if __name__ == '__main__':
    n=int(input())
    items=[]
    for i in range(n):
        x=int(input())
        items.append(x)
    def strictlyIncreasing(itms):
        return all(i<j for i,j in zip(itms,itms[1:]))
    def strictlyDecreasing(itms):
        return all(i>j for i,j in zip(itms,itms[1:]))
    lb=0
    ub=len(items)
    mid = ((lb+ub)//2)
    seq1 = items[lb:mid]
    seq2 = items[mid:ub]
    res1 = strictlyDecreasing(seq1)
    res2 = strictlyIncreasing(seq2)
    def check():
        global lb, ub, mid, seq1,seq2,res1,res2
        while(lb<ub):
            if res1 == True and res2 == True:
                print(True)
                break
            elif res1 == False and res2 == True:
                ub = mid
                mid = (lb+ub)//2
                seq1 = items[lb:mid]
                seq2 = items[mid:ub]
                res1 = strictlyDecreasing(seq1)
                res2 = strictlyIncreasing(seq2)
            elif res1 == True and res2 == False:
                lb = mid
                mid = (lb+ub)//2
                seq1 = items[lb:mid]
                seq2 = items[mid:ub]
                res1 = strictlyDecreasing(seq1)
                res2 = strictlyIncreasing(seq2)
            else:
                print(False)
                break
    check()
