def is_palindrome(string):
    # Chuyển đổi chuỗi thành chữ thường và loại bỏ khoảng trắng
    string = string.lower().replace(" ", "")

    # So sánh chuỗi với phiên bản đảo ngược của nó
    if string == string[::-1]:
        return True
    else:
        return False

# Ví dụ sử dụng
string = "Nhiệm vụ của chúng tôi là thiết kế một thuật toán cho dù có hay không! Mục đích là để đạt được thời gian chạy tuyến tính."
if is_palindrome(string):
    print("Chuỗi là palindrome!")
else:
    print("Chuỗi không phải là palindrome!")