from setuptools import setup, find_packages
from io import open
from os import path

import pathlib

# credits to Oyetoke Tobi Emmanuel for providing the template for this file
# This is the directory containing this path
HERE = pathlib.Path(__file__).parent

# Read in the readme file
README = (HERE / "README.md").read_text()

# this will automatically captured required modules for install_requires in requirements.txt
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]
setup(
    name='cbdcsim',
    description='CBCD-sim is an open source, easy-to-use, agent-based, simulator of artificial monetary transactions',
    version='0.1a',
    packages=find_packages(),  # list of all packages
    install_requires=['joblib', 'click', 'decorator', 'numpy', 'pandas', 'python-dateutil',
                      'pytz', 'scipy', 'threadpoolctl', 'xlrd'],
    python_requires='>=3.6',
    entry_points='''
    [console_scripts]
    cbdcsim=cbdcsim.__main__:main
    ''',
    author="Joeri Schasfoort",
    keyword="cbdc, central banking, simulation",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/blackrhinoabm/CBDC-sim',
    download_url='https://github.com/blackrhinoabm//CBDC-simarchive/1.0.0.tar.gz',
    author_email='joeri.schasfoort@uct.ac.za',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)
