#step 1 : add to folder main
#step 2 : import Lib
#step 3 : use


#return 1 : this is Prime 
#return 0 : not Prime 
def Check_Prime(x):
   if (x < 2):
      return False;
   for i in range(2, x):
      if (x % i == 0):
         return False
   return True


#return 1 : this is SquareNumber
#return 0 : not SquareNumber
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
def Check_even_odd(x):
    if x % 2 == 0:
        return 1
    else:
        return -1 





