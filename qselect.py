import random

def qselect(n, nums):
	if len(nums)==1:
		return nums[0]
	length = len(nums)
	if n>length or nums==[]:
		return None
	pivot = random.randint(0,length-1)
	left = [x for x in nums if x < nums[pivot]]
	right =[x for x in nums[:pivot]+nums[pivot+1:] if x >= nums[pivot]]
	if n<=len(left):
		return qselect(n, left)
	elif n==len(left)+1:
		return nums[pivot]
	else:
		return qselect(n-len(left)-1, right)


'''
best-case: O(n). When the first pivot is the select number, we just need to partition once.
worst-case: O(n2). When every time we choose the biggest number as pivot, but the select number is the smallest one (or sysmatrically choosing smallest number as pivot, but the select number is the biggest).
average-case: O(n).
'''