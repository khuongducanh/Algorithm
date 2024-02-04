#step 1 : add to folder main
#step 2 : import Lib
#step 3 : use
#warning : this is Library , No run code

#Library
import random 
print("Warning : this is Library , No run code ")



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
