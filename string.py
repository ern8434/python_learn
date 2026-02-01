text = """
Lorem ipsum dolor sit amet consectetur adipiscing elit
lorem ipsum dolor sit amet consectetur adipiscing
"""

print(text)

print (3* 'python ')

text = 'abcdef'
#       012345
print(text[0])

print(text[1:4])

print(text[-1])
print(text[-4:-1])


print(len(text))

print(text.title())
print(text.upper())
print(text.lower())

print(text.find('c'))
print(text.find('C'))

print(text.replace( 'c','C'))

isim = 'aBcDeF'
print(isim.lower().title())


#formatting string values
# classic method
num = 12
num2 = 7.4
print('The selected number is %d' % num)
print('The selected numbers are %d and %f' % (num,num2) )

# using format method
print( 'The selected number is {0}'.format(num) )
print( 'The selected numbers are {0} and {1}'.format(num, num2)  )















