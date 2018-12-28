#! /usr/bin/python3
from sys import maxint

#test = [1, 2, 3, -2, 5]
#test = [2, -5, 6, 7, 6 -9]
def not_kadanes(arr):
    largest = -maxint - 1
    largestNow = 0

    for index, ele in enumerate(arr):
        if index < len(arr) - 1 and abs(ele - arr[index + 1]):
            largestNow += ele
            if largestNow > largest:
                largest = largestNow
    return largest 

def kadanes_c(arr):
    maxNum = -maxint - 1
    maxEnd = 0

    for index, ele in enumerate(arr):
        maxEnd += ele
        if (maxNum < maxEnd):
            maxNum = maxEnd 
        if (maxEnd < 0):
            maxEnd = 0
    return maxNum

def kadanes_c1(arr, size):
    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + arr[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

def kadanes_c2(arr, size):
    curMax = arr[0]
    globalMax = arr[0]

    for index, ele in enumerate(arr):
        curMax = max(ele, ele + curMax)
        globalMax = max(curMax, globalMax)

    return globalMax

test = [1, 1, 2, 3, -2, 5]
test2 = [-1, -2, -3, -4]
test3 = [-1, 1, 2, 3, -5, 2]

print('Answer:', not_kadanes(test))
print('Answer:', not_kadanes(test2))
print('Answer:', not_kadanes(test3))
#print('Answer:', kadanes_c2(test, 5))
#print('Answer:', kadanes_c2(test2, 4))
#kadanes(test)
#kadanes(test2)
