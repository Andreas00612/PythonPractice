s = input().split()
def isValid(s):
	d = {'(':')', '{':'}','[':']'}
	stack = []
	for i in s:
		if i in d:
			stack.append(i)
		elif i in d.values() and (len(stack) == 0 or d[stack.pop()] != i):
			return False
	return len(stack) == 0
print(isValid(s))