from setuptools import setup, find_packages

VERSION = '0.0.8'
DESCRIPTION = 'A basic implementation of some data structures'

def read_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        return file.read()

setup(
    name="DScollection",
    version=VERSION,
    author="Kishan Chauhan",
    author_email="kishanchauhan2006.25@gmail.com",
    description=DESCRIPTION,
    long_description=read_file('README.md') + '\n\n' + read_file('CHANGELOG.txt'),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    keywords='data structures stack linked list',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
