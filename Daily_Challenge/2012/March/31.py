def stoogesort(array):
    """Perform the stooge sort algorithm on a list of numbers."""
    if array[0] > array[-1]:
        array[0], array[-1] = array[-1], array[0]
    if len(array) >= 3:
        t = len(array) // 3
        # stoogesort initial 2/3rds
        array = stoogesort(array[:(t*2)]) + array[(t*2):]
        # stoogesort final 2/3rds
        array = array[:t] + stoogesort(array[t:])
        # re-stoogesort initial 2/3rds
        array = stoogesort(array[:(t*2)]) + array[(t*2):]
    return array

def bogosort(array):
    """Instead of having bogosort call itself, and hitting the recursion ceiling of python, have this call it."""
    from random import shuffle
    while in_order(array) == False:
        shuffle(array)
    return array

def in_order(array):
    """Check to see if an array is in order from smallest to largest."""
    return all(array[x] < array[x+1] for x in range(len(array) - 1))


if __name__ == "__main__":
    array = [1,3,6,7,2,34,2]
    print("Array is : " + str(array))
    stooge = stoogesort(array)
    print("Stoogesorted array is: " + str(stooge))
    bogo = bogosort(array)
    print("Bogosorted array is " + str(bogo))
