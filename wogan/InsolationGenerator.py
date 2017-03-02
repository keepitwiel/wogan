from constants import *
import numpy
import math

class InsolationGenerator(object):

    MAX_LATITUDE_DEGREES = 60;
    MIN_LATITUDE_DEGREES = -60;

    def generate(self, dimensions, layers):
        result = numpy.zeros(dimensions, dtype=DEFAULT_NUMPY_DATA_TYPE)

        width, height = dimensions

        for x in range(width):
            for y in range(height):
                result[x][y] = 1000.0 #* math.cos(layers['latitude'][x][y])

        return result
