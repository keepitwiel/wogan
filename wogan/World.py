from constants import *
import Generator

class World(object):

    def __init__(self, dimensions=(100, 100)):
        self.dimensions = dimensions
        self.layers = {}
        self.generator = Generator.Generator()

        for layer_name in self.generator.generation_order:
            self.add_layer(layer_name)

    def add_layer(self, layer_name, contents=None):
        if contents == None:
            self.layers[layer_name] = self.generator.generate(layer_name, self.dimensions, self.layers)
        else:
            self.layers[layer_name] = contents

    def get_value(self, x, y, layer_name):
        result = 0

        if layer_name in self.layers and self.within_bounds(x, y):
            result = self.layers[layer_name][x][y]

        return result

    def get_values(self, x, y, layer_names=None):
        if layer_names == None:
            layer_names = self.layers.keys()

        return {layer_name: self.get_value(x, y, layer_name) for layer_name in layer_names}

    def add_values(self, x, y, args):
        if self.within_bounds(x, y):
            for layer_name in args:
                if not(self.layers.has_key(layer_name)):
                    self.add_layer(layer_name)

                self.layers[layer_name][x][y] += args[layer_name]

    def set_values(self, x, y, args):
        if self.within_bounds(x, y):
            for layer_name in args:
                if not(self.layers.has_key(layer_name)):
                    self.add_layer(layer_name)

                self.layers[layer_name][x][y] = args[layer_name]

    def within_bounds(self, x, y):
        result = False
        if x >= 0 and x < self.dimensions[0] and y >= 0 and y < self.dimensions[1]:
            result = True

        return result
