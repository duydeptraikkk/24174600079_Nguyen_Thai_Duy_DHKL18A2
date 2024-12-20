# Nhập chuỗi ký tự
input_string = input("Nhập vào chuỗi ký tự: ")
# Khởi tạo bộ đếm
count_upper = 0
count_lower = 0
for char in input_string:
    if char.isupper():  
        count_upper += 1
    elif char.islower():  
        count_lower += 1

# In kết quả
print("Số chữ cái viết hoa:", count_upper)
print("Số chữ cái viết thường:", count_lower)
