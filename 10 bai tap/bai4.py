# Nhập chuỗi ký tự
input_string = input("Nhập vào chuỗi ký tự: ")
# Khởi tạo bộ đếm
count_letters = 0
count_digits = 0
count_special = 0
for char in input_string:
    if char.isalpha(): 
        count_letters += 1
    elif char.isdigit(): 
        count_digits += 1
    else:  
        count_special += 1

# In kết quả
print("Số ký tự là chữ:", count_letters)
print("Số ký tự là số:", count_digits)
print("Số ký tự là ký tự đặc biệt:", count_special)
