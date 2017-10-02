import string
#asslt=0
import fileinput
with open('Crime.csv') as f:
	data = f.readlines()
	for line in data:
		words = line.split()
		#for word in words:
		#	global asslt
		print(words)
		count=words.count("ASSAULT")
		print(count)
			#xy
			#asslt=0
"""			if word=='ASSAULT':
				asslt += 1 
			elif word=='THEFT FROM VEHICLE':
				theft_vehicle+=1
			elif word=='BREAK AND ENTER':
				breaknenter+=1
			elif word=='ROBBERY':
				robbery+=1
			elif word=='THEFT OF VEHICLE':
				tov+=1
			#print(asslt)
"""
