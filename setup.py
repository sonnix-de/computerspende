
from setuptools import setup
setup(
    name='InstallationHelferlein',
    version='1.0',
    description='InstallationHelferlein der Computerspende Regensburg',
    author='computerspende-regensburg',
    author_email='team@computerspende-regensburg.de',
    packages=['json', ],  # same as name
    # external packages as dependencies
    install_requires=['bar', 'consolemenu', ],
    scripts=[
        'scripts/cool',
        'scripts/skype',
    ]
)