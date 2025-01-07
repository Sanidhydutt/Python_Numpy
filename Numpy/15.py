import numpy as np

x = [[1,2,3],[4,5,6],[7,8,9]]

arr = np.array(x)

print(arr)

#arr = arr.sum(axis=0)
arr = arr.sum(axis=1)
print(arr)




