try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This is the first I use python',
    'author': 'Hola',
    'url': 'https://github.com/kevinhoa95/skeleton',
    'download_url': 'https://github.com/kevinhoa95/skeleton',
    'author_email': 'kevinhoa95@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'skeleton'
}

setup(**config)