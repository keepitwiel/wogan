from constants import *
import numpy

class DefaultGenerator(object):
    def generate(self, dimensions, layers):
        return numpy.zeros(dimensions, dtype=DEFAULT_NUMPY_DATA_TYPE)
