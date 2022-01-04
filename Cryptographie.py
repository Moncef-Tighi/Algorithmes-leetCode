#Create a function that takes an encryption key (a string with an even number of characters) and a message to encrypt. Group the letters of the key by two:

#"gaderypoluki" -> "ga de ry po lu ki"
#Now take the message for encryption. If the message character appears in the key, replace it with an adjacent character
# in the grouped version of the key. If the message character does not appear in the key, leave it as is. 
# If the letter in the key occurs more than once, the first result is used.

def encrypt(key, message):
	x=1
	S=""
	for letter in key:
		S=S+letter
		if x%2==0:
			S=S+" "
		x=x+1

	x=0
	y=0
	result=""
	for letter in message:
		if letter in key and x+1<=len(message):
			y=S.index(letter)
			if S[y]==" ":
				y=y+1
			if (y-1)%3!=2:
				result=result+S[y-1]
			else:
				result=result+S[y+1]
		else:
			result=result+message[x]
		x=x+1
	return result









print(encrypt("ab c","abc ab"))