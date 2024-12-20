# Nhập chuỗi ký tự
input_string = input("Nhập chuỗi ký tự: ")
input_string = input_string.strip()
words = input_string.split()
word_count = len(words)
# In kết quả
print("Số các từ trong chuỗi là:", word_count)
