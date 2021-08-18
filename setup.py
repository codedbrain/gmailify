import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gmailify",
    version="1.0.0",
    author="Santosh Bhandari",
    description = "This tool validates if gmail addresses and corporate emails with google mail servers are valid without being authenticated. The default thread is 10 to avoid being rate limited.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codedbrain/gmailify",
    project_urls={
        "Bug Tracker": "https://github.com/codedbrain/gmailify/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'requests',
        'argparse',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
