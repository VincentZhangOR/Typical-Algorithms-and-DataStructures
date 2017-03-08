def order(V, E): 
	if V <= 0:
		return []
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
	res = []
	free = set(range(V))
	for x in edgesTail:
		free.remove(x)
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
	print order(4,[(0,1),(1,2),(2,3)])
	print order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
	print order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
	print order(4, [(0,1), (1,2), (2,1), (2,3)])
	print order(0,[])