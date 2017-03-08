from collections import defaultdict

def longest(V, E):
	if V == 0:
		return 0,[]
	if V == 1:
		return 0,[0]
	edgesTail = {}
	edgesHead = {}
	for (u, v) in E:
		if v not in edgesTail:
			edgesTail[v] = {u}
		else:
			edgesTail[v].add(u)
		if u not in edgesHead:
			edgesHead[u] = {v}
		else:
			edgesHead[u].add(v)
	free = set(range(V))
	for x in edgesTail:
		free.remove(x)
	
	tsort = order(V, free, edgesTail, edgesHead)
	if tsort == None:
		return None
	d = defaultdict(int)
	back = defaultdict(lambda: -1)
	for i in xrange(V):
		node = tsort[i]
		if node in edgesHead:
			for x in edgesHead[node]:
				temp = d[node] + 1
				if temp > d[x]:
					d[x] = temp
					back[x] = node
	endNum, endNode = 0, 0
	for x in d:
		if d[x] > endNum:
			endNum = d[x]
			endNode = x
	return d[tsort[V-1]], solution(endNode, back)

def solution(i, back):
	if i < 0:
		return []
	return solution(back[i], back) + [i]

def order(V, free, edgesTail, edgesHead): 
	res = []
	while free:   
		cur = free.pop()
		res.append(cur)
		if cur not in edgesHead:
			continue
		for x in edgesHead[cur]:
			if x in edgesTail:
				edgesTail[x].remove(cur)
				if len(edgesTail[x]) == 0:
					free.add(x)
					del edgesTail[x]
	if len(edgesTail) != 0:
		return None 
	return res

if __name__=="__main__":
	print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
	print longest(0,[])
	print longest(2,[(0,1)])
	print longest(4,[(0,1),(1,2),(2,3)])
	print longest(4,[(0,1),(1,2),(2,3),(0,3),(1,3)])
	print longest(4,[(1,2),(2,3),(0,3),(1,3)])
	print longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
	print longest(8,[(0,5),(5,4),(5,7),(5,3),(7,6),(3,2),(2,1)])