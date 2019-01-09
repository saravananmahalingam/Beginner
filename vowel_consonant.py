a=input()
l=['a','e','i','o','u','A','E','I','O','U']
if a.isalpha():
	if a in l:
		print('Vowel')
	else:
		print('Consonant')
else:
	print('invalid')
