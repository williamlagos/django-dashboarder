import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-dashboarder',
    version='0.1.0',
    packages=['dashboarder'],
    include_package_data=True,
    license='LGPLv3 License',
    description='A Django app to create fancy admin interface.',
    long_description=README,
    url='http://www.efforia.io/opensource/',
    author='William Oliveira de Lagos',
    author_email='ola@efforia.io',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
