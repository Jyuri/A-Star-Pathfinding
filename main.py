from random import random, randrange
from time import sleep
from perlin import PerlinNoiseFactory
from more import visualizeNoise, mapCollapse, mapCleaner

size = 80
res = 15
frames = 20
frameres = 5
space_range = size // res
frame_range = frames // frameres

pnf = PerlinNoiseFactory(2,
                         octaves=4,
                         tile=(space_range, space_range, frame_range))

newArray = []
for x in range(size):
    newArray.append([])
    for y in range(size):
        n = pnf(x / res, y / res)
        newArray[x].append(n + 0.5)

newArray = mapCollapse(newArray)
visualizeNoise(newArray, size, size)