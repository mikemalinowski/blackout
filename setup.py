import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='insomnia',
    version='1.0.0',
    author='Mike Malinowski',
    author_email='mike@twisted.space',
    description='A python package making it easy to drop a multi-module package from sys.modules',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mikemalinowski/insomnia',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
