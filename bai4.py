def giaithua(n):
    giaithua=1
    for i in range(2,n+1):
        giaithua=i*giaithua
    return giaithua
print(giaithua(n=int(input('nhap vao 1 so:'))))

