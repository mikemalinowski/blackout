import setuptools

try:
    with open('README.md', 'r') as fh:
        long_description = fh.read()
except:
    long_description = ''

setuptools.setup(
    name='blackout',
    version='1.0.2',
    author='Mike Malinowski',
    author_email='mike@twisted.space',
    description='A python package making it easy to drop a multi-module package from sys.modules',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mikemalinowski/blackout',
    packages=setuptools.find_packages(),
    entry_points="""
        [console_scripts]
        blackout = blackout:blackout
    """,
    py_modules=["blackout"],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
