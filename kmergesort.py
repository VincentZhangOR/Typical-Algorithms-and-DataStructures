import heapq

# Time complexity: O(nlogn)

def merge(lst):
	if lst==[]:
		return []
	h=[]
	res=[]
	for i in xrange(len(lst)):
		heapq.heappush(h,(lst[i][0],i,0))
	while h!=[]:
		temp=heapq.heappop(h)
		res.append(temp[0])
		if len(lst[temp[1]])>temp[2]+1:
			heapq.heappush(h,(lst[temp[1]][temp[2]+1],temp[1],temp[2]+1))
	return res

def kmergesort(a,k):
	n=len(a)
	if n<=1:
		return a
	lst=[]
	if n<=k:
		for x in a:
			lst.append([x])
		return merge(lst)
	num=n//k
	m=n%k
	left=0
	if m!=0:
		right=num+1
		m-=1
	else:
		right=num
	for i in xrange(k):
		lst.append(kmergesort(a[left:right],k))
		left=right
		if m>0:
			right+=num+1
			m-=1
		else:
			right+=num
	return merge(lst)
	
if __name__=="__main__":
	print kmergesort([4,1,5,2,6,3,7,0], 3) 
	print kmergesort([4,1,5,2,6,3,7,0], 4)
	print kmergesort([4,1,5,2,6,3,7,0], 5)
	print kmergesort([4,1,5,2,6,3,7,0], 2) 
	print kmergesort([4,1,5,2,6,3,7,0], 8)
	print kmergesort(range(1000,0,-1),17)