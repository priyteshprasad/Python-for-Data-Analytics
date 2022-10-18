
import numpy as np
x = np.array([5, 8, 9, 10, 11]) # using 'array' method

print("The type of object x is: ",type(x), sep=" ")   # Displays type of array 'x'

y = np.array([[6,   9], 
              [10, 82],
              [3,   5]])  
print(y)

'''
Some of the important attributes of a ndarray:

      ndim : Returns number of dimensions.
      shape: Returns Shape in tuple.
      size : Total number of elements.
      dtype : Type of each element.
      itemsize : Size of each element in Bytes.
      nbytes : Total bytes consumed by all elements.
'''

print("\nDimension: ",y.ndim,"\nShape: ", y.shape,"\nSize: ", y.size,"\nData type: ", y.dtype,"\nItem size: ", y.itemsize,"\nTotal bytes: ", y.nbytes, sep=" ")


print('''Data type can be explicitly specified with dtype argument.''')
y = np.array([[6, 9, 5],
              [10, 82, 34]], 
            dtype='float64')  
print(y)
print(y.dtype)


x = np.array([[3.2, 7.8, 9.2],
            [4.5, 9.1, 1.2]], dtype='int64')
print(x.itemsize)
print(x.flags)            # 


print(''' ndarray from list''')
# import numpy as np
a = [[[4.1, 2.5], [1.1, 2.3], [9.1, 2.5]], 
    [[8.6, 9.9],[3.6, 4.3], [6.6, 0.3]]]
x = np.array(a, dtype='float64')
print(type(x), x.ndim, x.shape)

''' ndarray using zeros method'''
x = np.zeros(shape=(2,4))
print(x)

''' ndarray using full method'''
y = np.full(shape=(2,3,2), fill_value=10.5)
print(y)

''' ndarry using arange method'''
x = np.arange(3, 15, 2.5) # 2.5 is step
print(x)

''' ndarry using linespace method'''
y = np.linspace(3, 15, 5) # 5 is size of array 'y'
print(y)

'''array using random attribute '''
np.random.seed(100)
x = np.random.randn(3) # Standard normal distribution
print(x)

'''array with normal distribution'''
np.random.seed(100)
x = 10 + 2*np.random.randn(3) # normal distribution with mean 10 and sd 2
print(x)


'''array using string '''
from io import StringIO
import numpy as np

x = StringIO('''88.25 93.45 72.60 90.90
72.3 78.85 92.15 65.75
90.5 92.45 89.25 94.50
''')
print(x)
d = np.loadtxt(x,delimiter=' ')
print(d)
print(d.ndim, d.shape)

'''---------------'''
x = np.array([[-1,0,1], [-2, 0, 2]])
y = np.zeros_like(x)
print(y)


import numpy as np

np.random.seed(100)
x = np.random.randint(10, 100, 8)
print(x, end='\n\n')
y = x.reshape(2,4) 
print(y, end='\n\n')
z = x.reshape(2,2,2)
print(z, '\n\n')

'''stacking arrays vertically'''
import numpy as np
x = np.array([[-1, 1], [-3, 3]])
y = np.array([[-2, 2], [-4, 4]])
print(np.vstack((x,y)))
'''stacking arrays horizontilly'''
x = np.array([[-1, 1], [-3, 3]])
y = np.array([[-2, 2], [-4, 4]])
z = np.array([[-5, 5], [-6, 6]])
a = np.hstack((x,y,z))
print(a)

'''splitting an ndarray using vsplit'''
import numpy as np
# x = np.arange(30).reshape(6, 5)
# res = np.vsplit(x, 2)
# print(res[0], end='\n\n')
# print(res[1])

'''splitting array vertically into 3 arrays'''
x = np.arange(10).reshape(5, 2)
print(x)
res = np.vsplit(x, (2,4,5)) # split array at r0w2, row 4, row 5
print(res)
print(res[0], end='\n-------------------\n')
print(res[1], end='\n-------------------\n')
print(res[2], end="\n-------------------\n")
print(res[3])

'''splitting array horizontally'''
x = np.arange(10).reshape(2, 5)
print(x)
res = np.hsplit(x, (2,4)) # split horizontally at column 2, column 4
print(res[0], end='\n^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')
print(res[1], end='\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')
print(res[2])







