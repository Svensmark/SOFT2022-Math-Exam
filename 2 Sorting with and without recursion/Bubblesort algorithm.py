# Python program for implementation of Bubble Sort
import datetime
import random 


def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
 
 
# Driver code to test above
myList = [0]*10000
counter = 0
for i in range(len(myList)):
    myList[i-1] = random.randint(0,10000)


first = datetime.datetime.now()
bubbleSort(myList)
last = datetime.datetime.now()
time = last-first
#print(myList)
print(f"Bubblesorting took: {time.total_seconds()} seconds")