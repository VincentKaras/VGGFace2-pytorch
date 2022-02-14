from setuptools import setup, find_packages

setup(
    name='VGGFace2-pytorch',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/VincentKaras/VGGFace2-pytorch',
    license='MIT',
    author='VincentKaras',
    author_email='vincent.karas@tum.de',
    description='ResNet50 and SENet50 pre-trained on VGGFace2. Forked from https://github.com/cydonia999/VGGFace2-pytorch',
    install_requires=[
        "pandas>=1.4",
        "torch>=1.10",
        "numpy>=1.19.2",
    ]
)
