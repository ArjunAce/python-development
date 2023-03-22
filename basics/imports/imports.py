# option 1
import math_operations
math_operations.add(3, 4)

# option 2
from math_operations import add, multiply
add(3, 4)

# option 3
from math_operations import *
add(3, 4)

# option 4
from math_operations import add as custom_add
custom_add(3, 4)
