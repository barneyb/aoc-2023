from setuptools import setup, find_packages

setup(
    name="barneyb-aoc-2023",
    version="0.1",
    description="Barney Boisvert's 2023 solutions for https://adventofcode.com/",
    url="https://github.com/barneyb/aoc-2023/",
    author="Barney Boisvert",
    author_email="bboisvert@gmail.com",
    # long_description=open("README.md").read(),
    # long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 2.0.1",
    ],
    packages=find_packages(),
    # entry_points={
    #     "adventofcode.user": ["myusername = mypackage:mysolve"],
    # },
)
