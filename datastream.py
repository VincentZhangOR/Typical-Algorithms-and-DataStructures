import heapq

def ksmallest(k,a):
	if k<=0:
		return []
	n=len(a)
	h=[]
	res=[]
	for x in a:
		if len(h)<k:
			heapq.heappush(h,0-x)
		else:
			if 0-x>h[0]:
				heapq.heappop(h)
				heapq.heappush(h,0-x)
	while h!=[]:
		res.append(0-heapq.heappop(h))
	return res[::-1]

if __name__=="__main__":
	print ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
	print ksmallest(3, xrange(1000000, 0, -1))
	print ksmallest(100, xrange(1000,0,-2))
	print ksmallest(0, xrange(1000,0,-2))
	print ksmallest(500, xrange(1000,0,-2))