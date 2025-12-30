from setuptools import setup, find_packages

setup(
    name="PySMan",
    version="0.1.0",
    description="Lightweight Service Manager for Python projects",
    author="BusyChild77",
    author_email="noemail@noemail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": ["pytest", "black", "flake8"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
