#Example
from Lib import *

if __name__ == '__main__' :
    sorted_array = [1, 2, 2, 2, 3, 4, 5, 6] #=> The array has been sorted
    result = linear_search(sorted_array, 6)
    if result != -1:
        print(f"value 2 in index : {result}")
    else:
        print("no value")        

#result : value 2 in index : 1.