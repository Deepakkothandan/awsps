from setuptools import setup

setup(
    name="awsps",
    version='0.1.0',
    install_requires=[
        'configparser;python_version<"3.0"'
    ],
    entry_points='''
        [console_scripts]
        awsps=awsps:main
    ''',
)
