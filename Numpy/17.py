import numpy as np

arr = np.array([[10,20,30],[40,50,60],[70,80,90]])

print(arr)

#print(arr.flat)

for i in arr.flat:
    print(i)
