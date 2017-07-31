import sys
from collections import *
import collections

a=[3,5,7]
trigrams={}
pentagrams={}
heptagrams={}
for k in a :
	
	d=sys.argv[1:][0]+str(k)
	for line in open(d):
		line = line.rstrip()
		tokens=line.split("\t")
		if k==3:
			trigrams[tokens[1]]=int(tokens[0])
		if k==5:
			pentagrams[tokens[1]]=int(tokens[0])
		if k==7:
			heptagrams[tokens[1]]=int(tokens[0])		

output_file=open(sys.argv[1:][1]+"_3_res","w")
for line in open("trigrams"):
	line=line.rstrip()
	if line in trigrams:
		output_file.write(str(trigrams[line])+"\t\t"+line+"\n")
	else:
		output_file.write("0\t\t"+line+"\n")
output_file.close()

output_file=open(sys.argv[1:][1]+"_5_res","w")
for line in open("pentagrams"):
	line=line.rstrip()
	if line in pentagrams:
		output_file.write(str(pentagrams[line])+"\t\t"+line+"\n")
	else:
		output_file.write("0\t\t"+line+"\n")
output_file.close()

output_file=open(sys.argv[1:][1]+"_7_res","w")
for line in open("heptagrams"):
	line=line.rstrip()
	if line in heptagrams:
		output_file.write(str(heptagrams[line])+"\t\t"+line+"\n")
	else:
		output_file.write("0\t\t"+line+"\n")
output_file.close()			
