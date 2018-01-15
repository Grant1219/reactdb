# reactdb

A simple python webapp that allows searching through reaction images
that have been tagged with metadata. I used this to learn how to use
the Sphinx search engine server.

This is a standard Pyramid framework application that can be setup as follows:

```
create a python virtualenv
cd <directory containing this file>
$venv/bin/python setup.py develop
$venv/bin/populate_reactdb development.ini
$venv/bin/pserve development.ini
```
