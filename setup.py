from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-username-email',

    version='1.0.2a1',

    description='Custom Django User model that makes email the USERNAME_FIELD.',
    long_description=long_description,

    url='https://github.com/thomasmeagher/django-username-email/',

    author='Tom Meagher',
    author_email='tom@meagher.co',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',

        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Operating System :: OS Independent',
    ],
    keywords='user email username',

    packages=find_packages(),
)
