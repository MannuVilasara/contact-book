# NOTE: Making it a python package for cli purpose

from setuptools import setup, find_packages

setup(
    name="contact",
    author="MannuVilasra",
    author_email="mannuvilasara@gmail.com",
    description="A simple cli-based contact book",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["colorama", "inquirer", "tabulate"],
    entry_points="""
        [console_scripts]
        contact=contact.main:main
    """,
)
