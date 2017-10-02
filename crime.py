import fileinput
with open('Crime.txt') as f:
	data = f.readlines()
	for line in data:
		 words = line.split()
	for word in words:
		print(word)
