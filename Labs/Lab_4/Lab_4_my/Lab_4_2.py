import sys

filename = input("Enter the name of a file:")

try:
	fh = open(filename, 'r')
except	IOError:
	print("Cannot open file")
	sys.exit()

dic = {}
for line in fh:
	for c in line:
		if c.isdigit():
			dic[c] = dic.setdefault(c, 0) + 1

ls = []
for key in dic:
	ls.append((key, dic[key]))
ls.sort()
print("Digits:\t", end="")
for a,b in ls:
	print(a, end="  ")
print("\nCount:\t", end="")
for a,b in ls:
	print(b, end="  ")
