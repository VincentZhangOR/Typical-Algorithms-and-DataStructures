from collections import defaultdict
def best(X, a):
	n = len(a)
	if X == 0:
		return (0, [0 for x in xrange(n)])
	d = defaultdict(int)
	back = defaultdict(int)
	for x in xrange(1,X+1):
		for i in xrange(n):
			j = 0
			while j*a[i] <= x:
				if j*a[i] == x or d[x-j*a[i],i-1]:
					temp = d[x-j*a[i],i-1]+1
					if d[x,i] == 0 or temp < d[x,i]:
						d[x,i] = temp
						back[x,i] = j
				j += 1
	return (d[X,n-1],solution(X,n-1,a,back)) if d[X,n-1] else None

def solution(x,i,a,back):
	if i < 0:
		return []
	j = back[x,i]
	return solution(x-j*a[i],i-1,a,back)+[j]

if __name__=="__main__":
	print best(0,[1,2,3])
	print best(47, [6, 10, 15])
	print best(59, [6, 10, 15])
	print best(37, [4, 6, 15])
	print best(27, [4, 6, 15])
	print best(75, [4, 6, 15])
	print best(17, [2, 4, 6])
	print best(8,[5,6])
