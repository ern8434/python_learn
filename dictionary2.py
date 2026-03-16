
sozluk = {
    'one':'bir',
    'two':'iki'
}

print( sozluk.keys())
print( sozluk.values())

items = sozluk.items()
print(items) # tuple listesi biçiminde

print( sozluk.get('one','[undefined]') )
print( sozluk.get('three','[undefined]') )
