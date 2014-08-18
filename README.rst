rq-cli
======

Interface
---------
Create a new CLI friendly ``rq`` command to support::

    Usage: rq [OPTIONS] COMMAND [ARGS]...

    Options:
      -c, --config TEXT    Module containing RQ settings.
      -u, --url TEXT       URL describing Redis connection details.
      --help               Show this message and exit.

    Commands:
      empty    Empty queues, default: empty failed queue
      requeue  Requeue all failed jobs in failed queue


Config
------

* Read config from a config file in ``~/.config/rq``
* Read config file passed by option ``-c config``
* Support pass configs throw command line

Plan
----

Implement ``empty`` and ``requeue`` first, then add ``info`` and ``enqueue``

Use `click <http://click.pocoo.org>`_ to implement.
