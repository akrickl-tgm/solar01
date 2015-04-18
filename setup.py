from distutils.core import setup

setup(
    # Application name:
    name="Solarsystem",

    # Version number (initial):
    version="1.1.3",

    # Application author details:
    author="Daniel Herczeg, Astrid Krickl",
    author_email="dherczeg@student.tgm.ac.at",

    # Packages
    packages=["solarsystem"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://www.whitebrownie.net",

    #
    # license="LICENSE.txt",
    description="Solarsystem Gruppenarbeit.",

    long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "pillow", "pyopengl", "pip", "pygments", "jinja2", "1337"
    ],
)