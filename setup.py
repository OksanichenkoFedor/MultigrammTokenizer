from setuptools import setup, find_packages

setup(
    name='mult-tokenizer',
    version='0.1.0',
    url='https://github.com/OksanichenkoFedor/MultigrammTokenizer',
    packages=find_packages(),
    author='Oksanichenko Fedor',
    author_email="okssolotheodor@gmail.com",
    description='Multigramm Tokenization package',
    install_requires=[
        "numpy >= 1.21.5",
        "tqdm >= 4.64.0"
    ],
    license='MIT'
)