#####122801#####

import pickle
import math
def selection_sort(arr,count):
    for current in range(0, count):
        min_idx,min = current,arr[current]
        walker = current+1
        while(walker < len(arr)):
            if arr[walker] < min:
                min_idx,min = walker,arr[walker]
            walker +=1
        arr[current],arr[min_idx] = arr[min_idx],arr[current]
    return arr

with open('input.pkl', 'rb') as inp:
    input = pickle.load(inp)
    print(selection_sort(input, 2))

#####122802#####

import pickle
import math
def insertion_sort(arr, count):
    for index in range(1, count+1):
        current = arr[index]
        walker = index
        while walker > 0 and arr[walker - 1] > current:
            arr[walker], arr[walker - 1] = arr[walker - 1], arr[walker]
            walker = walker - 1
    return arr

with open('input.pkl', 'rb') as inp:
    input = pickle.load(inp)
    print(insertion_sort(input, 2))


#####122803#####

import pickle
import math
def bubble_sort(arr):
    count = 0
    n = len(arr)
    swapped = True
    while (swapped != False):
        swapped = False
        count+=1
        for i in range(0,n-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True
    return count
with open('input.pkl', 'rb') as inp:
    input = pickle.load(inp)
    print(bubble_sort(input))


