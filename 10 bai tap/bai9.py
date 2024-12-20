    # Nhập chuỗi ký tự nhị phân
binary_string = input("Nhập vào chuỗi ký tự nhị phân: ")
# Kiểm tra và chuyển đổi
if all(char in '01' for char in binary_string):
    decimal_value = int(binary_string, 2)
    print(f"'{binary_string}' là số nhị phân, chuyển sang thập phân: {decimal_value}")
else:
    print(f"'{binary_string}' không phải là số nhị phân.")
