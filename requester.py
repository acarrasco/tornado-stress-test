import sys
import urllib
import time

requests = 0
start = time.time()
while True:
	urllib.urlopen(sys.argv[1]).read()
	requests += 1
	print (time.time()-start)/requests
