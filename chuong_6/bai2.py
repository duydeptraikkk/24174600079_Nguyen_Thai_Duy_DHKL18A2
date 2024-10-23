import math

# Nhập giá trị x
x = float(input("Nhập giá trị x: "))

# Tính giá trị của biểu thức f(x)
tu_so = -x + math.sqrt(x**2 + 4)
mau_so = (x**4 + 1)**(1/7)

# Kiểm tra xem mẫu số có bằng 0 hay không
if mau_so == 0:
    print("Mẫu số không thể bằng 0.")
else:
    f_x = tu_so / mau_so  # Tính giá trị của f(x)

    # Làm tròn kết quả đến 2 chữ số thập phân
    f_x = round(f_x, 2)

    # In kết quả
    print(f"Giá trị của f(x) là: {f_x}")
