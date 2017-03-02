import numpy

class WorldFileHandler(object):

    def save_world(self, world, filename):

        kwargs = {}
        for layer in world.layers:
            kwargs[layer] = world.layers[layer]

        f = file(filename, 'w+')
        numpy.savez(f, **kwargs)
        f.close()

    def load_world(self, filename):
        result = None

        f = file(filename, 'r')
        contents = numpy.load(f)

        layer_names = contents.files

        if len(layer_names) > 0:
            dimensions = contents[layer_names[0]].shape
            result = World(dimensions)
            for layer_name in layer_names:
                result.add_layer(layer_name, contents[layer_name])
        else:
            print 'Warning: file doesn''t contain any arrays'

        return result
