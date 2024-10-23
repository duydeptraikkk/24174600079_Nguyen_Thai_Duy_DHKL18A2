import math

# Nhập giá trị x
x = float(input("Nhập giá trị x: "))

# Kiểm tra điều kiện x
if x <= 0:
    print("Giá trị x phải lớn hơn 0.")
elif x == 1:
    print("Giá trị x = 1 làm cho log cơ số x không hợp lệ.")
else:
    # Tính log cơ số 4 của x và log cơ số x của 2
    log4_x = math.log(x) / math.log(4)
    logx_2 = math.log(2) / math.log(x)

    # Tính f(x)
    f_x = log4_x + logx_2

    # Làm tròn kết quả đến 2 chữ số thập phân
    f_x = round(f_x, 2)

    # In kết quả
    print(f"Giá trị của f(x) là: {f_x}")
