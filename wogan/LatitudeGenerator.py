from constants import *
import numpy

class LatitudeGenerator(object):

    def __init__(self):
        self.max_latitude_degrees = 60
        self.min_latitude_degrees = -60

    def generate(self, dimensions, layers):
        result = numpy.zeros(dimensions, dtype=DEFAULT_NUMPY_DATA_TYPE)

        width, height = dimensions

        for x in range(width):
            for y in range(height):
                result[x][y] = 1.0 * y / height * (self.max_latitude_degrees - self.min_latitude_degrees)

        return result
