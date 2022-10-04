###########100301#############
fp = open('input.txt')
string = fp.read()

longest_list=[]
temp_list = []

for text in string:
    if not text.isalpha():
        if len(temp_list)>=len(longest_list):
            longest_list = temp_list
        temp_list = []
    else:
        temp_list.append(text)
ans = "".join(longest_list)
print(ans)

###########100302#############
string =input().upper()
str_list=[]
str_count_list=[]
for text in string:
    if text.isalpha():
        if text not in str_list:
            str_list.append(text)
            str_count_list.append(1)
        else:
            num=str_list.index(text)
            str_count_list[num]=str_count_list[num]+1
for i in zip(str_list,str_count_list):
    print(i[0],i[1])
###########100302_<sol2>#######################
txt = input()
txt_upper = txt.upper()

count = {}
for i in txt_upper:
  if i.isalpha():
    if not i in count:
      count[i]=1
    else:
      count[i]=count[i]+1

for k, v in count.items():
    print(str(k), int(v))
