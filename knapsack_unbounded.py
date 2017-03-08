import random

# bottem-up
def best(w,a):
	d={0:0}
	n=len(a)
	track={}
	for x in xrange(1,w+1):
		d[x],temp1,temp2=0,0,0
		for i in xrange(n):
			if x>=a[i][0]:
				temp1 = d[x-a[i][0]]+a[i][1]
				if temp1>d[x]:
					temp2 = i
					d[x] = temp1
		track[x] = (1,-1) if d[x]==d[x-1] else (0,temp2)
		if x>=a[temp2][0] and d[x-1]==d[x-a[temp2][0]]+a[temp2][1]:
			lst1=solution(x,a,track)
			track[x]=(0,temp2)
			lst2=solution(x,a,track)
			if cmp(lst1,lst2)>=0:
				track[x]=(1,0)
	return d[w],solution(w, a, track)

def solution(i,a,track,res=None):
	if res==None:
		res=[0 for x in xrange(len(a))]
	if i<=0:
		return res
	if not track[i][0]:
		res[track[i][1]]+=1
	return solution(i-1,a,track,res) if track[i][0] else solution(i-a[track[i][1]][0],a,track,res)

# top-down:
def tbest(w,a):
	n=len(a)
	track={}
	
	def top_down(x, d=None):
		if d==None:
			d={0:0}
		if x in d:
			return d[x]
		d[x],temp1,temp2=0,0,-1
		for i in xrange(n):
			if x>=a[i][0]:
				#temp1 = max(top_down(x-1), top_down(x-a[i][0])+a[i][1])
				temp1 = top_down(x-a[i][0],d)+a[i][1]
				if temp1>d[x]:
					temp2 = i
					d[x] = temp1
		track[x] = (1,-1) if d[x]==top_down(x-1,d) else (0,temp2)
		if x>=a[temp2][0] and d[x-1]==d[x-a[temp2][0]]+a[temp2][1]:
			lst1=solution(x,a,track)
			track[x]=(0,temp2)
			lst2=solution(x,a,track)
			if cmp(lst1,lst2)>=0:
				track[x]=(1,0)
		return d[x]

	return top_down(w), solution(w, a, track)

# Exhaustive solution: 
def Ebest(w,a):
	if w<=0:
		return 0
	res=0
	for x in a:
		if x[0]<=w:
			res=max(res,Ebest(w-x[0],a)+x[1])
	return res

if __name__=="__main__":
	print best(3, [(2, 4), (3, 5)])		#(5, [0, 1])
	print best(3, [(1, 5), (1, 5)])		#(15, [3, 0])
	print best(3, [(1, 2), (1, 5)])		#(15, [0, 3])
	print best(3, [(1, 2), (2, 5)])		#(7, [1, 1])
	print best(58, [(5, 9), (9, 18), (6, 12)])		#(114, [2, 4, 2])
	print best(92, [(8, 9), (9, 10), (10, 12), (5, 6)])		#(109, [1, 1, 7, 1])
	print Ebest(58, [(5, 9), (9, 18), (6, 12)])
	print tbest(58, [(5, 9), (9, 18), (6, 12)])		#(114, [2, 4, 2])
	print tbest(92, [(8, 9), (9, 10), (10, 12), (5, 6)])		#(109, [1, 1, 7, 1])