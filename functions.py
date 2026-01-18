
# açıklamalı fonksiyon ( help(f) ile açıklama gösterilir )
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



# çoklu sonuç döndürme
def cember(r):
    c=2*3.14*r
    a=3.14*(r**2)
    return c,a

print(cember(4)) # tuple türünde

cevre,alan = cember(4)
print(cevre)
print(alan)
