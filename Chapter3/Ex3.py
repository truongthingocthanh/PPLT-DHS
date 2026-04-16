# Bài 3: Kiểm tra số nguyên tố

# Định nghĩa hàm is_prime(n)
def is_prime(n):
    # Số nguyên tố phải lớn hơn 1
    if n < 2:
        return False
    # Vòng lặp kiểm tra từ 2 đến n-1
    for i in range(2, n):
        if n % i == 0:
            # Nếu chia hết cho bất kỳ số nào khác 1 và chính nó thì không phải số nguyên tố
            return False
    return True

# Đoạn code gọi hàm để in ra các số nguyên tố từ 1 đến 100
print("Các số nguyên tố từ 1 đến 100 là:")
for i in range(1, 101):
    if is_prime(i):
        print(i, end=" ")