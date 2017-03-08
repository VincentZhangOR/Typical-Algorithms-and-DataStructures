# bottem-up
def best(w,a):
	n=len(a)
	d={(0,i):0 for i in xrange(n)}
	for j in xrange(w+1):
		d[(j,-1)]=0
	track={}
	for x in xrange(1,w+1):
		for i in xrange(n):
			d[(x,i)],temp1,temp2=0,0,0
			for j in xrange(0,a[i][2]+1):
				if x>=a[i][0]*j:
					temp1 = d[(x-a[i][0]*j,i-1)]+a[i][1]*j
					if temp1>d[(x,i)]:
						temp2 = j
						d[(x,i)] = temp1
				else:
					break
			track[(x,i)] = temp2
	return d[(w,n-1)],solution(w, a, n-1,track)

def solution(x,a,last,track,res=None):
	if res==None:
		res=[0 for j in xrange(len(a))]
	if x<=0 or last<0:
		return res
	if track[(x,last)]!=0:
		res[last]+=track[(x,last)]
	return solution(x,a,last-1,track,res) if track[(x,last)]==0 else solution(x-a[last][0]*track[x,last],a,last-1,track,res)

if __name__=="__main__":
	print best(3, [(2, 4, 2), (3, 5, 3)])		#(5, [0, 1])
	print best(3, [(1, 5, 2), (1, 5, 3)])		#(15, [2, 1])
	print best(3, [(1, 5, 1), (1, 5, 3)])		#(15, [1, 2])
	print best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])		#(130, [6, 4, 1])
	print best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])		#(236, [6, 7, 3, 7, 2])
	print best(58, [(5, 9,5), (9, 18,5), (6, 12,5)])		#(114, [2, 4, 2])