from setuptools import setup

setup(
    name='pytesterv3',
    version='0.1',
    description='description',
    long_description='description',
    author='Kamil Florek',
    author_email='kamiflorek7@gmail.com',
    url='',
    py_modules=['src'],
    entry_points = {
    'console_scripts':[
        'app = src.app:tester'
        ]
    },
    zip_safe=True,
    license='BSD-3',
    scripts=['bin/build/app']
)