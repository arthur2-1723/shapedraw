from setuptools import setup, find_packages

setup(
    name="shapedraw",
    version="0.1",
    packages=find_packages(),
    description="A simple library to draw geometric shapes using ASCII",
    author="Arthur",
    author_email="ederjose.santos@gmail.com",
    url="https://github.com/arthur2-1723/shapedraw",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)