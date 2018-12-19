#!/usr/bin/python3

# is `H` == `h`?
# do numbers count?
# special characters?
# check for inputs?
# O(n)
def isUnique(string):
    cache = {}
    for letter in string:
        if letter not in cache:
            cache[letter] = 1
        else:
            return False
    return True

# capitilization
# whitespace
# check for inputs
# O(n) || O(1)
def checkPermutation(s1, s2):
    cache = {}

    if len(s1) != len(s2):
        return False

    for letter in s1:
        if letter not in cache:
            cache[letter] = 1
    for letter in s2:
        if letter not in cache:
            return False
        if letter in cache:
            cache[letter] += 1
    return True

def URLify(string):
    newArr = []

    if len(string) < 1:
        return False

    for letter in string:
        if letter is ' ':
            letter = '%20'
        newArr.append(letter)
    
    return ''.join(newArr)


test    = 'Hello'
test1   = 'Hi'
test2   = 'elolH'
test3   = 'Hi There Sir'
test4   = 'Hey    there'

print(isUnique(test))
print(isUnique(test1))
print(checkPermutation(test, test1))
print(checkPermutation(test, test2))
print(URLify(test3))
print(URLify(test4))
