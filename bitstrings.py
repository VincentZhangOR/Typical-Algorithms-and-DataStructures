import time

def num_no(n, d={}):
	d[0],d[-1]=1,1
	for i in xrange(1,n+1):
		d[i]=d[i-1]+d[i-2]
	return d[n]

def num_yes(n):
	return pow(2,n)-num_no(n)

def num_no2(n, d=None):
	if d==None:
		d={}
	if n in d:
		return d[n]
	#print "calculating",n
	d[n]=1 if n<=0 else num_no2(n-1,d)+num_no2(n-2,d)
	return d[n]

if __name__=="__main__":
	print "no:",num_no(100)
	print "yes:",num_yes(100)
	print "no:",num_no(101)
	print "yes:",num_yes(101)
	print num_no(100)==num_no2(100)
	n=100
	while n<=100000:
		start=time.time()
		num_no(n)
		end=time.time()
		print n,end-start
		n*=10