from setuptools import setup, find_packages
from distutils.command.install import install as _install
from distutils.core import setup, Extension

module_cfunc = Extension('mg_tok.libcfuncs',
                       sources = ['mg_tok/cfuncs.c'])

setup(
    name='mult-tokenizer',
    version='0.1.39',
    url='https://github.com/OksanichenkoFedor/MultigrammTokenizer',
    packages=find_packages(include="mg_tok"),
    author='Oksanichenko Fedor',
    author_email="okssolotheodor@gmail.com",
    description='Multigramm Tokenization package',
    long_description='A Python implementation of ngram-tokenization algorithm.',
    install_requires=[
        "numpy >= 1.21.5",
        "tqdm >= 4.64.0"
    ],
    license='MIT'
)