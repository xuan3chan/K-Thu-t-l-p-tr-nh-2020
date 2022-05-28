#bai2
def max2so():
    a=int(input("nhap so :"))
    b=int(input("nhap so :"))
    if   a>b:
        return print(a)
    elif a<b:
        return print(b)
print(max2so())
#3so
def max3so():
    a=int(input("nhap so :"))
    b=int(input("nhap so :"))
    c=int(input("nhap so :"))
    if   a>b>c:
        return print(a)
    elif a<b<c:
        return print(c)
    else:
        return print(b)
print(max3so())

