#!/usr/bin/python

import random
import math


def merge(arr1, arr2):
    """Merge two sorted arrays."""
        
    arr = []

    # indicies for arr1 and arr2
    i, j = 0, 0
    
    # compare elements in arrays
    # append smaller value to arr
    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1

        else:
            arr.append(arr2[j])
            j += 1
    
    # add what is left of arr1
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    # add what is left of arr2
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1

    return arr

def is_sorted(arr):
    
    # arrays of length one are sorted
    if len(arr) <= 1:
        return True
    
    # simple check
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return True

    # can we add more?

    return False

def merge_sort(arr):
    
    mid = math.ceil(len(arr) / 2)
    
    if is_sorted(arr):
        return arr
    
    # break left side in half
    l = merge_sort(arr[:mid])
    # break right side in half
    r = merge_sort(arr[mid:])
    # merge sides
    merged = merge(l, r)
    
    return merged

    # since length 1 arrays are sorted
    # and we have a means to combine sorted arrays
    # we ask ourselves are these 2 arrays sorted? 
    # if no we ask arrays within the unsorted arrays the same question
    # we are garunteed to eventually get an answer since length 1 arrays are sorted
    # Once we get a yes to our question we merge them
    # this cascades back up as we work with every element
    # in our original unsorted array since we get the arrays we ask our question
    # to from the left and right halves of it!
    



