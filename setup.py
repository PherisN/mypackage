from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<pherisn>/<mypackage>',
    author='<Pheris Namakwa>',
    author_email='<pherisn@gmail.com>'
)