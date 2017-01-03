import cmath
import math
z=raw_input()
a=cmath.phase(complex(z))
b=abs(complex(z))
print("{0}\n{1}".format(b,a))