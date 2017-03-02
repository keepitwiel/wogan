from constants import *
import numpy

class PrecipitationGenerator(object):

    def generate(self, dimensions, layers):
        result = numpy.zeros(dimensions, dtype=DEFAULT_NUMPY_DATA_TYPE)

        width, height = dimensions

        for x in range(width):
            for y in range(height):
                result[x][y] = max(0, layers['altitude'][x][y])

        return result
