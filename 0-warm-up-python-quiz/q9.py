import numpy as np

arr = np.array([[3, 7, 2], [5, 9, 1], [8, 4, 6]])

max_value = arr.max()
max_position = np.unravel_index(arr.argmax(), arr.shape)

print(f"최대값: {max_value}")
print(f"위치: {max_position}")
