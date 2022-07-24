import numpy as np
import random

l = 3
h = 4
a = np.random.randint( -10, 10, size = (l, h) )

print( a )
pos = random.randint( 0, 12 )
print(pos)
print( a[int(11/4)][11%4] )
print( a[ int(pos/h) ][ pos%h ] )


