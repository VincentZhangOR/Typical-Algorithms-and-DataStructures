import bisect

def find(A, x, k):
	if len(A)<=k:
		return A
	pos=bisect.bisect(A,x)
	if pos==-1:
		return A[:k]
	if pos==len(A)-1:
		return A[len(A)-k:]
	left=pos
	right=pos+1
	while k>0:
		if left<0:
			right+=1
		elif right>len(A)-1:
			left-=1
		else:
			if abs(A[left]-x)<=abs(A[right]-x):
				left-=1
			else:
				right+=1
		k-=1
	return A[left+1:right]

if __name__=="__main__":
	print find([1,2,3,4,4,7], 5.2, 2)
	print find([1,2,3,4,4,7], 6.5, 3)
	print find([1,2,3,4,4,6,6], 5, 3)
	print find([1,2,3,4,4,5,6], 4, 5)
	print find([],4,2)
	print find([4],4,2)
	print find([4],4,0)