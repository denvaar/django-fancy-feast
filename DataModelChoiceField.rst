DataModelChoiceField
====================

Same as Django's ``ModelChoiceField``, but renders additional HTML5 ``data-`` attributes
on the ``<option>`` tags. Allows for mapping of additional model fields as the ``data-``
attributes.

Renders an HTML select field with ``data-`` attributes. Use the data_attributes

Field Options
-------------

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Required Parameters     | Description                                                                                                                                   |
+=========================+===============================================================================================================================================+
|``queryset``             | A QuerySet of model objects from which the choices for the field will be derived, and which will be used to validate the user’s selection.    |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
|``data_attributes``      | A dictionary mapping from data attribute name to the model's field name.                                                                      |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+


Example Usage
-------------

.. code-block:: python

    # models.py
    class Color(models.Model):
        name = models.CharField(max_length=254)
        value = models.CharField(max_length=254)
        opacity = models.DecimalField()

        def __str__(self):
            return self.name

.. code-block:: python
    
    # forms.py 
    from fancy_feast.forms.fields import DataModelChoiceField
    
    class ExampleForm(forms.Form):
        icon_color = DataModelChoiceField(queryset=Color.objects.all(),
                                          data_attributes={'color':'value',
                                                           'opacity': 'opacity'})

The result would be a select field like this:

.. code-block:: html
    
    <select id="id_icon_color" name="icon_color">
        <option value="" selected="selected">---------</option>
        <option data-color="#53DF83" data-opacity="0.5" value="1">Happy Green</option>
        <option data-color="#47D2E9" data-opacity="0.9" value="2">Flyby</option>
        <option data-color="#EEEEEE" data-opacity="1.0" value="3">Concrete</option>
        <option data-color="#3F3F3F" data-opacity="0.1" value="4">The Dark Side</option>
    </select>
