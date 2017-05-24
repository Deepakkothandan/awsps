from setuptools import setup

setup(
    name="awsps",
    version='0.2.0',
    description='AWS Profile Switcher',
    url='https://github.com/Deepakkothandan/awsps.git',
    author='Deepak Kothandan',
    author_email='deepak.kdy@gmail.com',
    license='MIT',
    keywords='aws profile switch',
    install_requires=[
        'configparser;python_version<"3.0"'
    ],
    entry_points='''
        [console_scripts]
        awsps=awsps.awsps:main
    ''',
    packages=['awsps']
)
