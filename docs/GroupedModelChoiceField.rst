GroupedModelChoiceField
=======================

Much like Django's ``ModelChoiceField``, but renders an HTML select box where the choices are
grouped together using optgroups.


Field Options
-------------

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Required Parameters     | Description                                                                                                                                   |
+=========================+===============================================================================================================================================+
|``queryset``             | A QuerySet of model objects from which the choices for the field will be derived, and which will be used to validate the user’s selection.    |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
|``group_by_field``      | The name of a field on the model to use as an optgroup                                                                      |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Optional Parameters     | Description                                                                                                                                   |
+=========================+===============================================================================================================================================+
|``group_by_label``       | A function that will return a label for each optgroup. |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

You may also use the traditional args and kwargs from Django's ``ModelChoiceField``.


Example Usage
-------------

.. code-block:: python
    
    # forms.py 
    from fancy_feast.forms.fields import GroupedModelChoiceField
    
    # Assuming this model:
    # class Position(models.Model):
    #     name = models.CharField(max_length=254)
    #     employer = models.CharField(max_length=254)
    # 
    #     def __str__(self):
    #         return self.name
    
    class ExampleForm(forms.Form):
        positions = GroupedModelChoiceField(queryset=Position.objects.all(),
                                            group_by_field='employer')

        ...

The result would be a select field like this:

.. code-block:: html
    <select id="id_positions" name="positions">
      <optgroup label="Employer 1">
        <option>Software Developer</option>
      </optgroup> 
      <optgroup label="Employer 2">
        <option>Dog Show Host</option>
        <option>Scuba Instructor</option>
      </optgroup>
    </select>
