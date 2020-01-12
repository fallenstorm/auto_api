import os
import re
from setuptools import setup, find_packages


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('auto_api')

setup(
    name='auto_api',
    version=version,
    install_requires=[
        'djangorestframework',
        'django_filter'
    ],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    python_requires=">=3.6"
)
