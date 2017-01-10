==================
django-fancy-feast
==================

A collection of additional form fields for Django.

- `DataModelChoiceField <docs/DataModelChoiceField.rst>`_
- `GroupedModelChoiceField <docs/GroupedModelChoiceField.rst>`_
- `GroupedModelMultiChoiceField <docs/GroupedModelMultiChoiceField.rst>`_
- `TagField <docs/TagField.rst>`_

Requirements
------------
- python3
- django 1.8 or higher

Quick Start
-----------

1. Run ``pip install django-fancy-feast``

2. Add 'fancy_feast' to your INSTALLED_APPS setting::

    INSTALLED_APPS = [
        ...

        'fancy_feast',
    ]
