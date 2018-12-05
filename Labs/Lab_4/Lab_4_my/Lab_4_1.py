import sys

try:
	height = int(input("Enter strictly positive number: "))
except ValueError:
	print("Wrong Input")
	sys.exit()

def char_wrap(num):
	if num > ord('Z'):
		num = ord('A')	
	if num < ord('A'):
		num = ord('Z')		
	return num
		
char_num = ord('A')	
for h in range(1, height+1):
	for i in range(height - h):
		print(" ", end="")
	length = 2 * h - 1
	for l in range(1, length+1):
		print(chr(char_num), end="")
		if l == h:
			char_max = char_wrap(char_num + 1)

		if l < h:
			char_num += 1
			char_num = char_wrap(char_num)
		else:
			char_num -= 1
			char_num = char_wrap(char_num)
	
	for i in range(height - h):
		print(" ", end="")
	print("\n", end="")
	char_num = char_max
	if char_num > ord('Z'):
		char_num = ord('A')		
	
