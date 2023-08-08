"""Setup for pymagsac."""
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

try:
    from skbuild import setup
except ImportError:
    print("Please update pip to pip 10 or greater, or a manually install the PEP 518 requirements in pyproject.toml", file=sys.stderr)
    raise

cmake_args = []
debug = False
cfg = 'Debug' if debug else 'Release'
cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
cmake_args += ['-DCREATE_SAMPLE_PROJECT=OFF']  # <-- Disable the sample project
		
setup(
    name='pymagsac-testing',
    version='0.3.0',
    author='Daniel Barath, Dmytro Mishkin',
    author_email='barath.daniel@sztaki.hu',
    description='MAGSAC and MAGSAC++',
    long_description='Robust estimator for H, F and E estimation.',
    packages=find_packages('src'),
    package_dir={'':'src'},
    cmake_args=cmake_args,
    cmake_install_dir="src/pymagsac",
    cmake_install_target='install',
    #test_suite='tests',
    zip_safe=False,
    install_requires="numpy",
)
