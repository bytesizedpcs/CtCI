#! /usr/bin/python3

def kadanes(arr):
    longest = 0
    prevIndex = 0
    largest = 0
    prevEle = 0

    for index, ele in enumerate(arr):
        if index == 0:
            prevEle = ele
        if abs(ele - prevEle) <= 1 and index - prevIndex <= 1:
            prevEle += ele
            if prevEle > largest:
                largest = prevEle

    return largest

test = [1, 2, 3, -2, 5]
test2 = [-1, -2, -3, -4]

print('Answer:', kadanes(test))
print('Answer:', kadanes(test2))
#kadanes(test)
#kadanes(test2)
