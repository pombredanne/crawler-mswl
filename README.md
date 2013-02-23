crawler-mswl: Python web crawler
=================================

Introduction
=============

This is a Python crawler project to retrieve all links in `a` tags defined in URL and access every `href` property for each link as defined in input parameter.

Ricardo García Fernández developed this project for ``Developing Tools`` Subject coursed in [Master on Libre Software (Master Universitario en Software libre](http://master.libresoft.es/) at [Universidad Rey juan Carlos](http://www.urjc.es/).

Requirements
=============

* Java JDK 1.6.0_22
* Python 2.7.2

License
========

This project has ``GNU GENERAL PUBLIC LICENSE version 3`` see complete definition in [COPYING](COPYING) file.

Install
========

Read install instructions in [INSTALL](INSTALL) file.

* Install from PYPI.
* Install from Source.

Command
========

How to use the application.

This application run by command `ricardo-crawler` after instalation.

To use this application without installing it you have to type:

```shell
python ricardo-crawler.py -n 1 http://www.google.es
```

Arguments
----------

Two arguments to run the application:
```shell
-n [Number of levels to inspect]: number of depth level to retrieve 
  links. If no argument is passed, by default is assigned to *1*.
[URL]: URL to inspect for each level defined.
```

Has a help command to define correctly these arguments.
```shell
python ricardo_crawler.py --help
```

Help Console Output:

```shell
usage: ricardo_crawler.py [-h] [-n NUMBER_OF_LEVELS] url

Let's crawl a web

positional arguments:
  url                   target URL

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER_OF_LEVELS, --number-of-levels NUMBER_OF_LEVELS
                        how depth the crawl will go.
```

Test
-----

There are tests developer for each controller behaviour:

```shell
test/
├── controllers
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── TestHttpLinksCollector.py
│   ├── TestHttpLinksCollector.pyc
│   ├── TestUrlContentRetrieve.py
│   └── TestUrlContentRetrieve.pyc
├── __init__.py
└── __init__.pyc
```

Issues management
==================

Issue management its done with Redmine project tracker in:

  http://code.sidelab.es/projects/ricardogarcia2012/issues

License
========

<a href="http://creativecommons.org/licenses/by/3.0/" rel="Creative Commons Attribution 3.0">![Foo](http://i.creativecommons.org/l/by/3.0/88x31.png)</a>

This work is licensed under a [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).
