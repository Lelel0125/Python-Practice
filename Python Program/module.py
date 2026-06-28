# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# print(help("modules"))

# import math
# import math as m
# from math import e

# a, b, c, d, e = 1, 2, 3, 4, 5
# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)
# print(math.e ** e)

import Exmodule

result = Exmodule.pi
result = Exmodule.square(3)
result = Exmodule.cube(3)
result = Exmodule.circumference(3)
result = Exmodule.area(3)

print(result)