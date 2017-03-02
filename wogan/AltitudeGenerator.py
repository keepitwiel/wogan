from constants import *
import math
import numpy

START_AMPLITUDE = 100.0
MAX_POWER_SCALE = 10

class AltitudeGenerator(object):

    def generate(self, dimensions, layers):
        resolution_power_scale = min([n for n in range(0, 2**MAX_POWER_SCALE) if 2**n >= max(dimensions)])
        unsampled_array = numpy.random.normal(0.0, START_AMPLITUDE, (2, 2))

        for n in range(resolution_power_scale + 1):
            unsampled_array = self.generate_brownian_array(unsampled_array)

        result = numpy.array(self.sample(unsampled_array, dimensions), dtype=DEFAULT_NUMPY_DATA_TYPE)

        return result

    def generate_brownian_array(self, input_array):
        x, y = input_array.shape[0], input_array.shape[1]
        xx, yy = x*2-1, y*2-1

        output_array = numpy.zeros((xx, yy))

        # copy values
        for i in range(x):
            for j in range(y):
                output_array[i*2][j*2] = input_array[i][j]

        for i in range(1, xx, 2):
            for j in range(y+1):
                output_array[i][j] = (output_array[i+1][j] + output_array[i-1][j]) / 2.0 + numpy.random.normal(0.0, START_AMPLITUDE / x)

        for i in range(x+1):
            for j in range(1, yy, 2):
                output_array[i][j] = (output_array[i][j+1] + output_array[i][j-1]) / 2.0 + numpy.random.normal(0.0, START_AMPLITUDE / x)

        for i in range(1, xx, 2):
            for j in range(1, yy, 2):
                output_array[i][j] = (output_array[i+1][j+1] + output_array[i+1][j-1] + output_array[i-1][j-1] +  output_array[i-1][j+1]) / 4.0 + numpy.random.normal(0.0, START_AMPLITUDE / math.sqrt(x))

        return output_array

    def sample(self, unsampled_array, dimensions):
        result = unsampled_array[:dimensions[0], :dimensions[1]]
        max = numpy.amax(result)
        min = numpy.amin(result)
        result *= 255.0 / (max - min)
        return result
