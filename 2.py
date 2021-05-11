import numpy as np
import math

#def magnitude(vector): 
#    return math.sqrt(sum(pow(element, 2) for element in vector))

# displaying the original vector
v = np.array([0, 1, 2])
print('Vector:', v)
w=np.array([3,4,5])
vector_sum=v+w  
vector_dot=np.dot(v,w)
# computing and displaying the magnitude of the vector
print('|v|+|w|(', np.linalg.norm(v)+np.linalg.norm(w),')>|v+w|(',np.linalg.norm(vector_sum),')' )

print('|v|.|w|(',np.linalg.norm(v)*np.linalg.norm(w),')>|v.w|(',np.linalg.norm(vector_dot),')' )