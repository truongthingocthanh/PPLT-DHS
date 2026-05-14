# TẦNG DỮ LIỆU (Mô hình hóa Thực thể)
class Sach:
    # Hàm khởi tạo với trạng thái mặc định là "Sẵn sàng"
    def __init__(self, ma_sach, ten_sach, tac_gia, trang_thai="Sẵn sàng"):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.trang_thai = trang_thai

    # Phương thức in thông tin của cuốn sách
    def hien_thi(self):
        print(f"Mã: {self.ma_sach:^5} | Tên sách: {self.ten_sach:<25} | Tác giả: {self.tac_gia:<18} | Trạng thái: {self.trang_thai}")


# TẦNG NGHIỆP VỤ (Lớp Quản lý Hệ thống)
class QuanLyThuVien:
    def __init__(self):
        # Mảng lưu trữ danh sách các đối tượng Sách
        self.danh_sach_sach = []

    def them_sach(self, sach_moi):
        self.danh_sach_sach.append(sach_moi)
        print("\n-> Đã thêm sách mới vào thư viện thành công!\n")

    def hien_thi_tat_ca(self):
        if not self.danh_sach_sach:
            print("\n-> Thư viện hiện đang trống.\n")
            return
            
        print("\n" + "="*80)
        print(f"{'DANH SÁCH SÁCH TRONG THƯ VIỆN':^80}")
        print("="*80)
        for sach in self.danh_sach_sach:
            sach.hien_thi() # Gọi phương thức hiển thị của từng đối tượng Sách
        print("-" * 80 + "\n")

    def muon_sach(self, ma_sach):
        # Duyệt qua mảng để tìm sách
        for sach in self.danh_sach_sach:
            if sach.ma_sach == ma_sach:
                # Nếu tìm thấy, kiểm tra trạng thái
                if sach.trang_thai == "Sẵn sàng":
                    sach.trang_thai = "Đã mượn"
                    print(f"\n-> Mượn sách '{sach.ten_sach}' thành công!\n")
                else:
                    print(f"\n-> Thất bại: Sách '{sach.ten_sach}' hiện đã có người mượn!\n")
                return # Kết thúc hàm ngay khi đã xử lý xong cuốn sách tìm thấy
        
        # Nếu duyệt hết mảng mà không thấy
        print("\n-> Thất bại: Không tìm thấy sách nào với mã này!\n")


# TẦNG GIAO DIỆN (Menu điều khiển CLI)
def main():
    # Khởi tạo đối tượng quản lý thư viện
    thu_vien = QuanLyThuVien()
    
    # Thêm sẵn một vài cuốn sách để dễ dàng test chương trình
    thu_vien.them_sach(Sach("S01", "Lập trình Python", "Trần Văn Long"))
    thu_vien.them_sach(Sach("S02", "Cấu trúc dữ liệu", "Nguyễn Văn A"))

    # Vòng lặp vô hạn cho CLI
    while True:
        print("=== HỆ THỐNG QUẢN LÝ THƯ VIỆN ===")
        print("1. Thêm sách mới")
        print("2. Hiển thị danh sách sách")
        print("3. Mượn sách")
        print("4. Thoát")
        
        lua_chon = input("Nhập lựa chọn của bạn (1-4): ")
        
        if lua_chon == '1':
            ma = input("Nhập mã sách: ")
            ten = input("Nhập tên sách: ")
            tac_gia = input("Nhập tên tác giả: ")
            # Tạo đối tượng Sách mới và đưa vào mảng
            sach_moi = Sach(ma, ten, tac_gia)
            thu_vien.them_sach(sach_moi)
            
        elif lua_chon == '2':
            thu_vien.hien_thi_tat_ca()
            
        elif lua_chon == '3':
            ma_muon = input("Nhập mã sách cần mượn: ")
            thu_vien.muon_sach(ma_muon)
            
        elif lua_chon == '4':
            print("\nĐang thoát chương trình. Tạm biệt!")
            break
            
        else:
            print("\n-> Lựa chọn không hợp lệ, vui lòng nhập lại!\n")

# Điểm neo chạy chương trình chính
if __name__ == "__main__":
    main()