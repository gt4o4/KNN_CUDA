import os
import re
from setuptools import setup, find_packages

# Read version without importing the package (which requires torch at import time)
with open(os.path.join('knn_cuda', '__init__.py')) as f:
    _version_match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', f.read())
    assert _version_match, "Could not find __version__ in knn_cuda/__init__.py"
    __version__ = _version_match.group(1)


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='KNN_CUDA',
    version=__version__,
    description='pytorch version knn support cuda.',
    author='Shuaipeng Li',
    author_email='sli@mail.bnu.edu.cn',
    packages=find_packages(),
    package_data={
        'knn_cuda': ["csrc/cuda/knn.cu", "csrc/cuda/knn.cpp"]
    },
    install_requires=required
)
