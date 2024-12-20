# Nhập chuỗi ký tự
input_string = input("Nhập vào chuỗi ký tự: ")
# Kiểm tra số thập phân
try:
    float(input_string)
    print(f"'{input_string}' là số thập phân.")
except ValueError:
    print(f"'{input_string}' không phải là số thập phân.")
