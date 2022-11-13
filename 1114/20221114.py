
def check_pow(input_num):

    if input_num == 1 :
        return True
    elif input_num % 2 !=0:
        return False
    return check_pow(input_num//2)

print(check_pow(int(input())))