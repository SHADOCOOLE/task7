import numpy as np
#task 1
letters  = np.array(['a', 'b', 'c', 'd', 'e',
                      'f', 'g', 'h', 'i', 'j'])
print("dtype of array:", letters.dtype)
print("shape of array:", letters.shape)
print("size of array:", letters.size)
#task 2
builtin = np.arange(2,34,2).reshape (4, 4)
print("array using arange")
print( builtin)
lin = np.linspace(2,32,16, dtype = int).reshape(4,4)
print("array using linspace")

print(lin)

# Task 3
arr = np.arange(1, 26).reshape(5, 5)
print("5*5 array:")
print(arr)

odd_numbers = arr[arr % 2 != 0]
print("Odd numbers in the array:")
print(odd_numbers)
