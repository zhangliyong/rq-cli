rq-cli
======

A RQ CLI tool with ``empty``, ``requeue`` and ``info`` commands.

.. image:: https://pypip.in/download/pyfuncrun/badge.svg
    :target: https://pypi.python.org/pypi/pyfuncrun/
    :alt: Downloads

Install
-------
.. code-block:: bash

    $ pip install rq-cli

Usage
-----
.. code-block:: bash

    $ rq --help
    Usage: rq [OPTIONS] COMMAND [ARGS]...

    Options:
      -u, --url TEXT  URL describing Redis connection details.
      --help          Show this message and exit.

    Commands:
      empty    [QUEUES]: queues to empty, default: failed...
      info     RQ command-line monitor.
      requeue  Requeue all failed jobs in failed queue
