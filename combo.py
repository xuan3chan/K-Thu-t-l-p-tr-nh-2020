

from re import S


Sd#bai4
# def timgiatri(e):
#     nhapdodaidanhsach=int(input('nhap do dai danh sach'))
#     listt=[]
#     for i in range(1,nhapdodaidanhsach+1):
#         a=listt.append(int(input(f'{i}nhap so vao danh sach: ')))
#     for check in listt:
#         if e in listt:
#             print(f'{e} co trong danh sach')
#             break 
#         else:
#             print(f'{e} không có trong danh sách')
#             break 
# timgiatri(e=int(input('so can tim:')))
#bai5
# def timgiatri(e):
#     nhapdodaidanhsach=int(input('nhap do dai danh sach'))
#     listt=[]
#     for i in range(1,nhapdodaidanhsach+1):
#         listt.append(int(input(f'{i}nhap so vao danh sach: ')))
#     print(f'có {listt.count(e)} lần của {e}')
    
# timgiatri(e=int(input('so can tim:')))
#bài 6 
# def timgiatri():
#     nhapdodaidanhsach=int(input('nhap do dai danh sach'))
#     listt=[]
#     for i in range(1,nhapdodaidanhsach+1):
#         listt.append(int(input(f'{i}nhap so vao danh sach: ')))
#     print(f'danh sach đa nhap theo thu tu tang dan{sorted(listt)}')
# timgiatri()
#bai 7
# def timgiatri():
#     nhapdodaidanhsach=int(input('nhap do dai danh sach'))
#     listt=[]
#     for i in range(1,nhapdodaidanhsach+1):
#         listt.append(int(input(f'{i}nhap so vao danh sach: ')))
#     print(f'danh sach đa nhap theo thu tu giam dan{sorted(listt,reverse=True)}')
# timgiatri()
#bai8
# def timgiatri():
#     nhapdodaidanhsach=int(input('nhap do dai danh sach'))
#     listt=[]
#     for i in range(1,nhapdodaidanhsach+1):
#         listt.append(int(input(f'{i}nhap so vao danh sach: ')))
#     print(f'so lớn nhất trong danh sách là {max(listt)}')
# timgiatri()
# #bai9
# def timgiatri():
#     nhapdodaidanhsach=int(input('nhap do dai danh sach'))
#     listt=[]
#     for i in range(1,nhapdodaidanhsach+1):
#         listt.append(int(input(f'{i}nhap so vao danh sach: ')))
#     print(f'so nhỏ nhất trong danh sách là {min(listt)}')
# timgiatri()
#bai14
# def muatrongthang(x):
#     xuan=[1,2,3]
#     ha=[4,5,6]
#     thu=[7,8,9]
#     dong=[10,11,12]
#     if x in xuan:
#         print('mùa xuấn tới gòi')
#     elif x in ha:
#         print('mùa hạ tới gòi')
#     elif x in thu:
#         print('mùa thu tới gòi')
#     elif x in dong:
#         print('mùa đông tới gòi')
# muatrongthang(x=int(input('nhập tháng:')))
#bai 15
# def nam(x):
#     if (x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0)):
#         print(f'{x} năm nhuận')
#     else:
#         print(f'{x} năm 0 nhuận')
# nam(x=int(input('nhập vào nam')))
#bai 17
def trungbinhcong(a,b):
    cacso=[]
    tong=0
    for i in range(a,b+1):
        cacso.append(i)
    for c in cacso:
        tong+=c
    AVerg=tong/len(cacso)
    return AVerg
a=int(input('nhập số a:'))
b=int(input('nhập số b:'))
while a <=0:
    a=int(input('nhập lại số a:'))
print(trungbinhcong(a,b))
s,dm;asmd

