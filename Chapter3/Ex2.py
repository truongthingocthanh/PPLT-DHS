# Bài 2: Vòng lặp For và Cập nhật trạng thái
# Nhập số nguyên dương n từ bàn phím
n = int(input("Nhập vào một số nguyên dương n: "))

# Khởi tạo các biến tích lũy trạng thái ban đầu
tong_chan = 0
tong_le = 0

# Sử dụng vòng lặp for chạy từ 1 đến n
for i in range(1, n + 1):
    # Kiểm tra số chẵn hay lẻ bằng phép chia lấy dư %
    if i % 2 == 0:
        # Nếu chia hết cho 2 là số chẵn, cập nhật vào tong_chan
        tong_chan = tong_chan + i
    else:
        # Ngược lại là số lẻ, cập nhật vào tong_le
        tong_le = tong_le + i

# In kết quả ra màn hình theo yêu cầu
print(f"1. Tổng các số lẻ từ 1 đến {n} là: {tong_le}")
print(f"2. Tổng các số chẵn từ 1 đến {n} là: {tong_chan}")