import math 
def ptbac2(a,b,c):
    delta= b**2-4*a*c
    if delta >0:
        x1=(-b+math.sqrt(delta))/2*a
        x2=(-b-math.sqrt(delta))/2*a
        return x1,x2
    elif delta == 0:
        x12=-b/2*a
        return x12
    else:
        print('phuong trinh vo nghiem')
a=int(input("nhap so :"))
b=int(input("nhap so :"))
c=int(input("nhap so :"))
print(ptbac2(a,b,c))