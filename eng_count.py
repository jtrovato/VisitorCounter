infile = open("eng_count.txt", "r")
hits = infile.readline()
hits_int = int(hits) + 1
hits_str = str(hits_int)
outfile = open("eng_count.txt", "w")
outfile.write(hits_str)
outfile.close()
print hits_str
#print "old: " + hits + " new: " + hits_str
