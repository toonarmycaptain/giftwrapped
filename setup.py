import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="giftwrapped-toonarmycaptain",
    version="0.0.1",
    author="David Antonini",
    author_email="toonarmycaptain@hotmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toonarmycaptain/giftwrapped",
    project_urls={
        "Bug Tracker": "https://github.com/toonarmycaptain/giftwrapped",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
