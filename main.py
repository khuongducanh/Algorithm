a = []
var = input("nhap so phan tu cua List :  ")

def nhap_mang():
   for i in range(0,int(var)):
      i = input("nhap vao vi tri " + str(i) + " : ")
      a.append(i)

def xuat_mang():
   print("List vua nhap la : " + str(a))


def check_nguyen_to(n):
   if (n < 2):
      return False;
   for i in range(2, n):
      if (n % i == 0):
         return False
   return True


def check_chinh_phuong(x):
   if (x < 1):
      return False;
   i = 1
   while (i * i <= x):
      if (i * i == x):
         return True;
      i = i + 1
   return False

def so_nguyen_to():
   sum = 0
   for i in range(0, int(var)):
     if (check_nguyen_to(int(a[i]))):
      print("cac phan tu nguyen to trong List : " + str(a[i]))
      sum = sum + 1
   print("Tong phan tu nguyen to trong List : " + str(sum))


def so_chinh_phuong():
   for j in range(0,int(var)):
      if(check_chinh_phuong(int(a[j]))):
         print("cac phan tu chinh phuong tronh List : " + str(a[j]))



 

if __name__ == "__main__":
    nhap_mang()
    xuat_mang()
    so_nguyen_to()
    so_chinh_phuong()
