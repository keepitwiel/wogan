from constants import *
import numpy

class BiomassGenerator(object):

    def generate(self, dimensions, layers):

        result = numpy.zeros(dimensions, dtype=DEFAULT_NUMPY_DATA_TYPE)

        width, height = dimensions

        for x in range(width):
            for y in range(height):
                result[x][y] = self._biomass_function(layers['sea_depth'][x][y], layers['temperature'][x][y], layers['precipitation'][x][y])

        return result

    def _biomass_function(self, sea_depth, temperature, precipitation):
        result = 0

        if sea_depth >= 0:
            result = temperature * precipitation * 0.01
        else:
            result = max(0, (temperature - 200) * precipitation * 0.1)
        return result
