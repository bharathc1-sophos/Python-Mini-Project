import sys
from collections import *
import collections

a=[3,5,7]
d=sys.argv[1:][0]
for k in a :
	trigrams={}
	d=sys.argv[1:][0]+str(k)
	for line in open(d):
		line = line.rstrip()
		tokens=line.split("\t")
		trigrams[tokens[1]]=int(tokens[0])
	output_file = open(sys.argv[1:][1]+"_top30"+"_"+str(k),'w')
	l=len(trigrams)
	trigrams=collections.Counter(trigrams).most_common(int(l*0.3))
	for trigram in trigrams:
		#count = trigrams[trigram]
		output_file.write(str(trigram[0])+"\n")
	output_file.close()
