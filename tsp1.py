from collections import defaultdict
from itertools import combinations

def tsp(a):
	n = len(a)
	res = float("inf")
	d = defaultdict(lambda: float("inf"))
	back = defaultdict(lambda: -1)
	if n <= 1:
		return 0
	for i in xrange(1,n):
		for sub in combinations(range(1,n),i):
			subSet = set(sub)
			if i==1:
				d[sub, sub[0]] = a[0][sub[0]] if a[0][sub[0]] > 0 else float("inf")
				back[sub, sub[0]] = 0 if a[0][sub[0]] > 0 else -1
			for x in subSet:
				oldSubSet = subSet - {x}
				oldSub = tuple(oldSubSet)
				for k in oldSubSet:
					temp = d[oldSub, k] + a[k][x] if a[k][x] > 0 else float("inf")
					if temp < d[sub, x]:
						d[sub, x] = temp
						back[sub, x] = k if d[sub, x] < float("inf") else -1
					if sub == tuple(range(1,n)):
						temp = d[sub, x] + a[x][0] if a[x][0] > 0 else float("inf")
						if temp < res:
							res = temp
							back[tuple(range(0,n)),0] = x
	return res, solution(a, back, tuple(range(0,n)), 0, 0)

def solution(a, back, i, x, flag):
	if x == 0 and flag > 0:
		return [0]
	flag += 1
	prev = back[i,x]
	subSet = set(i)
	oldSubSet = subSet - {x}
	return solution(a, back, tuple(oldSubSet), prev, flag) + [x]

if __name__ == "__main__":
	a = [[0,1,1,4],[1,0,2,1],[1,2,0,1],[4,1,1,0]]
	b = [[0,1,3],[1,0,2],[3,2,0]]
	c = [[0,10,1,1],[10,0,1,1],[1,1,0,10],[1,1,10,0]]
	print tsp(a)
	print tsp(b)
	print tsp(c)