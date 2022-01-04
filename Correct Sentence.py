#Start each sentence with an uppercase alphabet.
#For every uppercase letter (other than the first alphabet), you have to place a fullstop(.) followed by an empty space.
#There must be only one space between the words and sentences.
#Sentence must end with a full stop(.)
#Two continuous spaces are not allowed.

def correct_sentences(s):
	answer=""
	B=s.split()
	B[len(B)-1]=B[len(B)-1]+"."
	for letter in B:
		if letter[0].isupper()==True:
			B[B.index(letter)]=". "+ B[B.index(letter)]

	B[0]=B[0].capitalize()
	for letter in B:
		answer=answer + letter+ " "
	answer=answer.replace(" . ", ". ")
	answer=answer[:-1]
	return answer

A = "  his english is not good Help him     Thank you"
C =correct_sentences(A)
print(C)