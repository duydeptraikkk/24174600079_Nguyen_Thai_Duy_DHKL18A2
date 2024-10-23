# Nhập thời gian sử dụng bóng đèn từ bàn phím (giây)
thoi_gian = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))

# Giá trị đã cho
U = 220  # Hiệu điện thế (Volt)
I = 2.7  # Cường độ dòng điện (Ampe)
gia_dien = 7000  # Giá điện (đồng/kWh)

# Kiểm tra điều kiện hợp lệ của thời gian sử dụng
if thoi_gian < 0:
    print("Thời gian sử dụng không hợp lệ. Phải lớn hơn hoặc bằng 0.")
elif thoi_gian == 0:
    print("Thời gian sử dụng là 0, không có điện năng tiêu thụ.")
else:
    # Tính công suất của bóng đèn (W)
    P = U * I  # Công suất P = U * I (Watt)

    # Chuyển đổi thời gian từ giây sang giờ
    thoi_gian_gio = thoi_gian / 3600  # 1 giờ = 3600 giây

    # Tính năng lượng tiêu thụ (kWh)
    nang_luong_tieu_thu = (P * thoi_gian_gio) / 1000  # Đổi từ Wh sang kWh

    # Tính tiền điện phải trả
    tien_dien = nang_luong_tieu_thu * gia_dien

    # Làm tròn tiền điện đến 2 chữ số thập phân
    tien_dien = round(tien_dien, 2)

    # In kết quả
    print(f"Công suất bóng đèn: {P} W")
    print(f"Năng lượng tiêu thụ: {nang_luong_tieu_thu} kWh")
    print(f"Tiền điện phải trả: {tien_dien} đồng")