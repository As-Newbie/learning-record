import day18_mytools
print(day18_mytools.say_hello("ChatGPT"))
print(day18_mytools.square(5))

import day18_mytools
from day18_mytools import say_hello
print(say_hello("直接 import mytools"))
from day18_mytools import square
square(6)
print(day18_mytools.say_hello("ChatGPT"))
print(day18_mytools.square(5))
import day18_mytools as mt
mt.say_hello("用 import mytools as mt")
mt.square(7)

import math
print(math.pi)
print(math.sqrt(25))