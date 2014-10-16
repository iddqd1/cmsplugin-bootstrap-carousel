from setuptools import setup
import os

setup(
    name = "cmsplugin-bootstrap-carousel",
    packages = ['cmsplugin_bootstrap_carousel','cmsplugin_bootstrap_carousel.migrations'],

    package_data = {
        '': [
            'templates/cmsplugin_bootstrap_carousel/*.html',
        ]
    },

    version = "0.15",
    description = "Bootstrap carousel plugin for django-cms 2.2",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author = "Antoine Nguyen",
    author_email = "tonio@ngyn.org",
    url = "http://bitbucket.org/iddqd1/cmsplugin-bootstrap-carousel",
    license = "BSD",
    keywords = ["django", "django-cms", "bootstrap", "carousel"],
    classifiers = [
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django"
        ],
    include_package_data = True,
    zip_safe = True,
    dependency_links = ['https://github.com/smacker/django-filebrowser-no-grappelli#egg=django-filebrowser'],
    install_requires = ['Django-CMS>=2.2'],
    )
