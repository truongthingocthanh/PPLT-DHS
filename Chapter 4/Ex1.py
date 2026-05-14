# Khai báo Lớp 
class HinhChuNhat:
    # Hàm khởi tạo 
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai # Thuộc tính
        self.chieu_rong = chieu_rong # Thuộc tính

    # Phương thức tính chu vi tuân thủ snake_case
    def tinh_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2

    # Phương thức tính diện tích tuân thủ snake_case
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong


hcn1 = HinhChuNhat(5, 3)
hcn2 = HinhChuNhat(10.5, 4)

# In kết quả
print("--- Hình Chữ Nhật 1 ---")
print(f"Chu vi: {hcn1.tinh_chu_vi()}")
print(f"Diện tích: {hcn1.tinh_dien_tich()}")

print("\n--- Hình Chữ Nhật 2 ---")
print(f"Chu vi: {hcn2.tinh_chu_vi()}")
print(f"Diện tích: {hcn2.tinh_dien_tich()}")