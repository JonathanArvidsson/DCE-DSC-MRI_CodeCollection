from setuptools import setup, find_packages


setup(
        name='src',
        version = '1.0.0', 
        install_requires = ['pytest','numpy','scipy','lmfit','nibabel','mat73'],
        packages = find_packages()
        )
