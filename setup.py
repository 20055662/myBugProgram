from setuptools import setup, find_packages

setup(
    name="example",  # Replace with your actual package name
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List your dependencies here
        # For example: "requests>=2.25.1",
    ],
    python_requires=">=3.6",
    description="Collab project for week 8 ",
    author="Luke Fyfe",
    author_email="your.email@example.com",
)