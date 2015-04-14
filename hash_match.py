# To use the program, specify file1 and file2 name as the arguments
#########################################################
#							#
#							#
#	Usage: python hash_match.py file1 file2		#
#							#
#							#
######################################################


import hashlib
import sys

try:
	a = str(sys.argv[1])
	b = str(sys.argv[2])
	c = hashlib.sha512(open(a).read()).hexdigest()
	d = hashlib.sha512(open(b).read()).hexdigest()

	if c==d:
		print '*' * 60 + '\n'
		print '            Hash Matched! Files are Same\n'
		print '*' *60
	else:
		print '*' * 60 + '\n'	
		print "Hash does not Match\n"
		print '*' * 60 + '\n'
	
except:
	print 'Please specify arguments correctly'
	print " "
	print "Usage: python hash_match.py file1 file2"
	print " "


