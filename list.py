
# list
arr = []
#print (type(arr))

arr.append(1)
arr.append(2)
arr.append(3)
#print(arr[0])

n = len(arr)
i=0
while i<n:
    print(arr[i])
    i += 1

if 4 in arr:
    print('4 in arr')
else:
    print('4 is not in arr')


arr  = ['a','b','c','d']

for x in arr:
    print(x)

for i in range(10):
    print(i)


last = print(arr.pop())
print(arr)

arr  = ['a','b','c','d']

last = print(arr.pop())
print(arr)

arr.remove('b')
print(arr)

if 'e' in arr:
    arr.remove('e')

arr.append('x')
print( arr.count('x') )
print(arr)
print(arr.index('x'))

arr.reverse()
print(arr)
print(sorted(arr))
arr.sort()
print(arr)

arr.insert(2,'z')
print(arr)
arr.sort()
print(arr)

arr2 = ['x','y','z']

arr.extend(arr2)
print(arr)


#copy list to another
arr2 = arr[:]

arr2.append('Z')
print(arr)
print(arr2)




