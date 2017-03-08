def find(A):
	A.sort()
	ans=[]
	for x in A:
		left=0
		right=len(A)-1
		while left<right:
			if A[left]==x:
				left+=1
				continue
			if A[right]==x:
				right-=1
				continue
			if A[left]+A[right]==x:
				ans.append((A[left],A[right],x))
				left+=1
				right-=1
			elif A[left]+A[right]<x:
				left+=1
			else:
				right-=1
	return ans

if __name__=="__main__":
	print find([])
	print find([1])
	print find([1,2])
	print find([1,2,3])
	print find([1, 4, 2, 3, 5])