"""Package setup."""
from setuptools import find_packages, setup

name = 'asante_mobile_wallet'
version = "0.0.0.1"

setup(
    name=name,
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    description="Digital Mobile Wallet",
    # long_description=open('README.rst').read(),
    url="",
    author="ASANTE SYSTEMS",
    author_email="jimmy@asantesytems.com",
    license="Proprietary",
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Asante Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'gunicorn',
        'django-filter>=2.4.0',
        'djangorestframework>=3.8.2',
        'Markdown',
        'django-cors-headers>=3.7.0',
        'dj-database-url>=0.5.0',
        'django-ses',
        'django>=3.1.0',
        'psycopg2',
        'celery',
        'djangorestframework-simplejwt==4.7.2',
        'raven',
        'django-sentry-400-middleware',
    ],
    include_package_data=True
)
