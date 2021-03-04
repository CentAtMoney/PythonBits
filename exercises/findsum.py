#!/usr/bin/python3

def bs(goal, arr, sort=False):
   
    if sort:
        arr = sorted(arr)

    if len(arr) == 0:
        return None

    mid = len(arr) // 2
    
    if arr[mid] == goal:
        return goal
    elif arr[mid] > goal:
        return bs(goal, arr[mid::])
    else:
        return bs(goal, arr[0:mid])

def find_pair(goal, arr):

    d = dict()
    for num in arr:

        if goal - num in d.keys():
            return d[goal - num], num
        
        d[num] = num

    return None

print(find_pair(5, [1,3,5,2]))

