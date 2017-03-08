def sorted(t):
	if t == []:
		return []
	ans=[]
	for x in t:
		if isinstance(x,list):
			ans+=sorted(x)
		else:
			ans.append(x)
	return ans

def _search(tree, x):
	if tree == []:
		return tree
	if tree[1]==x:
		return tree
	elif tree[1]>x:
		return _search(tree[0],x)
	else:
		return _search(tree[2],x)

def search(t,x):
	if _search(t,x)==[]:
		return False
	else:
		return True

def insert(t,x):
	if _search(t,x)==[]:
		if t==[]:
			t.append([])
			t.append(x)
			t.append([])
		elif t[1]>x:
			insert(t[0],x)
		else:
			insert(t[2],x)

def sort(nums):
	if nums == []:
		return []
	pivot = nums[0]
	left = [x for x in nums if x < pivot]
	right =[x for x in nums[1:] if x >= pivot]
	return [sort(left)] + [pivot] + [sort(right)]


'''
Time Complexities:
sort:
	best case: O(nlogn)
	worst case: O(n2)
	average case: O(nlogn)
sorted:
	best case: O(n)
	worst case: O(n)
	average case: O(n)
search:
	best case: O(logn)
	worst case: O(n)
	average case: O(logn)
insert:
	best case: O(logn)
	worst case: O(n)
	average case: O(logn)