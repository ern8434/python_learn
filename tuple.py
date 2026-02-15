
values = (365, 24, 7)
print('Bir yılda %d gün vardır \nBir günde %d saat vardır\nHaftada %d gün vardır' % values)

# indeks ile erişim
print(values[1])

# !!! tuple türünde veri ataması yapılamaz
# values[1] = 48
# TypeError: 'tuple' object does not support item assignment

# harici değişkenlere atama yapılabilir
(a,b,c) = (12,24,63)
print('a:',a)
print('b:',b)
print('c:',c)


