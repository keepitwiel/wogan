import AltitudeGenerator
import SeaDepthGenerator
import LatitudeGenerator
import InsolationGenerator
import TemperatureGenerator
import BiomassGenerator
import PrecipitationGenerator
import DefaultGenerator

class Generator(object):

    def __init__(self):
        self.generation_order = ['altitude',
                                 'sea_depth',
                                 'latitude',
                                 'insolation',
                                 'temperature',
                                 'precipitation',
                                 'biomass']

        self.generator_dict = {
            'altitude': AltitudeGenerator.AltitudeGenerator(),
            'sea_depth': SeaDepthGenerator.SeaDepthGenerator(),
            'latitude': LatitudeGenerator.LatitudeGenerator(),
            'insolation': InsolationGenerator.InsolationGenerator(),
            'temperature': TemperatureGenerator.TemperatureGenerator(),
            'precipitation': PrecipitationGenerator.PrecipitationGenerator(),
            'biomass': BiomassGenerator.BiomassGenerator(),
            'default': DefaultGenerator.DefaultGenerator()
        }

    def generate(self, name, dimensions, layers):
        final_name = 'default'
        if name in self.generation_order:
            final_name = name

        return self.generator_dict[final_name].generate(dimensions, layers)
