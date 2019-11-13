from setuptools import setup, find_packages


NAME = 'simple_http'
DESCRIPTION = ''
AUTHOR = 'shuiruge'
AUTHOR_EMAIL = 'shuiruge@hotmail.com'
URL = 'https://github.com/shuiruge/simple_http'
VERSION = '0.0.1'
with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license='MIT',
    url=URL,
    packages=find_packages(exclude=['dat.*', 'dat']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python :: 3+',
    ],
    zip_safe=False,
)
