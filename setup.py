import os
from setuptools import find_packages, setup
import leancloud

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#     README = readme.read()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
                    'Django >= 1.8',
                    'requests >= 2.1',
                   ],

setup(
    name='django-leancloud-sms',
    version=leancloud.__version__,
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A simple Django app use leancloud sms api',
    # long_description=README,
    author='jiaxin',
    author_email='edison7500@gmail.com',
    url='https://github.com/edison7500/django-leancloud-sms',
    download_url='https://github.com/edison7500/django-leancloud-sms/archive/v0.2-alpha.tar.gz',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires,
    test_suite = 'testapp',
    zip_safe = False,
)