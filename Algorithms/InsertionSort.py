def Sort(list):
    n = len(list)
    for i in range(1, n):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key