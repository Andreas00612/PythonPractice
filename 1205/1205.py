######120501####
import math
def sumOfChild(list_):
    # --- TO DO---#
    height = len(list_)
    tree_level = int(math.log(height, 2))
    a = pow(2, tree_level) - 1
    sum = 0
    level = 2

    while level < tree_level:
        left_node_num = pow(2, level) - 1
        right_node_num = left_node_num + pow(2, level - 1)
        for i in range(left_node_num, right_node_num):
            sum += list_[i]
        level += 1

    ##最後一層
    for i in range(a, height):
        sum += list_[i]
    print(sum)
    # ------------------------------------------------------------#


# loading input file
with open('input.pkl', 'rb') as inp:
    heap = pickle.load(inp)  # a list
    sumOfChild(heap)


###120502####
import math
def heapCheck(Arr):
    if len(Arr) <= 1:
        return True
    heaps = (len(Arr) - 2) // 2 + 1
    for i in range(heaps):
        if Arr[i] > Arr[2 * i + 1]:  ## 確認左節點符合
            return False
        elif (2 * i + 2 != len(Arr) and Arr[i] > Arr[2 * i + 2]): ##確認右節點是某存在 & 確認是否符合
            return False
    return True
    #------------------------------------------------------------#
#loading input file
with open('input.pkl','rb') as inp:
    hlist = pickle.load(inp) # a list
    print(heapCheck(hlist))
