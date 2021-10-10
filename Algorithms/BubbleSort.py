import Utility.Swap

def Sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if (list[j] > list[j+1]):
                Utility.Swap.Swap(list, j, j+1)