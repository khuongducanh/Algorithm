def check(x) :
    if(x<0):
        return False
    if(x%2==0):
        return True
    return False        


if __name__ == "__main__":
   for i in range (100):
    if(check(i)==True):
        print(i)
