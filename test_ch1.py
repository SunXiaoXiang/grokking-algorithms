def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low<= high:
        mid = (low + high)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None 

def test_binary_search():
    my_list = [1,3,5,7,9]
    assert binary_search(my_list,3) != None
    assert binary_search(my_list,31) == None
