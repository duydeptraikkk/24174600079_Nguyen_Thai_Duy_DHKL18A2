import math
# nhập bán kính và chiều cao
r = float(input("nhập bán kính r: "))
h = float(input("nhập chiều cao h: "))
# giá trị pi
pi = 3.14
if r <= 0:
    print("bán kính phải lớn hơn 0.")
elif h <= 0:
    print("chiều cao phải lớn hơn 0.")
else:
    # tính diện tích xq
    dien_tich_xung_quanh = 2 * pi * r * h
# tính diện tích tp
dien_tich_toan_phan = 2 * pi * r * (r + h)
# tính thể tích khối trụ
the_tich = pi * r ** 2 * h
# làm tròn kq đến 2 chữ số thập phân
dien_tich_xung_quanh = round(dien_tich_xung_quanh, 2)
dien_tich_toan_phan = round(dien_tich_toan_phan, 2)
the_tich = round(the_tich, 2)
# kết quả
print(f"diện tích xung quanh: {dien_tich_xung_quanh}")
print(f"diện tích toàn phần: {dien_tich_toan_phan}")
print(f"thể tích khối trụ: {the_tich}")