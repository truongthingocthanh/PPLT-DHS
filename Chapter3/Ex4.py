# Bài 4: Xử lý Danh sách (Mảng)

# Hàm tìm số lớn nhất
def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]  # Giả định số đầu tiên là lớn nhất
    for x in lst:
        if x > max_val:
            max_val = x  # Cập nhật nếu tìm thấy số lớn hơn
    return max_val

# Hàm tìm số nhỏ nhất
def find_min(lst):
    if not lst:
        return None
    min_val = lst[0]  # Giả định số đầu tiên là nhỏ nhất
    for x in lst:
        if x < min_val:
            min_val = x  # Cập nhật nếu tìm thấy số nhỏ hơn
    return min_val

# Chạy thử nghiệm với mảng diem_so
diem_so = [6.5, 8.0, 4.5, 9.5, 7.0]
print(f"Danh sách điểm: {diem_so}")
print(f"Số lớn nhất là: {find_max(diem_so)}")
print(f"Số nhỏ nhất là: {find_min(diem_so)}")