from distutils.core import setup

setup(
    name='emergency',
    version='0.0.1',
    packages=['emergency'],
    url='',
    license='MIT License',
    author='Darwin Monroy',
    author_email='contact@darwinmonroy.com',
    description='Web-based Emergency Management Service',
    entry_points = {
        'console_scripts': [
            'emergency = emergency.cli:main',
        ],
    },
    install_requires=[
        'aiopg',
        'attrdict',
        'chilero>=0.2.2,<0.3',
        'gunicorn',
        'schema-migrations',
        'setuptools',
    ]
)
