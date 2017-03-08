import time

#Catalan number

#method 1: O(n^2)
def bsts1(n):
	d=[0 for x in xrange(n+1)]
	d[0]=1
	for i in xrange(1,n+1):
		for j in xrange(1,i+1):
			d[i]+=(max(d[j-1],1))*(max(d[i-j],1))
	return d[n]
#method 2: O(n)
def bsts(n,d={}):
	d[0]=1
	for i in xrange(1,n+1):
		d[i]=2*(2*i-1)*d[i-1]/(i+1)
	return d[n]

if __name__=="__main__":
	print bsts(3)
	print bsts(5)
	print bsts1(100)==bsts(100),bsts(100)
	n=100
	while n<=100000:
		start=time.time()
		bsts(n)
		end=time.time()
		print n,end-start
		n*=10
		'''
		start=time.time()
		bsts1(n)
		end=time.time()
		print n,end-start
		n*=10
		'''