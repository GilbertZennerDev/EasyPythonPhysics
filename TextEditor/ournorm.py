def checkFunctionTab(line):
	if "(" not in line or ';' in line:
		return (line + '\n')
	original_line = line
	line = line.split()
	print(line)
	if line[1] and '(' in line[1]:
		print("one")
		line = line[0] + '\t' + line[1]
		return (line + '\n')
	#line = line.split('\t')
	#if ' ' in line:#len(line) != 2:
#		line = line[0].split(' ')
#		line = line[0] + '\t' + line[1]#
#		return (line + '\n')
	else:
		return (original_line  + '\n')

def checkTabIdent(line):
	if ';' not in line:
		return (line + '\n')
	line = '\t' + line.strip()
	return (line + '\n')

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
	