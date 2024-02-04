import math

def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False
    # check so nguyen to khi n >= 2
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

if __name__ == "__main__":
    listPrimeNumber = []
    print("Cac so nguyen to nho hon 100 la:")
    for i in range(0, 100):
        if (isPrimeNumber(i)):
            print(i)
