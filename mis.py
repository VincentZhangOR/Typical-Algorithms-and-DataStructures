import time

#max_wis: O(n)
def max_wis(a,d=None):
	if d is None:
		d={}
	return help(a,d,len(a))

def help(a,d,n):
	if n==0 or n==-1:
		return (0,[])
	else:
		if n in d:
			return d[n]
		temp20,temp21=help(a,d,n-1)
		temp10,temp11=help(a,d,n-2)
		if a[n-1]>=0:
			temp11.append(a[n-1])
			d[n]=(temp10+a[n-1],temp11) if temp10+a[n-1]>=temp20 else (temp20,temp21)
		else:
			d[n]=(temp10,temp11) if temp10>=temp20 else (temp20,temp21)
	return d[n]

#max_wis2: O(n)
def max_wis2(a,d={}):
	d[0]=(0,[])
	if len(a)>0:
		d[1]=(a[0],[a[0]]) if a[0]>=0 else (0,[])
	for i in xrange(2,len(a)+1):
		if a[i-1]>=0:
			temp=d[i-2][1]
			temp.append(a[i-1])
			d[i]=(d[i-2][0]+a[i-1],temp) if d[i-2][0]+a[i-1]>=d[i-1][0] else d[i-1]
		else:
			d[i]=d[i-2] if d[i-2][0]>=d[i-1][0] else d[i-1]
	return d[len(a)]

if __name__=="__main__":
	print max_wis([7,8,5])
	print max_wis([-1,8,10])
	print max_wis([])

	print max_wis2([7,8,5])
	print max_wis2([-1,8,10])
	print max_wis2([])

	max_wis(xrange(10))
	max_wis(xrange(11))
#running time for max_wis
	start=time.time()
	max_wis(xrange(1000,0,-2))
	end=time.time()
	print end-start
#running time for max_wis2
	start=time.time()
	max_wis2(xrange(1000,0,-2))
	end=time.time()
	print end-start

	flag=True
	for i in xrange(500):
		if max_wis2(xrange(i))!=max_wis(xrange(i)):
			print i,"false"
			flag=False
	print flag

	i=10000
	while i<100000000:
		max_wis2(xrange(i))
		end=time.time()
		print i,end-start
		i*=10
		
	print max_wis([0,1,0])
	print max_wis([0,-1,0])
	print max_wis([-1,0,1])
	print max_wis([-1,0,0])