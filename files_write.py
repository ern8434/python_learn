
# dosya açma modları (ikinci parametre)
# r: salt okunur
# w: yazma (mevcut dosya ise içeriği silinir, yeni dosya oluşturmak için kullanılabilir)
# a: sonuna ekleme
# b: binary
# t (default): salt metin
# +: güncelleme (okuma ve yazma)

F= open('files/test.txt','a')

F.write('\n\n')
F.write('new line added\n')
F.write('another line added\n')

F.close() # F.flush() otomatik olarak çalıştırılır ve diske kaydedilir


