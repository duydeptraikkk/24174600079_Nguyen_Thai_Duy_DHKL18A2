# Nhập chuỗi ký tự
input_string = input("Nhập vào chuỗi ký tự: ")
input_string = input_string.strip()
result_string = " ".join(input_string.split())
# In chuỗi sau khi loại bỏ khoảng trắng thừa
print("Chuỗi sau khi loại bỏ khoảng trắng thừa:", result_string)
