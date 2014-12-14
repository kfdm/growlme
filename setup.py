from setuptools import setup

setup(
    name='growlme',
    version='0.2',
    description='Growl when a comand is finished',
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
