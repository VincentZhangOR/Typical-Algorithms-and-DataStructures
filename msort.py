def mergesort(nums):
	if nums==[]:
		return []
	if len(nums)==1:
		return nums
	mid=len(nums)/2
	left=mergesort(nums[:mid])
	right=mergesort(nums[mid:])
	i=0
	j=0
	ans=[]
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			ans.append(left[i])
			i+=1
		else:
			ans.append(right[j])
			j+=1
	if i<len(left):
		ans+=left[i:]
	if j<len(right):
		ans+=right[j:]
	return ans