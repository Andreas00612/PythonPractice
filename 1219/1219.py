####121901####
import heapq
import pickle
import math
def heapsort(lis):
    ans = []
    heapq.heapify(lis)
    while len(lis)>0:
        ans.append(heapq.heappop(lis))
    return ans


with open('input.pkl', 'rb') as inp:
    hlist = pickle.load(inp)
    print(heapsort(hlist))
    
    
####121902####
import pickle
import math
def del_Vertex(data,index):
  for i in range(len(data)):
    del data[i][index]
  del data[index]
  return data
def count_edge(data):
  num=0
  for i in data:
      num += sum(i)
  print(num)
with open('input.pkl', 'rb') as inp:
  hlist = pickle.load(inp)
  hlist = del_Vertex(hlist,2)
  count_edge(hlist)
    
    