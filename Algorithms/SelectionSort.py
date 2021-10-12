import Utility

def Sort(list):
    n = len(list)
    for i in range(n): 
        min = i
        for j in range(i+1, n):
            if list[j] < list[min]: 
                min = j
        Utility.Swap(list, i, min)