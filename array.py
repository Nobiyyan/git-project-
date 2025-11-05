import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

list = [1,2,3,4,5]
print(list)
print(type(list))

a = np.array([2,4,6])
b = np.array([1,3,5])
print(a+b)
print(a*b)

arr = np.array([1,2,3])
print(arr*2)
print(arr.mean())
print(np.mean(arr))
print(arr[0:3])
print(arr[0])
print(arr[0] + arr[1])

twod = np.array([
            [1,2,3],
            [4,5,6]])


print(twod)

threed = np.array([
    [[1,2],
     [3,4]],

    [[5,6],
     [7,8]],

    [[9,10],
     [11,12]]
])
print(threed.ndim)
print(threed)

contoharr = np.array([1,2,3], dtype="S")
print(contoharr)
print(contoharr.dtype, "Rekayasa Perangkat Lunak")