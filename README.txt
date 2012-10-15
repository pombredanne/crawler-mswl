=================================
crawler-mswl: Python web crawler
=================================

Introduction
=============

This is a Python crawler project to retrieve all links in **a** tags defined in
 URL and access every **href** property for each link as defined in input
  parameter.

Ricardo García Fernández developed this projecto for ``Developing Tools`` 
Subject in Universidad Rey Juan Carlos ``Master en Software Libre``.

Environment
============

Java JDK 1.6.0_22
Python 2.7.2

License
========

This project has ``GNU GENERAL PUBLIC LICENSE version 3`` see complete 
definition in **COPYING** file.

Install
========

Read install instructions in **INSTALL** file. 

Command
========

How to use the application.

This application run by command **ricardo-crawler** after instalation.
To use this application without installing it you have to type:

    * python ricardo-crawler.py -n 1 http://www.google.es

Arguments
----------

Two arguments to run the application::

    * -n [Number of levels to inspect]: number of depth level to retrieve 
      links. If no argument is passed, by default is assigned to *1*.
    * [URL]: URL to inspect for each level defined.

Has a help command to define correctly these arguments.

    * python ricardo_crawler.py --help

Console Output::

    usage: ricardo_crawler.py [-h] [-n NUMBER_OF_LEVELS] url

    Let's crawl a web

    positional arguments:
      url                   target URL

    optional arguments:
      -h, --help            show this help message and exit
      -n NUMBER_OF_LEVELS, --number-of-levels NUMBER_OF_LEVELS
                            how depth the crawl will go.

Issues management
==================

Issue management its done with Redmine project tracker in::

    * http://code.sidelab.es/projects/ricardogarcia2012/issues
    

