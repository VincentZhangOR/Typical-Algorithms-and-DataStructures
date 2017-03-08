from collections import defaultdict
from heapdict import heapdict

def shortest(V,E):
	edges = defaultdict(list)
	for (u, v, cost) in E:
		edges[u].append((v, cost))
		edges[v].append((u, cost))
	d = heapdict()
	back = defaultdict(lambda: -1)
	d[0] = 0
	for i in xrange(1,V):
		d[i] = float("inf")
	while True:
		v, dis = d.popitem()
		if v == V-1:
			return dis, solution(back,v)
		for (u,cost) in edges[v]:
			if u in d and dis + cost < d[u]:
				d[u] = dis + cost
				back[u] = v

def solution(back, v):
	if v <= 0:
		return [0]
	return solution(back, back[v]) + [v]
	
if __name__=="__main__":
	print shortest(4, [(0,1,3), (1,2,3), (2,3,3),(0,3,8),(0,2,4)])
	print shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])