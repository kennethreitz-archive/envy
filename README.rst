Pyenv: Python Environment Manager
=================================

Current status:

- virtualenv: containerization
- pip: installs dependencies

Future:

- python-build: bootstraps pythons
- pyenv: defines dependencies, installs dependencies with pip, bootstraps virtualenvs with new pythons, generates requirements.txt (like a lockfile), allows cleaning/restarts of virtualenvs

Purpose
-------

- Standarization. Virtualenvs always in ``.venv`` (or similar), ``requirements.txt`` for dependencies. Establish a way to define which version of Python is required for an application.
- ``requirements.txt`` generation.
- Standardized virtualenv locations remove alot of boilerplate documentation.
- Add another version of Python. Not a big deal.
- Rebuild virtualenvs all the time. Not a big deal.

Possible Usage
--------------

``pyenv install``: Recursively finds `Envfile`, and bootstraps virtualenv in ``.venv`` relative to that. If Python defined isn't available, uses `python-build` to provide that as well. Defined python defaults to simply ``python``.

``pyenv init``: Activates the virtualenv. Useful shortcut.

``pyenv freeze``: Generates ``requirements.txt``, based on ``Envfile``.

``pyenv clean``: Removes dependency cruft from a virtualenv.

``pyenv clean --hard``: Rebuilds the virtualenv from scratch.



Example Envfile
---------------

Name to be determined. Yaml? package.cfg?::

    # stuff
    python: pypy-1.6
    module: requests >= 0.9
    module: clint
    github-module: kennethreitz/requests ref

``pyenv freeze`` would result in the following ``requirements.txt``::

    # Python: pypy-1.6

    # From module: requests >= 0.9
    certifi==0.0.6
    requests==0.9.1

    # From module: clint
    clint==0.3.1





