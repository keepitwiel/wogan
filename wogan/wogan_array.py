import numpy

class wogan_array(object):

    def __init__(self, partition_dimensions, partition_size, dtype):
        self.partition_size = partition_size
        self.partitions = [[numpy.zeros(partition_size, partition_size) for x in partition_dimensions.x] for y in partition_dimensions.y]

    def get_value(self, x, y):
        pass
