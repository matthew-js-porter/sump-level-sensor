import setuptools
setuptools.setup(
    name='sump-level-sensor',
    version='1.0',
    description='A tool that will report if the water level in the sump is past a certain level using a float sensor',
    author='Matt Porter',
    author_email="matthew.js.porter@gmail.com",
    setup_requires=['wheel', 'setuptools-lint', 'pytest-runner'],
    install_requires=['gpiozero', 'boto3'],
    tests_require=['pytest', 'pytest-cov', 'coverage'],
    packages=setuptools.find_packages(),
    test_suite='tests',
    entry_points={
        "console_scripts": [
            "sump = sump.sump:main",
            "mocksump = sump.sump:mockmain"
        ]
    }
)
