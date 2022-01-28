import os

path = os.path.dirname(__file__)

def isPalindrome(text):
	text = list(text)
	while " " in text:
		text.remove(" ")

	for i in range(len(text)):
		if text[i] != text[len(text)-i-1]:
			return False
	return True

with open(os.path.join(path, "palindrom.txt"), "r") as file:
	palindromes = []
	for row in file:
		if isPalindrome(str(row.strip())):
			palindromes.append(row.strip())

	print(palindromes)

with open(os.path.join(path, "palindrom.txt"), "a") as f:
	for palindrome in palindromes:
		print(palindrome, file=f)
	
