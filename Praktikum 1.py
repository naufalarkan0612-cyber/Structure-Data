# Nama : Naufal Arkan El Rochim
# NPM : 2505060068
# Matkul : Structure Data

import array as arr

# Membuat Array
a = arr.array('i',[1,2,3])
print("The new created array is : ", end=" ")

b = arr.array('d', [2.5, 3.2, 3.3])
print("The new created array is :", end=" ")

c = arr.array('d', [6, 7, 8, 8, 9, 10])
print("The new created array is :", end=" ")

for i in range(0, 3):
  print(a[i], end=" ")

print()

for i in range(0, 3):
  print(b[i], end=" ")

print()

for i in range(0, 3):
  print(c[i], end=" ")

print()

# Menambahkankan Elemen Array
a.insert(1, 4)
print("Array after insertion :", end=" ")

for i in (a):
  print(i, end=" ")

print()

b.append(4.4)
print("Array after insertion :", end=" ")

for i in (b):
  print(i, end=" ")

print()

# Mengakses Elemen Array
print("Access element is : ", a[0])
print("Access element is : ", b[2])

# Menghapus Elemen Array
print("The popped element is : ", end=" ")

print(a.pop(2))
print("The array after popping is : ", end=" ")

for i in range(0, 2):
  print(a[i], end=" ")

print("\r")

b.remove(2.5)
print("The array after removing is :", end=" ")

for i in range(0, 2):
  print(b[i], end=" ")

# Pemotongan Elemen Array

c = a[3 : 8]
print("\nSlicing elements in a range 3-8: ")
print(c)

c = a[5:]
print("\nElements sliced from 5th"
"element till the end: ")
print(c)

c = a[:]
print("\nPrinting all elements using slice operation: ")
print(c)

# Mengubah Elemen Array
c[2] = 6
print("Array after updation:", end=" ")

for i in range(3):
  print(c[i], end=" ")

print()

# Extend dalam Array
a.extend([6, 7, 8 , 9, 10])
print("\nThe array after extend", end=" ")

for i in range(0, 8):
  print(a[i],end=" ")

print()

# Menghitung elemen
count = a.count(2)
print("Number of occurrences of 2 :", count)

# Membalik susunan index
print("Original array :", *b)
b.reverse()
print("Reversed array : ", *b)