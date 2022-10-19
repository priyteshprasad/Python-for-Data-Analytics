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

print('''predefined math funcions on array''')
x = np.array([[2,4], [5,8]])
print(np.square(x), end='\n**********\n')
print(np.sin(x), end="\n^^^^^^^^^\n")
print(np.sqrt(x),end="\n----------\n")
print(np.cbrt(x),end="\n----------\n")
print(np.log10(x),end="\n----------\n")
print(np.reciprocal(x),end="\n----------\n")

print("sum operation/function over array")
x = np.array([[0,1,3], [2, 3, 4]])
print(x)
print(x.sum(), end='\n\n')
print(x.sum(axis=0), end='\n\n')      # sum of each column: list with ith element as sum of ith column
print(x.sum(axis=1))                  # sum of each row 

print("Indexing and slicing of 1D array")
x = np.array([5, 10, 15, 20, 25, 30, 35])
print(x[1])  # Indexing
print(x[1:6]) # Slicing
print(x[1:6:3]) # Slicing


print("Indexing and slicing of 2D array")
y = np.array([[11, 12, 13, 14, 15],
              [21, 22, 23, 24, 25],
              [31, 32, 33, 34, 35],
              [41, 42, 43, 44, 45]])
print(y[0:3, 1:3]) 
# print(y[1])   
print(y[:, 1]) #print a column in horizontal array 


print(" Indexing and slicing of nD array")
z = np.array([[[-1, 1], [-2, 2]],
              [[-4, 4], [-5, 5]],
              [[-7, 7], [-9, 9]]])
print(z[1,:,1]) # index 1 element in row of index 1
print(z[1:,1,:]) # From all outer rows except the first, select 1st index element (which itself is an array) completely.
print(z[2]) # print 2nd index element

print("Boolean Indexing")
x = np.arange(10).reshape(2,5)
print(x)
condition = x % 2 == 0
print(condition)
print(x[condition])

print("Some tried outputs for practice")
x = np.arange(4)
print(x.flatten())

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x[[0, 1, 2], [0, 1, 1]])

x = np.arange(30).reshape(3,5,2)
print(x[1][::2][1])

x = np.array([[0, 1], [1, 1], [2, 2]])
print(x.sum(1))

x = np.array([[-2], 
              [2]])
y = np.array([[-3, 3]])
print(x + y)

x = np.arange(4)
y = np.arange(4)

print(x == y)

z = np.eye(2)
print(z)


x = np.array([[0, 1], [1, 1], [2, 2]])
print(x)
y = x.sum(-1)
print(y)
print(x[y < 2, :])

x = np.arange(4).reshape(2,2)
y = np.arange(4, 8).reshape(2,2)

print(np.hstack((x,y)))
























