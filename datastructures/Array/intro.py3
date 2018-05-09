# Python code to demonstrate the working of
# array(), append(), insert()

# for array operation import array
import array

arr = array.array('i', [1,2,3])

for i in range(0,3):
    print(arr[i], end = " ")

for i in range(0,3):
    print(arr[i], end = " ")

arr.append(4)

print("Array after append: ")

for i in range(0,4):
    print(arr[i], end = " ")

arr.insert(2,6)

for i in range(5):
    print(arr[i], end = " ")