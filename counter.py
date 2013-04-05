infile = open("/mnt/castor/seas_home/j/jtrovato/html/cgi-bin/count.txt", "r")
hits = infile.readline()
hits_int = int(hits) + 1
hits_str = str(hits_int)
outfile = open("count.txt", "w")
outfile.write(hits_str)
outfile.close()
