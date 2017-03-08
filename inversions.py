def num_inversions(nums):
	return helper(nums)[1]

def helper(nums):
	if len(nums)<=1:
		return nums,0
	mid=len(nums)/2
	lleft,nleft=helper(nums[:mid])
	lright,nright=helper(nums[mid:])
	i=0
	j=0
	res=[]
	ans=nleft+nright
	while i<len(lleft) and j<len(lright):
		if lleft[i]<=lright[j]:
			res.append(lleft[i])
			i+=1
		else:
			ans+=mid-i
			res.append(lright[j])
			j+=1
	return res+lleft[i:]+lright[j:],ans