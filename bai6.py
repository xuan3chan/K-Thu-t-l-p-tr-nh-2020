import time 
def tuoine(tuoinhap):
    year=time.localtime()
    tuoi=int(year)-tuoinhap
    return tuoi
print(tuoine(tuoinhap=int(input('nhap nam sinh cua ban:'))))