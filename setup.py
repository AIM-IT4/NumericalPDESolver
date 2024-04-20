import setuptools

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="numerical-pde-solver",  # Replace with your own username
    version="0.1.4",  # Increment this with each release
    author="Amit Kumar Jha",
    author_email="jha.8@alumni.iitj.ac.in",
    description="A small package for solving PDEs using numerical methods",  # Short description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AIM-IT4/numerical-pde-solver",  # Replace with the URL to your repo
    project_urls={
        "Bug Tracker": "https://github.com/AIM-IT4/numerical-pde-solver/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change the license if it's not MIT
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the minimum Python version required
    install_requires=[  # Add any other dependencies your package needs
        "numpy",
        # "pandas",
        # "scipy",
        # ...
    ],
)
