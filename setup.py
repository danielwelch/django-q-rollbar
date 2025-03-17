import os
from setuptools import setup, find_packages

try:
    import pypandoc
    README = pypandoc.convert('README.md', 'rst')
except ImportError:
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
        README = readme.read()


setup(
    name='django-q-rollbar',
    version='0.2.0',
    author='Daniel Welch',
    author_email='dwelch2102@gmail.com',
    keywords='django distributed task queue worker scheduler cron redis disque ironmq sqs orm mongodb multiprocessing rollbar',
    packages=find_packages(include=['django-q-rollbar'], exclude=['.venv', 'dist','build', 'django-q-rollbar*egg-info']),
    install_requires=['rollbar>=1.0.0'],
    url='https://django-q.readthedocs.org',
    license='MIT',
    description='A Rollbar support plugin for Django Q',
    long_description=README,
)
