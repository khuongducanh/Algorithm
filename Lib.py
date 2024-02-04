#step 1 : add to folder main
#step 2 : import Lib
#step 3 : use


#return 1 : this is Prime 
#return 0 : not Prime 
def Check_Prime(n):
   if (n < 2):
      return False;
   for i in range(2, n):
      if (n % i == 0):
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




