try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'WOGAN - a 2d layered world generator and handler.',
    'author': 'Giel van de Wiel',
    'url': '',
    'download_url': '',
    'author_email': 'sj@apple.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['wogan'],
    'scripts': [],
    'name': 'wogan'
}

setup(**config)
