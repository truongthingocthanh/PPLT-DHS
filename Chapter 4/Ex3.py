# TẦNG DỮ LIỆU (Mô hình hóa Thực thể)
# 1. Lớp Cha
class NhanVien:
    def __init__(self, ma_nv, ten):
        self.ma_nv = ma_nv
        self.ten = ten

    # Phương thức chung (Giao diện)
    def tinh_luong(self):
        pass  # Hoặc print("Chưa xác định")

# 2. Lớp Con 1 (Kế thừa NhanVien)
class NhanVienFullTime(NhanVien):
    def __init__(self, ma_nv, ten, luong_co_ban):
        super().__init__(ma_nv, ten) # Gọi hàm khởi tạo của lớp Cha
        self.luong_co_ban = luong_co_ban

    # Ghi đè (Override) phương thức tính lương
    def tinh_luong(self):
        return self.luong_co_ban

# 3. Lớp Con 2 (Kế thừa NhanVien)
class NhanVienPartTime(NhanVien):
    def __init__(self, ma_nv, ten, so_gio_lam, luong_theo_gio):
        super().__init__(ma_nv, ten)
        self.so_gio_lam = so_gio_lam
        self.luong_theo_gio = luong_theo_gio

    # Ghi đè (Override) phương thức tính lương
    def tinh_luong(self):
        return self.so_gio_lam * self.luong_theo_gio


# TẦNG NGHIỆP VỤ (Lớp Quản lý Hệ thống)
class QuanLyNhanVien:
    def __init__(self):
        # Mảng (List) chứa lẫn lộn cả NV Full-time và Part-time
        self.danh_sach_nv = []

    def them_nhan_vien(self, nv):
        self.danh_sach_nv.append(nv)
        print("-> Đã thêm nhân viên thành công!\n")

    def hien_thi_va_tinh_luong(self):
        if not self.danh_sach_nv:
            print("-> Danh sách hiện đang trống.\n")
            return
            
        print("\n--- DANH SÁCH & LƯƠNG NHÂN VIÊN ---")
        for nv in self.danh_sach_nv:
            luong = nv.tinh_luong()
            print(f"Mã NV: {nv.ma_nv} | Tên: {nv.ten:<20} | Lương: {luong:,.0f} VNĐ")
        print("-" * 35 + "\n")


# TẦNG GIAO DIỆN (Menu điều khiển)
def main():
    # Khởi tạo đối tượng quản lý
    he_thong = QuanLyNhanVien()
    
    # Thêm sẵn dữ liệu mẫu để test tính đa hình ngay từ đầu
    he_thong.them_nhan_vien(NhanVienFullTime("12S345678", "Alice", 15000000))
    he_thong.them_nhan_vien(NhanVienPartTime("PT01", "Dorris", 120, 50000))

    # Vòng lặp Menu
    while True:
        print("=== MENU HỆ THỐNG ===")
        print("1. Thêm Nhân viên Full-Time")
        print("2. Thêm Nhân viên Part-Time")
        print("3. Hiển thị danh sách và Tính lương")
        print("4. Thoát")
        
        lua_chon = input("Nhập lựa chọn của bạn (1-4): ")
        
        if lua_chon == '1':
            ma = input("Nhập Mã NV: ")
            ten = input("Nhập Tên NV: ")
            lcb = float(input("Nhập Lương cơ bản: "))
            he_thong.them_nhan_vien(NhanVienFullTime(ma, ten, lcb))
            
        elif lua_chon == '2':
            ma = input("Nhập Mã NV: ")
            ten = input("Nhập Tên NV: ")
            gio = float(input("Nhập Số giờ làm: "))
            luong_gio = float(input("Nhập Lương theo giờ: "))
            he_thong.them_nhan_vien(NhanVienPartTime(ma, ten, gio, luong_gio))
            
        elif lua_chon == '3':
            he_thong.hien_thi_va_tinh_luong()
            
        elif lua_chon == '4':
            print("Đang thoát chương trình. Tạm biệt!")
            break
            
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!\n")

# Điểm neo kích hoạt chương trình
if __name__ == "__main__":
    main()