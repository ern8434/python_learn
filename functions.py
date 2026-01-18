
def f(x):
    '''gelen sayıya 5 ekler'''
    y= x+5
    return y

print(f(3))




#default parametreli fonksiyon
def kokAl(sayi,derece=2):
    kok = sayi**(1/derece)
    return kok

print( kokAl(9) )

print( kokAl(125,3) )


