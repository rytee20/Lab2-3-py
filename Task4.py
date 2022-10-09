import os
import random

os.mkdir("example")
for i in range(0,100):
    file = open("example/examplefile"+str(i), "w")
    size = 1024*random.randint(1, 100)
    file.write(" " * size)
