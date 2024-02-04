from Lib import *

#example : KMP(Knuth-Morris-Pratt)

if __name__ == '__main__' :
    vanban = "Đức Anh đẹp trai nhất thế giới"
    mau = "thế giới"
    temp = Rabin_karp(vanban,mau)
    print("Search in index when use Rabin_karp:" + str(temp))

#result
#Search in index when use Rabin_karp:22   
