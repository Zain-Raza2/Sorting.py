def SelectionSort(list):
    for i in range(len(list)): 
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]: 
                min = j
        list[i], list[min] = list[min], list[i]