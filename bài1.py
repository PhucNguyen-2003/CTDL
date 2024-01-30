def dao_nguoc_danh_sach(danh_sach):
    # Sử dụng hai con trỏ, một ở đầu danh sách và một ở cuối danh sách
    dau = 0
    cuoi = len(danh_sach) - 1
    while dau < cuoi:
        # Hoán đổi các phần tử tại vị trí đầu và cuối
        danh_sach[dau], danh_sach[cuoi] = danh_sach[cuoi], danh_sach[dau]
        # Di chuyển con trỏ đến phần tử tiếp theo
        dau += 1
        cuoi -= 1
    return danh_sach
# Kiểm tra hàm với danh sách đầu vào
danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(dao_nguoc_danh_sach(danh_sach))
