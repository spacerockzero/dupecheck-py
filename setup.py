import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="dupecheck",
    version="0.6.3",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Jakob Anderson",
    author_email="fictionisfiction@gmail.com",
    license="MIT",
    url="https://github.com/spacerockzero/dupecheck",
    description="Check for duplicate word series between generated text and a dataset",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=["tqdm"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1", "numpy"],
    test_suite="tests",
)
