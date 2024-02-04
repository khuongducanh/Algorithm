import random

chuoi = input("nhap chuoi : ")
danh_sach_phan_tu = list(chuoi)
random.shuffle(danh_sach_phan_tu)
chuoi_ngau_nhien = ''.join(danh_sach_phan_tu)
print("Chuỗi gốc:", chuoi)
print("Chuỗi sau khi được ngẫu nhiên hoán đổi:", chuoi_ngau_nhien)
