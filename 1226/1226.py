#####122601#####
import math
import pickle
def DFS(graph):
    stack = ['A']
    ans = ['A']
    while len(stack) > 0:
        neighbor = stack.pop()
        if neighbor not in ans:
            ans.append(neighbor)
        for neighbor in graph[neighbor]:
            stack.append(neighbor)
    print(ans)

with open('input.pkl', 'rb') as inp:
    graph = pickle.load(inp)
    DFS(graph)
    
    
#####122602#####
import math
import pickle
def LongestDistance(graph):
    queue = ['A']
    count = -1
    while queue:
        next_queue = []
        for s in queue:
            for neighbor in graph[s]:
                next_queue.append(neighbor)
        queue = next_queue
        count+=1
    print(count)

with open('input.pkl', 'rb') as inp:
    graph = pickle.load(inp)
    LongestDistance(graph)