# setup.py

from setuptools import setup, find_packages

setup(
    name='byteCaptcha',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    author='h3xcolor',
    author_email='oktk0728@gmail.com',
    description='A powerful captcha generation library for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sjskUw/byteCaptcha',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
