# Bài 5: Máy tính điện tử (Calculator Bot)

# Định nghĩa các hàm toán học cơ bản
def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    # Kiểm tra điều kiện chia cho 0 để tránh lỗi chương trình
    if b == 0:
        return "Lỗi chia cho 0"
    else:
        return a / b

# Hàm hiển thị menu lựa chọn
def hien_thi_menu():
    print("\n--- MÁY TÍNH ĐIỆN TỬ ---")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")

# Luồng thực thi chính của chương trình
def main():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn (1-5): ")

        if lua_chon == '5':
            print("Đang thoát chương trình...")
            break

        if lua_chon in ['1', '2', '3', '4']:
            # Nhập dữ liệu đầu vào cho phép toán
            try:
                a = float(input("Nhập số thứ nhất (a): "))
                b = float(input("Nhập số thứ hai (b): "))
                
                if lua_chon == '1':
                    print(f"Kết quả: {a} + {b} = {cong(a, b)}")
                elif lua_chon == '2':
                    print(f"Kết quả: {a} - {b} = {tru(a, b)}")
                elif lua_chon == '3':
                    print(f"Kết quả: {a} * {b} = {nhan(a, b)}")
                elif lua_chon == '4':
                    print(f"Kết quả: {a} / {b} = {chia(a, b)}")
            except ValueError:
                print("Lỗi: Vui lòng nhập vào một số thực hợp lệ.")
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5.")

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()