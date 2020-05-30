# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.

setup(
    name='stockiness',  # Required
    version='0.0.1.dev',  # Required

    description='Stock market analysis application',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/StefanNiehaus/StockAnalysis',
    keywords='stocks, stock analysis, stock market',

    packages=find_packages(),  # Required

    python_requires='>=3.5, <3.8',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    install_requires=['kivy', 'alpha-vantage'],  # Optional
)
