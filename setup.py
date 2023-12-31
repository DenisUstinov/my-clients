from setuptools import setup, find_packages

setup(
    name='my_clients',
    version='0.1.0',
    author='ChatGPT and Denis Ustinov',
    author_email='revers-06-checkup@icloud.com',
    description='A Python package for working with APIs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DenisUstinov/my-clients',
    license='MIT',
    packages=find_packages(),
    install_requires=['websockets', 'backoff', 'aiohttp'],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
