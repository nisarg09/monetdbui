from setuptools import setup, find_packages

setup(name='mdvisual-2018',
    version='1.0.0',
    license='LGPL',
    description='MonetDB Database Tool',
    packages=['src','src/lib'],
    long_description=open('README.md').read(),
    zip_safe=False,
    setup_requires=['pymonetdb==1.1.1','PyQt5==5.11.3','PyQt5-sip==4.19.13'],)
