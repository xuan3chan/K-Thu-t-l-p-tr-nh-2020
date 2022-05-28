
def ktra_so_nguyen_to(n):
    kt= True
    if n<2:
        kt = False
    elif n == 2:
        kt=True
    elif (n%2)==0:
        kt=False
    else:
        for i in range(3,n,2):
            if (n%i) == 0:
                kt=False
            
    return kt
n = int(input("nhap so tu nhien:"))

if ktra_so_nguyen_to(n) is True:
    print(n,"la so nguyen to")
else:
    print(n,"khong phai so nguyen to")

