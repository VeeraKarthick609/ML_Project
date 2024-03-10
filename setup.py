from typing import List
from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."

def get_requirements() -> List[str]:
    """
    Function that reads requirements.txt and
    returns the list of packages

    Args:
    None

    Returns:
    - List: Required packages list
    """

    packages = []
    try:

        with open("requirements.txt", "r") as file:
            packages = file.readlines()
            packages = [req.replace("\n", "") for req in packages]
    
        if HYPHEN_E_DOT in packages:
            packages.remove(HYPHEN_E_DOT)

        return packages
    
    except Exception as e:
        print(f"Error while running setup.py: {e}")


setup(
    name="mlproject",
    version="0.0.1",
    author="Veera",
    author_email="veerakarthick609@gmail.com",
    packages=find_packages(),
    requires=get_requirements(),
)
