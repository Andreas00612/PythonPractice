########<sol1>############
def check_pow(input_num):

    if input_num == 1 :
        return True
    elif input_num % 2 !=0:
        return False
    return check_pow(input_num//2)

print(check_pow(int(input())))


########<sol2>############

def power2(a):
    if a==1:
        return True
    else:
        if a % 2 !=0:
            return False
        else:
            b=a/2 
        return power2(b)
  
print(power2(int(input())))
