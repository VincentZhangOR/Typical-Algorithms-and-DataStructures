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

def find(A, x, k):
	if k>=len(A):
		return A
	diff=[]
	for y in A:
		diff.append(abs(y-x))
	target=qselect(k,diff)
	count=0
	i=0
	ans=[]
	while count<k:
		if diff[i]<=target:
			ans.append(A[i])
			count+=1
		i+=1
	return ans

if __name__=="__main__":
	print find([4,1,3,2,7,4], 5.2, 2)
	print find([4,1,3,2,7,4], 6.5, 3)
	print find([],4,2)
	print find([4],4,2)
	print find([4],4,0)