# 1. TẦNG MODELS (Lớp Dữ liệu Thực thể)
class ThuCung:
    def __init__(self, ma_thu_cung, ten, loai, gia_tien):
        self.__ma_thu_cung = ma_thu_cung
        self.__ten = ten
        self.__loai = loai
        self.__gia_tien = gia_tien

    # Các phương thức Getters để lấy dữ liệu an toàn
    def get_ma_thu_cung(self):
        return self.__ma_thu_cung

    def get_ten(self):
        return self.__ten

    def get_loai(self):
        return self.__loai

    def get_gia_tien(self):
        return self.__gia_tien

    def hien_thi(self):
        print(f"Mã: {self.__ma_thu_cung:<5} | Tên: {self.__ten:<15} | Loại: {self.__loai:<15} | Giá: {self.__gia_tien:,.0f} VNĐ")


# 2. TẦNG SERVICES (Lớp Nghiệp vụ/Xử lý logic)
class CuaHangService:
    def __init__(self):
        self.kho_hang = []   # Mảng lưu trữ thú cưng đang bán
        self.doanh_thu = 0   # Khởi tạo doanh thu = 0

    def nhap_thu_cung(self, thu_cung):
        self.kho_hang.append(thu_cung)
        print(f"\n-> Nhập kho thành công: {thu_cung.get_ten()}")

    def xem_kho_hang(self):
        if not self.kho_hang:
            print("\n-> Kho hàng hiện đang trống.")
            return
            
        print("\n" + "="*65)
        print(f"{'DANH SÁCH THÚ CƯNG TRONG KHO':^65}")
        print("="*65)
        for tc in self.kho_hang:
            tc.hien_thi()
        print("-" * 65)

    def ban_thu_cung(self, ma_thu_cung):
        # Duyệt kho hàng để tìm thú cưng
        for tc in self.kho_hang:
            if tc.get_ma_thu_cung() == ma_thu_cung:
                self.kho_hang.remove(tc)                # Xóa khỏi kho
                self.doanh_thu += tc.get_gia_tien()     # Cộng tiền vào doanh thu
                print(f"\n-> Chúc mừng! Đã bán bé '{tc.get_ten()}' thành công.")
                print(f"-> Cộng {tc.get_gia_tien():,.0f} VNĐ vào doanh thu.")
                return # Thoát hàm ngay sau khi bán xong
                
        print("\n-> Lỗi: Không tìm thấy mã thú cưng này trong kho!")


# 3. TẦNG VIEWS (Lớp Giao diện Console)
class GiaoDienConsole:
    def __init__(self):
        # Khởi tạo Service để giao diện có thể gọi các hàm xử lý logic
        self.service = CuaHangService()
        
        self.service.nhap_thu_cung(ThuCung("TC01", "Bé Mun", "Mèo đen", 1200000))
        self.service.nhap_thu_cung(ThuCung("TC02", "Bơ Mập", "Chó Corgi", 5500000))
        self.service.nhap_thu_cung(ThuCung("TC03", "Bông", "Mèo Ba Tư", 3000000))

    def chay_chuong_trinh(self):
        while True:
            print("\n=== QUẢN LÝ CỬA HÀNG THÚ CƯNG (PET STORE) ===")
            print("1. Nhập thú cưng mới")
            print("2. Hiển thị kho hàng")
            print("3. Bán thú cưng")
            print("4. Xem tổng doanh thu")
            print("5. Thoát")
            
            lua_chon = input("Nhập lựa chọn của bạn (1-5): ")
            
            if lua_chon == '1':
                ma = input("Nhập mã thú cưng: ")
                ten = input("Nhập tên thú cưng: ")
                loai = input("Nhập giống/loài: ")
                gia = float(input("Nhập giá tiền: "))
                
                # Tạo đối tượng ThuCung mới và truyền xuống tầng Service
                tc_moi = ThuCung(ma, ten, loai, gia)
                self.service.nhap_thu_cung(tc_moi)
                
            elif lua_chon == '2':
                self.service.xem_kho_hang()
                
            elif lua_chon == '3':
                ma_ban = input("Nhập mã thú cưng cần bán: ")
                self.service.ban_thu_cung(ma_ban)
                
            elif lua_chon == '4':
                print(f"\n-> TỔNG DOANH THU HIỆN TẠI: {self.service.doanh_thu:,.0f} VNĐ")
                
            elif lua_chon == '5':
                print("\nĐóng cửa hàng. Hẹn gặp lại!")
                break
                
            else:
                print("\n-> Lựa chọn không hợp lệ, vui lòng nhập lại!")

# ĐIỂM NEO KHỞI CHẠY (ENTRY POINT)
if __name__ == "__main__":
    app = GiaoDienConsole()
    app.chay_chuong_trinh()