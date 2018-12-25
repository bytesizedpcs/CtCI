#!/usr/bin/python3

def oneEditAway(s1, s2):
    if len(s1) == len(s2):
        return oneEditReplace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return oneEditInsert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return oneEditInsert(s1, s2)

    return False

def oneEditReplace(s1, s2):
    foundDifference = False

    for index in range(len(s1)):
        if s1[index] != s2[index]:
            if foundDifference:
                return False
            foundDifference = True

    return True

def oneEditInsert(s1, s2):
    index1 = 0
    index2 = 0

    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    
    return True

def oneEditAwayUp(s1, s2):
    if abs(len(s1) - len(s2) > 1):
        return False

    s1 = s1 if len(s1) < len(s2) else s2
    s2 = s2 if len(s1) < len(s2) else s1

    index1 = 0
    index2 = 0
    foundDifference = False

    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if foundDifference: return False
            foundDifference = True

def longestSubsequence(s1, s2):
    cache1 = {}
    cache2 = {}
    count = 0
    longest = ''

    if s1 == s2:
        return s1
    if len(s1) < 1 and len(s2) < 1:
        return False

    for index, letter in enumerate(s1):
        if letter not in cache1:
            cache1[letter] = [index]
        if letter in cache1 and index not in cache1[letter]:
            cache1[letter].append(index)

    for index, letter in enumerate(s2):
        if letter not in cache2:
            cache2[letter] = [index]
        if letter in cache2 and index not in cache2[letter]:
            cache2[letter].append(index)

    for index, letter in enumerate(s1):
        return
        
    return (cache1, cache2)

def LCS(s1, s2):
    n = len(s1)
    m = len(s2)
    arr = [1, 2, 3, 4]

    L = [[None] * (n+1) for i in xrange(m+1)]    

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]

test0 = 'Hello'
test1 = 'Hell'
test2 = 'Heloo'
test3 = 'Aeloo'
test4 = 'ABAZDC'
test5 = 'BACBAD'

print(LCS(test4, test5))

#print(oneEditAway(test0, test1))
#print(oneEditAway(test0, test2))
#print(oneEditAway(test0, test3))
