def check_anagram(word1, word2):
    # Chuyển hai từ về chữ thường và loại bỏ khoảng trắng (nếu có)
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    # Kiểm tra xem hai từ có cùng độ dài hay không
    if len(word1) != len(word2):
        return False
    
    # Sắp xếp các ký tự trong hai từ theo thứ tự từ điển
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    
    # So sánh hai từ đã được sắp xếp
    if sorted_word1 == sorted_word2:
        return True
    else:
        return False

# Kiểm tra ví dụ
word1 = "yên bình"
word2 = "bối rối"
if check_anagram(word1, word2):
    print("{} và {} là đảo chữ của nhau.".format(word1, word2))
else:
    print("{} và {} không phải là đảo chữ của nhau.".format(word1, word2))