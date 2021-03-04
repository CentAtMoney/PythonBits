#!/usr/bin/python3


arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10, 12]

def median(arr1, arr2, index=(len(smaller) / 2)):

    smaller, larger = arr1, arr2 if len(arr1) <= len(arr2) else arr2, arr1

    mid = index
    #I fucked up an didn't use smaller and larger but the args 
    #this problem doesn't bring joy
    arr1_left = arr1[:mid]
    arr1_right = arr1[mid:]

    total_len = len(arr1) + len(arr2)

    want = ((total_len + 1) / 2 ) - len(arr1_left)
    
    arr2_left = arr2[:want]
    arr2_right = arr2[want:]

    arr1_left_big = arr1_left[len(arr1_left - 1)]
    arr1_right_small = arr1_right[0]
    arr2_left_big = arr2_left[len(arr2_left - 1)]
    arr2_right_small = arr2_right[0]
    avg = lambda x,y : (x + y) / 2
    if (arr1_left_big <= arr2_right_small) and (arr1_right_small >= arr2_left_big): 
        if total_len % 2 == 0:
            return avg(max([arr1_right_small, arr2_right_small]), min([arr1_left_big, arr2_left_big]))
        else:
            return max([arr1_left_big, arr2_left_big])
    elif arr1_left_big > arr2_right_small:
        #call median
        median(arr1, arr2, index=(index

