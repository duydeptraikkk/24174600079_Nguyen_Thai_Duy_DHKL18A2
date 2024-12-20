def decimal_to_binary(n):
    if n < 0:
        return "Không thể chuyển đổi số âm."
    return bin(n).replace("0b", "")  # Chuyển đổi và loại bỏ "0b" ở đầu

def binary_to_decimal(b):
    try:
        return int(b, 2)  # Chuyển đổi từ nhị phân sang thập phân
    except ValueError:
        return "Đầu vào không phải là số nhị phân hợp lệ."

# Chọn chế độ chuyển đổi
print("Chọn chế độ chuyển đổi:")
print("1. Chuyển đổi từ cơ số 10 sang cơ số 2")
print("2. Chuyển đổi từ cơ số 2 sang cơ số 10")

choice = input("Nhập lựa chọn (1 hoặc 2): ")

if choice == '1':
    number = int(input("Nhập số cơ số 10: "))
    binary = decimal_to_binary(number)
    print(f"Số {number} trong hệ cơ số 2 là: {binary}")
elif choice == '2':
    binary_number = input("Nhập số nhị phân: ")
    decimal = binary_to_decimal(binary_number)
    print(f"Số nhị phân {binary_number} trong hệ cơ số 10 là: {decimal}")
else:
    print("Lựa chọn không hợp lệ!")
