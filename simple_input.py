from functools import reduce
try:
	s=[]
	while True:
		n=int(input())
		s.append(n)
		total = reduce((lambda x,y: x+y), s)
		if total<0:
			break;
	for i in range(len(s)-1):
		print(s[i])
except:
	pass
