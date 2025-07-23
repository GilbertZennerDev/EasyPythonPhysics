def checkFunctionTab(line):
	original_line = line
	line = line.split('\t')
	#print(line)
	if len(line) != 2:
		line = line[0].split(' ')
		#print(line)
		line = line[0] + '\t' + line[1] + '\n'
		#print(line)
		return (line)
	else:
		return (original_line)

def check25lines(lines):
	start = -1
	for i, line in enumerate(lines):
		if "{" in line:
			start = i
		if "}" in line and start > -1:
			return ((i - start) <= 25)
			
def checkEmptyLine(lines):
	for line in lines:
		if line == "":
			return (False)
	return (True)

def ournorm(line):
	pass# we need to check void function1()
	