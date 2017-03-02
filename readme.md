WOGAN - A 2D world generator and handler
===
This software randomly generates static 2D worlds with multiple numerical layers  of spatial data (altitude, precipitation, biomass etc.) and allows loading, saving and data access to these worlds.

Parameters can be tweaked to change generation outcome.

Written in Python 2.7. Developed and tested on Lubuntu 16.04 & macOS 10.12.3.

This readme is a bit out of date, so some bits might not work as advertised.

Features
---
- Create a world
- Save a world to file
- Load a world from file
- Access a specific tile's attributes
- Add layers

Dependencies
---
- numpy (1.11) (install using `sudo pip install python-numpy` or using virtualenv)

Installation (Linux/Mac)
---
- clone into a folder of your choosing
- in the command line, run `python setup.py install`

Quickly generate a world in Python interpreter:
---
  - Open a terminal
  - type `python` and hit `Enter`
  - in the Python interpreter, execute the following:
```
>>> import wogan.World as wogan
>>> world = wogan.World()
```

This generates a world with the default height and width (100x100). Calling `wogan.World((x, y))` will generate a world with dimensions `(x, y)`.

```
>>> x = world.get_values(10, 10)
```
  - This wil get the world's values at coordinate (10, 10)
  - A typical result would look like this:
```
>>> x
{'altitude': 12.14342, 'sea_depth': 0}
```

You can even add your own layer, which are 32-bit float by default:
```
>>> world.set_values(10, 10, {'unicorns': 42})
```

```
>>> world.get_values(10, 10)
{'altitude': 12.14342, 'sea_depth': 0, 'unicorns': 42.0}
```

Concepts
---
WOGAN takes generating, loading, saving and accessing worlds out of your hands, so you can focus on building your game. At the risk of becoming too generic, it allows you to easily add and modify layers to your world.

WOGAN's approach is to store data in multiple NumPy arrays, and return a dictionary when requesting a tile at a specific coordinate, thereby combining data from different arrays.

The advantage with using NumPy is:
- It's fast
- It allows large arrays
- It allows explicit data types, for example single byte integers, thereby saving space
- It allows quick mathematical calculations
- It's reusable

WOGAN runs individual generators for each array, or _layer_. Currently, there are two layers being generated: an altitude map and a sea depth map. Each generator can use previously generated layers as input, as is the case with sea depth (simply put, `sea_depth = max(0, sea_level - altitude)` - if the land is above sea level, sea depth is zero - otherwise take the difference).

Additional layers and their generators can be easily added (see below).

Todo
---
- Update readme.md
- Add more layers
- Add status during generation/saving/loading
- Add logging
- Allow custom filename
- Allow custom parameters
- Allow base and aggregated values (i.e. biomass = mass of all species on a tile)
