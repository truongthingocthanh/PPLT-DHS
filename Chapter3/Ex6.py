# Bài 6: Dự án Quản lý Danh bạ (Contact Book)

# 1. Hàm thêm liên hệ mới
def add_contact(danh_ba):
    ten = input("Nhập tên: ")
    sdt = input("Nhập số điện thoại: ")
    # Định dạng chuỗi "Tên - Số điện thoại"
    lien_he = f"{ten} - {sdt}"
    danh_ba.append(lien_he)
    print("Thêm liên hệ thành công!")

# 2. Hàm hiển thị tất cả danh bạ
def show_contacts(danh_ba):
    if not danh_ba:
        print("Chưa có liên hệ nào.")
    else:
        print("--- DANH SÁCH LIÊN HỆ ---")
        # Sử dụng vòng lặp for để in danh sách kèm số thứ tự
        for i, lien_he in enumerate(danh_ba, 1):
            print(f"{i}. {lien_he}")

# 3. Hàm tìm kiếm liên hệ
def find_contact(danh_ba):
    ten_tim = input("Nhập tên cần tìm: ")
    tim_thay = False
    for lien_he in danh_ba:
        # Kiểm tra nếu tên tồn tại trong chuỗi liên hệ
        if ten_tim.lower() in lien_he.lower():
            print(f"Thông tin tìm thấy: {lien_he}")
            tim_thay = True
    
    if not tim_thay:
        print("Không tìm thấy.")

# 4. Hàm main điều phối tổng thể
def main():
    my_contacts = [] # Khởi tạo danh sách rỗng
    
    while True:
        # Hiển thị giao diện menu
        print("\n=== HỆ THỐNG QUẢN LÝ DANH BẠ")
        print("1. Thêm liên hệ mới")
        print("2. Hiển thị tất cả danh bạ")
        print("3. Tìm kiếm liên hệ")
        print("4. Thoát chương trình")
        
        lua_chon = input("Nhập lựa chọn của bạn (1-4): ")
        
        # Cấu trúc rẽ nhánh để gọi các hàm con tương ứng
        if lua_chon == '1':
            add_contact(my_contacts)
        elif lua_chon == '2':
            show_contacts(my_contacts)
        elif lua_chon == '3':
            find_contact(my_contacts)
        elif lua_chon == '4':
            print("Đang thoát chương trình...")
            break # Kết thúc vòng lặp
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")

# Chạy chương trình
if __name__ == "__main__":
    main()