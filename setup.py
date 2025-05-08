from setuptools import setup, find_packages
import os

# Read long description from README.md
long_description = ""
if os.path.exists("README.md"):
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="RepMat",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "sympy",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/george-elliott-git/RepMat",
    project_urls={
        "Documentation": "https://yourdocs.com",  # Replace with actual URL
    },
    author="George Elliott",
    author_email="georgeelliott.ge@proton.me",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
