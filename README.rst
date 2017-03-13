jinja2-render
=============

Load variables from a YAML-formatted file and render a jinja2 template to
the standard output.

Installation
------------

.. code-block:: bash
    ./setup.py install

Usage
-----

.. code-block:: bash
    jinja2-render <template_file> <data_file>

Example
-------

Template file ``template.j2``:

.. code-block:: json
    {
        "user": {
            "firstName": "{{ first_name }}",
            "lastName": "{{ last_name }}"
            "
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
            "
        }
    }
