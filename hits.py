print "testing again"
try:
	infile = open("/mnt/castor/seas_home/j/jtrovato/html/cgi-bin/count.txt", "r")
except Exception:
	print "Can't Find the File!"
else:
	print "in the file"
	print infile.readline()

print "testing!"
