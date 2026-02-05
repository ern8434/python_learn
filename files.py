
F= open('files/test.txt')
line = F.readline()
print(line)

#baştan başlamak için
F.seek(0)

# tek seferde içeriği almak
file_content = F.read()
print(file_content)
F.close()

# dosya kapatmak
F.close()


# satır satır okumak
F = open('files/test.txt')
for l in F:
    print(l.strip())
F.close()




