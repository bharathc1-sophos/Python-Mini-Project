import sys
import os
a=[3,5,7]
trigrams={}
pentagrams={}
heptagrams={}
for i in a:
	d=sys.argv[1:][0]+str(i)
	for f in os.listdir(d):
		if i==3:
			for line in open(d+"/"+f):
				line = line.rstrip()
				#trigram=line.split("\n")
				trigrams[line]=1
		if i==5:
			for line in open(d+"/"+f):
				line = line.rstrip()
				#pentgram=line.split("\n")
				pentagrams[line]=1			
		if i==7:
			for line in open(d+"/"+f):
				line = line.rstrip()
				#heptagram=line.split("\n")
				heptagrams[line]=1
				
output_file=open("trigrams",'w')
for trigram in trigrams:
	output_file.write(trigram+"\n")
output_file.close()
output_file=open("pentagrams",'w')
for pentagram in pentagrams:
	output_file.write(pentagram+"\n")
output_file.close()
output_file=open("heptagrams",'w')
for heptagram in heptagrams:
	output_file.write(heptagram+"\n")
output_file.close()	
