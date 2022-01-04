#Your computer might have been infected by a virus! Create a function that finds the viruses in files and removes them from your computer.

#Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.
#Return "PC Files: Empty" if there are no files left on the computer.

def remove_virus(files):
	B=files.split()
	files=""
	for letter in B:
		if (letter.find("virus")!= -1) or (letter.find("malware")!= -1):
			if (letter.find("antivirus.exe")!=-1) or (letter.find("notvirus.exe")!=-1) :
				files=files+" " +letter				
		else:
			files=files+" " +letter
	if files[len(files)-1]==",":
		files=files[:-1]
	files=files[1:]
	if len(files)==9:
		return "PC Files: Empty"
	return files

A =("PC Files: virus.exe, bestmalware.exe, memzvirus.exe")
B= remove_virus(A)
print(B)