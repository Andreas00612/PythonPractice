######<sol1>########
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



######<sol2>########
s = input().split()
first_list = ['(','{','[']
second_list = [')','}',']']


def isValid(s):
    stack = []
    for i in s:
        if i in first_list:
            stack.append(i)
        else:
            if i in second_list:
                if len(stack)==0:
                    return False
                else:
                    op = stack.pop()
                    index_1 = first_list.index(op)
                    index_2 = second_list.index(i)
                    if index_1 != index_2:
                        return False
    if len(stack)==0:
        return True
    else:
        return False
print(isValid(s))
