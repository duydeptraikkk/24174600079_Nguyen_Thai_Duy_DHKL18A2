# Nhập chuỗi ký tự
input_string = input("Nhập vào chuỗi ký tự: ")
# Kiểm tra số âm
if input_string.startswith("-") and input_string[1:].isdigit():
    print(f"'{input_string}' là số âm.")
else:
    print(f"'{input_string}' không phải là số âm.")
