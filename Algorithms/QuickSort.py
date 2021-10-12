import Utility

def Sort(list):
    quickSort(0, len(list) - 1, list)

def quickSort(start, end, list):
    if (start < end):
        
        p = partition(start, end, list)
        quickSort(start, p - 1, list)
        quickSort(p, + 1, end, list)

def partition(start, end, list):
    
    n = len(list)
    pivotIndex = start
    pivot = list[pivotIndex]

    while start < end:

        while start < n and list[start] <= pivot:
            start += 1

        while list[end] > pivot:
            end -= 1

        if (start < end):
            Utility.Swap.Swap(list, list[start], list[end])

    Utility.Swap(list, list[end], list[pivotIndex])

    return end
