from numpy import *
arr = array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24]])
mat = matrix(arr)
print(mat)
print(arr[2,1:4])#2
print(arr[:2,1:4])#3
print(arr[:,3:6])#4
print(arr[:,:3])#6
print(arr[:,1:3])#7
print(mat.transpose())
transpose = mat.transpose()
print(transpose[:3,:4])#1
print(transpose[3:6,:4])#5
print(transpose[3:6,1:3])#8
print(transpose[1:,:2])#10
print('9',arr[0:2,::-1])
print('3',arr[1::-1,1:4])