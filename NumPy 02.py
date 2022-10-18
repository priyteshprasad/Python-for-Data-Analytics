import numpy as np

x = np.arange(6).reshape(2,3)
print('''operations with constants''')
print(x + 10, end='\n\n')
print(x * 3, end='\n\n')
print(x % 2) 

print('''operations between arrays''')
x = np.array([[-1, 1], [-2, 2]])
y = np.array([[4, -4], [5, -5]])
print(x + y, end='\n\n')
print(x * y)

print('''operation b/w arrays with different size''')
x = np.array([[-1, 1], [-2, 2]])
y = np.array([-10, 10])
print(x * y)