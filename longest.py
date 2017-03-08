def longest(tree):
	return helper(tree)[0]

def helper(tree):
	path=0
	height=0
	if tree==[]:
		return (0,0)
	elif tree[0]==[] and tree[2]==[]:
		return (0,1)
	else:
		leftP,leftH=helper(tree[0])
		rightP,rightH=helper(tree[2])
		path=max(leftP,rightP,leftH+rightH)
		height=max(leftH,rightH)+1
	return (path,height)