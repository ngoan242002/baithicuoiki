hoten = input("Nhập họ và tên: ")
print(hoten)
def soTN(x):
    so1 = str(x);
    so2 = so1[::-1];
    if (so1 == so2):
        return True;
    else:
        return False;
x = int(input("Nhập số nguyên dương x : "));
print("Tổng các chữ số của", x, "là", soTN(x));


