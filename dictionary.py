
sozluk = {
    'one':'bir',
    'two':'iki'
}

sozluk['key'] = 'anahtar'
sozluk['value'] = 'değer'

print(sozluk)

if 'key' in sozluk:
    print(sozluk['key'])
else:
    print('sözlükte yok')

cumle = 'How do you want your coffee?'

s = {}

for i in cumle:
    if i in s: # zaten varsa değerini arttır
        s[i] = s[i]+1
    else:
        s[i] = 1 # ilk kez ekleniyor

print ('Cümledeki harf analizi')
for i in sorted(s):
    print(i,' => ',s[i])

print('\n Boşluk dahil toplam %d çeşit karakter vardır' % len(s))


