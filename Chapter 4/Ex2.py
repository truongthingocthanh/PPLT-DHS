class TaiKhoan:
    # Hàm khởi tạo với số dư mặc định là 0 nếu không truyền vào
    def __init__(self, ten_chu_the, so_du=0):
        self.ten_chu_the = ten_chu_the  # Thuộc tính Public
        self.__so_du = so_du            # Thuộc tính Private 

    # Phương thức gửi tiền (đóng vai trò như Setter có kiểm tra logic)
    def gui_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien
            print(f"-> Đã gửi thành công {so_tien}đ. Số dư hiện tại: {self.__so_du}đ")
        else:
            print("-> Lỗi: Số tiền gửi phải lớn hơn 0!")

    # Phương thức rút tiền
    def rut_tien(self, so_tien):
        if so_tien > 0 and so_tien <= self.__so_du:
            self.__so_du -= so_tien
            print(f"-> Rút thành công {so_tien}đ. Số dư còn lại: {self.__so_du}đ")
        elif so_tien <= 0:
            print("-> Thất bại: Số tiền rút phải lớn hơn 0!")
        else:
            print(f"-> Thất bại: Số dư ({self.__so_du}đ) không đủ để rút {so_tien}đ!")

    # Phương thức kiểm tra số dư (Getter)
    def kiem_tra_so_du(self):
        return self.__so_du


tk_sinh_vien = TaiKhoan("Nguyễn Văn A")
print(f"Chủ thẻ: {tk_sinh_vien.ten_chu_the}")
print(f"Số dư ban đầu: {tk_sinh_vien.kiem_tra_so_du()}đ")
print("-" * 30)

# Thử nghiệm gửi tiền
tk_sinh_vien.gui_tien(500000)   # Hợp lệ
tk_sinh_vien.gui_tien(-50000)   # Không hợp lệ (Số âm)
print("-" * 30)

# Thử nghiệm rút tiền
tk_sinh_vien.rut_tien(200000)   # Hợp lệ
tk_sinh_vien.rut_tien(1000000)  # Thất bại (Vượt quá số dư)