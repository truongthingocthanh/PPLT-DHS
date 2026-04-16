# Bài 1: 
# Nhập số km từ bàn phím và chuyển sang kiểu số thực (float)
so_km = float(input("Nhập số km taxi đã đi: "))

# Khởi tạo biến tổng tiền
tong_tien = 0

# Sử dụng cấu trúc rẽ nhánh để tính giá theo từng mốc
if so_km <= 0:
    tong_tien = 0
    print("Số km không hợp lệ.")
elif so_km <= 1:
    # Mức 1: 1 km đầu tiên
    tong_tien = so_km * 15000
elif so_km <= 20:
    # Mức 2: 1km đầu + các km tiếp theo đến km 20
    tong_tien = 1 * 15000 + (so_km - 1) * 12000
else:
    # Mức 3: 1km đầu + 19km mức giá hai + các km từ 21 trở đi
    tong_tien = 1 * 15000 + 19 * 12000 + (so_km - 20) * 10000

# In ra số tiền khách phải trả
print(f"Tổng số tiền taxi phải trả là: {tong_tien:,.0f} VNĐ")