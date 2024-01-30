def dao_nguoc_so(so):
    # Khởi tạo số đảo ngược là 0
    so_dao_nguoc = 0
    # Lặp cho đến khi số gốc bằng 0
    while so > 0:
        # Lấy chữ số cuối cùng của số gốc
        chu_so = so % 10
        # Thêm chữ số vào số đảo ngược
        so_dao_nguoc = so_dao_nguoc * 10 + chu_so
        # Loại bỏ chữ số cuối cùng của số gốc
        so = so // 10
    return so_dao_nguoc
# Kiểm tra hàm với một số đầu vào
so = 6789
print(dao_nguoc_so(so))
