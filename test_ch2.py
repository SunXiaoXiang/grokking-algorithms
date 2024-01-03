def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def test_findSmallest():
    arr = [1,3,4,5,6,7,8,9,11,2]
    assert findSmallest(arr) == 0

def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

selectionSort([5,3,6,2,10])
