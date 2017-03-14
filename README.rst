jinja2-render
=============

Load variables from YAML-formatted files and perform Jinja2 template
rendering to the standard output.

Installation
------------

.. code-block:: bash

   ./setup.py install

Usage
-----

.. code-block:: bash

    jinja2-render <template_name> <data_file1> [<data_file2> ...]

Example
-------

Template file ``template.j2``:

.. code-block:: json

    {
        "user": {
            "firstName": "{{ first_name }}",
            "lastName": "{{ last_name }}"
        }
    }

Variable file ``var.yml``:

.. code-block:: yaml

    ---
    first_name: Raoul
    last_name: Duke

Rendering the template:

.. code-block:: bash

    jinja2-render template.j2 var.yml

Result:

.. code-block:: json

    {
        "user": {
            "firstName": "Raoul",
            "lastName": "Duke"
        }
    }

Setting template path
---------------------

The path to Jinja2 template files can be set using the
``-t``/``--template-path`` option:


.. code-block:: bash

    jinja2-render -t /path/to/templates/ template.j2 var.yml

If omitted, it assumed to be the current working directory.

Loading extra Jinja2 filters
----------------------------

Extra filters ``/path/to/extra/filters.py``:

.. code-block:: python

    def foo(...):
        return ...

    def bar(...):
        return ...

    FILTERS = {
        'foo': foo,
        'bar': bar,
    }

Rendering with extra filters:

.. code-block:: bash

    jinja2-render -p /path/to/extra -f filters template.j2 var.yml
