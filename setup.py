from setuptools import setup, find_packages

setup(
    name="RepMat", 
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[ 
        "numpy",
        "sympy",
    ],
    # Optional additional configurations (metadata)
    author="George Elliott",
    description="Representation theory of finite groups in Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6", 
)
