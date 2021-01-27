try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupytercheck",
    version="0.0.1dev",
    author="Dirk Colbry",
    author_email="colbrydi@msu.edu",
    description="Answerchecker for student jupyter notebooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=[
        'answercheck',
    ],
)
