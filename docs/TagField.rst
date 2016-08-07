TagField
====================

Renders an input field that is suitable for creating multiple tags.

Field Options
-------------

+-------------------------+--------------------------------------------------------------------------+
| Required Parameters     | Description                                                              |
+=========================+==========================================================================+
|``model``                | The model to use.                                                        |
+-------------------------+--------------------------------------------------------------------------+
|``field``                | Name of the model's field to use.                                        |
+-------------------------+--------------------------------------------------------------------------+

+-------------------------+-------------------------------------------------------------------------------------------------+
| Optional Parameters     | Description                                                                                     |
+=========================+=================================================================================================+
|``split_character``      | Character to use as a delimeter for separating tags internally. ``'|'`` is the default.         |
+-------------------------+-------------------------------------------------------------------------------------------------+


Example Usage
-------------

.. code-block:: python

    # models.py
    class Tag(models.Model):
        name = models.CharField(max_length=254)

        def __str__(self):
            return self.name

.. code-block:: python
    
    # forms.py 
    from fancy_feast.forms.fields import TagField
    
    class ExampleForm(forms.Form):
        tags = TagField(model=Tag, field='name')

.. image:: https://cloud.githubusercontent.com/assets/10538978/17461055/b8ad4a16-5c3b-11e6-95aa-b9973805dd77.gif


