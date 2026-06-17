from setuptools import setup

setup(
    name="networksecurity",
    version="0.0.1",
    packages=["networksecurity"],   # explicitly tell which package
    install_requires=[
        "python-dotenv",
        "pandas",
        "numpy",
        "pymongo",
        "certifi",
    ],
)