TagField
====================

Renders an input field that is suitable for creating multiple tags. This field is designed to replace the default form field used for many-to-many relationships.
The appearance of this field is controlled by these CSS classes:

- ``.tag-styles``
- ``.tag-input``
- ``.tag-editor``
- ``.tag-close``
- ``.close-icon``

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
    
    # forms.py 
    from fancy_feast.forms.fields import TagField
    
    # Assuming this model exists:
    # class Tag(models.Model):
    #     name = models.CharField(max_length=254)
    #     
    #     def __str__(self):
    #         return self.name
    #
    # class ExampleModel(models.Model):
    #     title = models.CharField(max_length=254)
    #     tags = models.ManyToManyField(Tag, blank=True)
    #     ...
    #
    
    class ExampleForm(forms.ModelForm):
        tags = TagField(model=Tag, field='name')
        
        class Meta:
            model = ExampleModel
            fields = ('title', 'tags',)
        
        def save(self):
            obj = super(ExampleForm, self).save(commit=False)
            obj.save()
            [obj.tags.add(t) for t in self.cleaned_data.get('tags')]
            self.save_m2m()
            return obj
            
*Be sure to include* ``{% if form.media %} {{ form.media.css }} {% endif %}`` *in your template.*

.. image:: https://cloud.githubusercontent.com/assets/10538978/17461055/b8ad4a16-5c3b-11e6-95aa-b9973805dd77.gif


