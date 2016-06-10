'''
Growl when a command is finished.

Original version by Robey Pointer https://github.com/robey
'''


from setuptools import setup

setup(
    name='growlme',
    version='0.2',
    description=__doc__,
    url='https://github.com/kfdm/growlme',
    maintainer='Paul Traylor',
    install_requires=['gntp'],
    license='Apache',
    packages=['growlme'],
    package_data={'growlme': [
        './*.png'
    ]},
    include_package_files=True,
    entry_points={
        'console_scripts': [
            'growlme=growlme:main'
            ]
        }
    )
