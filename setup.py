import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='sass-cli',
    version='0.0.3',
    description='CLI for SASS compliation',
    long_description=readme(),
    url='http://bmcorser.github.com/sass-cli',
    author='bmcorser',
    author_email='bmcorser@gmail.com',
    packages=['sass_cli'],
    install_requires=['sass', 'click'],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    entry_points='''
        [console_scripts]
        sass=sass_cli.main:run
    ''',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only'
    ],
)
