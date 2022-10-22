########101001<SOL1>###############

s = input()
num = [f'{i}' for i in range(0, 10)]
s = sum([int(y) for y in str(sum([int(x) for x in s if x in num]))])
while s >10:
    s = str(s)
    s = sum([int(y) for y in str(sum([int(x) for x in s if x in num]))])
print(s)
#############101001<sol2>###########

input = input()
sum=int(input[0])
for i in range(1,len(input)):
    sum +=int(input[i])
    if sum>10:
        sum = sum%10+1
print(sum)

###########101002###########

num_list = input()
num_list = num_list.split(',')
ans_list = []
for i in num_list:
    i =int(i)
    if not i in ans_list:
        ans_list.append(i)
print(ans_list)

#########101003##########

num_list = input()
num_list = num_list.split(',')
ans_list = []
for i in num_list:
    ans_list.append(len(i))
print(ans_list)

##########101004<sol1>###########
input_list = input().split()
cal_list = []
for i in input_list:
    if i == '+':
        first = cal_list.pop()
        secoond = cal_list.pop()
        cal_list.append(first+secoond)
    elif i =='-':
        first = cal_list.pop()
        secoond = cal_list.pop()
        cal_list.append(secoond-first)
    elif i == '*':
        first = cal_list.pop()
        secoond = cal_list.pop()
        cal_list.append(first*secoond)
    elif i == '/':
        first = cal_list.pop()
        secoond = cal_list.pop()
        cal_list.append(secoond / first)
    else:
        cal_list.append(int(i))
print(cal_list[0])

##########101004<sol2>###########
op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y}

input_list = input().split()
cal_list = []
for i in input_list:
    if i in op:
        first = cal_list.pop()
        second = cal_list.pop()
        cal_list.append(op[i](second,first))
    else:
        cal_list.append(int(i))
print(cal_list[0])
