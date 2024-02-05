#step 1 : add to folder main
#step 2 : import Lib
#step 3 : use
#warning : this is Library , No run code

#Library
import random 
import bisect
#

#Algorithm basic
#
#return 1 : this is Prime 
#return 0 : not Prime 
#x : number
def Check_Prime(x):
   if (x < 2):
      return False;
   for i in range(2, x):
      if (x % i == 0):
         return False
   return True


#return 1 : this is SquareNumber
#return 0 : not SquareNumber
#x : number
def Check_SquareNumber(x):
   if (x < 1):
      return False;
   i = 1
   while (i * i <= x):
      if (i * i == x):
         return True;
      i = i + 1
   return False


#return 1 : this is even number
#return -1 : this is odd number
#x : number
def Check_even_odd(x):
    if x % 2 == 0:
        return 1
    else:
        return -1 


#return 1 random string of characters
#x : string
def sort_and_random(x):
    char = list(x)
    random.shuffle(char)
    return ''.join(char)

###


#Algorithm with String
#KMP (Knuth-Morris-Pratt): search string
def Create_Table_lps(x):
    m = len(x)
    lps = [0] * m
    i, j = 1, 0

    while i < m:
        if x[i] == x[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

#return : index or string
#x : string main
#y : string to find
def Search_kmp(x, y):
    n, m = len(x), len(y)
    lps = Create_Table_lps(y)
    i, j = 0, 0

    while i < n:
        if y[j] == x[i]:
            i += 1
            j += 1

            if j == m:
                return i - j
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1



#Rabin-Karp : search string
def hash_func(s):
    return sum(ord(c) for c in s)

#return : index or string
#x : string main
#y : string to find
def Rabin_karp(x, y):
    n, m = len(x), len(y)

    y_hash = hash_func(y)
    x_hash = hash_func(x[:m])

    for i in range(n - m + 1):
        if x_hash == y_hash and x[i:i+m] == y:
            return i

        if i < n - m:
            x_hash = hash_func(x[i+1:i+m+1])
##


#Algorithm Sort
#
#Quick sort : sort array
#return : The array has been sorted 
def Quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return Quick_sort(left) + middle + Quick_sort(right)



#Merge sort : sort array
#return : The array has been sorted 
def Merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = Merge_sort(left_half)
    right_half = Merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # So sánh từng phần tử và trộn
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



#Linear sort : sort array
#return : The array has been sorted 
def Linear_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)
    for value in arr:
        count[value] += 1

    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])

    return result
##


#Algorithm Search
#
#Binary search 
#return index of value 
#return -1 : no value
#arr : array[]
#x   : value search
#Note: array must be sorted
def binary_search(arr, x):
    index = bisect.bisect_left(arr, x)
    if index != len(arr) and arr[index] == x:
        return index
    else:
        return -1
#example
#sorted_array = [1, 2, 2, 2, 3, 4, 5, 6] #=> The array has been sorted
#result = binary_search(sorted_array, 2)
#if result != -1:
#    print(f"value 2 in index : {result}.")
#else:
#    print("no value")        
#result : value 2 in index 1


#Linear search : 
#return index of value 
#return -1 : no value
#arr : array[]
#x   : value search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  
    return -1 