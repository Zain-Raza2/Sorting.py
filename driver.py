# Imports for everything else
import random

# Imports for Algorithms
import Algorithms.SelectionSort
import Algorithms.BubbleSort
import Algorithms.InsertionSort

# Put your algorithms here
AlgorithmsList = [
    Algorithms.SelectionSort.Sort,
    Algorithms.BubbleSort.Sort,
    Algorithms.InsertionSort.Sort
]

def GenRandomList(min, max):
    RandomList = []

    for i in range(min, max):
        RandomInt = random.randint(1,30)
        RandomList.append(RandomInt)
    return RandomList

def TestAlgorithms(Algorithm):
    TestCases = [1, 2, 10]
    
    print("")
    print("Testing for:", Algorithm.__name__)
    for case in TestCases:
        RandomList = GenRandomList(0, case)
        Algorithm(RandomList)
        print(case, RandomList)
        if (isSortedAscending(RandomList)):
            print("[SUCCESS]")
        else:
            print("[FAILED]")
    print("")
        
def isSortedAscending(list):
    n = len(list)
    if (n == 1):
        return True
    
    for i in range(n-1):
        if (list[i] > list[i+1]):
            return False
    return True
        
[TestAlgorithms(Algorithm) for Algorithm in AlgorithmsList]