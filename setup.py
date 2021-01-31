from setuptools import find_packages, setup

setup(
    name="copycheck",
    packages=find_packages(exclude=["tests"]),
    version="0.5.1",
    description="Check for duplicate word series between generated text and a dataset",
    author="Jakob Anderson",
    license="MIT",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1", "numpy"],
    test_suite="tests",
)
