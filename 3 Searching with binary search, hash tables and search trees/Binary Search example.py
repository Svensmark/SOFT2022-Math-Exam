import math

def binarySearch(array, target):
    #If there isn't a length on the array, return -1
    if not len(array):
        return -1

    #Define the most left and right indexes
    left = 0
    right = len(array)

    #As long as there is 2 or more elements in the given array.
    while (left + 1 < right):
        #Calculate the mid, use math ceilin incase of uneven numbers
        mid = math.ceil((right + left) // 2)

        #If we found the target on mid, return index of target
        if array[mid] == target:
            return mid
        #If the mid is lower than target, left = mid
        elif array[mid] < target: 
            left = mid 
        #Otherwise right = mid
        else:
            right = mid

    #Checking if final element is target, if it is return index
    if array[left] == target:
        return left 

    #If it isn't, the target isn't in the array, and return -1.
    return -1


def main():
    array = [1,4,5,7,9,12,15,18,19,22,23,25,29,30,33,35,40,41,50]
    print(f'Index of 1: {binarySearch(array, 1)}')
    print(f'Index of 9: {binarySearch(array, 9)}')
    print(f'Index of 22: {binarySearch(array, 22)}')
    print(f'Index of 30: {binarySearch(array, 30)}')
    print(f'Index of 50: {binarySearch(array, 50)}')

    array = []
    print(f'Index of 100: {binarySearch(array, 100)}')

    array = [1]
    print(f'Index of 1: {binarySearch(array, 50)}')

    array = [8, 9]
    print(f'Index of 1: {binarySearch(array, 8)}')

main()