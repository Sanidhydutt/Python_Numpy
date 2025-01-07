import numpy as np

arr = np.arange(100)

arr = arr.reshape(4,25)

#make 1d array again
arr = arr.ravel()

print(arr)



