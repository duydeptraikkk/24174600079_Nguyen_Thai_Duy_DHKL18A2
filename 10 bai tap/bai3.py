# Nhập họ tên
full_name = input("Nhập vào họ tên đầy đủ: ")
# Loại bỏ khoảng trắng thừa
full_name = full_name.strip()
name_parts = full_name.split()
# Lấy họ là từ đầu tiên
ho = name_parts[0]
# Lấy tên là từ cuối cùng
ten = name_parts[-1]
# In kết quả
print("Họ:", ho)
print("Tên:", ten)
