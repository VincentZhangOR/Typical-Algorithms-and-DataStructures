from collections import defaultdict
from heapq import heappush, heappop

pair = {('A','U'),('U','A'),('G','C'),('C','G'),('G','U'),('U','G')}

def best(s):
	n = len(s)
	back = defaultdict(lambda: -1)
	def topdown(i,j,d=defaultdict(int)):
		if (i,j) in d or i >= j-1:
			return d[i,j]
		temp1, temp2, temp, index = 0, 0, 0, -1
		if (s[i],s[j-1]) in pair:
			temp1 = topdown(i+1,j-1,d) + 1
		for k in xrange(i+1,j):
			temp = topdown(i,k,d) + topdown(k,j,d)
			if temp > temp2:
				temp2 = temp
				index = k
		if temp1 >= temp2 and temp1 > 0:
			d[i,j] = temp1
			back[i,j] = i
		else:
			d[i,j] = temp2
			back[i,j] = index
		return d[i,j]
	return topdown(0,n), solution(s, back, 0, n)

def solution(s,back,i,j):
	if j <= i:
		return ''
	if j-1 == i:
		return '.'
	if back[i,j] == -1:
		return  '.' * (j-i)
	if back[i,j] == i:
		return '(' + solution(s, back, i+1, j-1) + ')'
	return solution(s, back, i, back[i,j]) + solution(s, back, back[i,j], j)

def total(s):
	n = len(s)
	def topdown(start, end, d = defaultdict(lambda: 1)):
		if (start, end) in d:
			return d[start,end]
		if end - start == 1:
			d[start, end] = 2 if (s[start],s[end]) in pair else 1
			return d[start, end]
		for i in xrange(start, end):
			for j in xrange(i+1,end+1):
				if (s[i],s[j]) in pair:
					d[start,end] += topdown(i+1,j-1,d) * topdown(j+1,end,d)
		return d[start,end]
	return topdown(0,n-1)

def kbest(s,k):
	n = len(s)
	def topdown(i, j, d = defaultdict(lambda: [])):
		if (i,j) in d:
			return d[i,j]
		if i >= j-2:
			if i == j:
				d[i,j].append((0,''))
			if i == j-1:
				d[i,j].append((0,'.'))
			if i == j-2:
				if (s[i],s[j-1]) in pair:
					d[i,j].append((1,'()'))
				d[i,j].append((0,'..'))
			return d[i,j]
		h, used = [], set()
		tempN, tempP = topdown(i+1,j,d)[0]
		tempP = '.' + tempP
		heappush(h,(-tempN,tempP,0,i+1,j,0,0))
		used.add((tempN, tempP))
		for m in xrange(i+1,j+1):
			if (s[i],s[m-1]) in pair:
				tempN1, tempP1 = topdown(i+1,m-1,d)[0]
				tempN2, tempP2 = topdown(m,j,d)[0]
				tempN = 1 + tempN1 + tempN2
				tempP = '(' + tempP1 + ')' + tempP2
				heappush(h,(-tempN,tempP,m,i+1,j,0,0))
				used.add((tempN, tempP))
		while len(d[i,j]) < k:
			if h == []:
				break
			v, struct, m, x, y, index1, index2 = heappop(h)
			d[i,j].append((-v,struct))
			if m == 0:
				if index1 + 1 < len(topdown(x,y,d)):
					tempN, tempP = topdown(x,y,d)[index1+1]
					tempP = '.' + tempP
					if (tempN,tempP) not in used:
						heappush(h,(-tempN,tempP,0,x,y,index1+1,0))
						used.add((tempN, tempP))
			else:
				if index1 + 1 < len(topdown(x,m-1,d)):
					tempN1, tempP1 = topdown(x,m-1,d)[index1+1]
					tempN2, tempP2 = topdown(m,y,d)[index2]
					tempN = 1 + tempN1 + tempN2
					tempP = '(' + tempP1 + ')' + tempP2
					if (tempN,tempP) not in used:
						heappush(h,(-tempN,tempP,m,x,y,index1+1,index2))
						used.add((tempN, tempP))
				if index2 + 1 < len(topdown(m,y,d)):
					tempN1, tempP1 = topdown(x,m-1,d)[index1]
					tempN2, tempP2 = topdown(m,y,d)[index2+1]
					tempN = 1 + tempN1 + tempN2
					tempP = '(' + tempP1 + ')' + tempP2
					if (tempN,tempP) not in used:
						heappush(h,(-tempN,tempP,m,x,y,index1,index2+1))
						used.add((tempN, tempP))
		return d[i,j]
	return topdown(0,n)