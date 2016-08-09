from django.forms import CharField

from fancy_feast.forms.widgets import TagInput


class TagField(CharField):
    
    def __init__(self, model, field, split_character='|',
                 max_length=None, min_length=None,
                 strip=True, *args, **kwargs):
        self.model = model
        self.field = field
        self.split_character = split_character
        super(TagField, self).__init__(widget=TagInput(
                split_character=split_character, *args, **kwargs))

    def to_python(self, value):
        tags = []
        for item in value.strip(self.split_character).split(
                self.split_character):
            tag, was_created = self.model.objects.get_or_create(
                    **{self.field:item})
            tags.append(tag)
        return tags

    def prepare_value(self, value):
        as_string = ''
        if (hasattr(value, '__iter__') and
                not isinstance(value, six.text_type) and
                not hasattr(value, '_meta')):
            for tag in value:
                as_string += '{}{}'.format(getattr(tag, self.field),
                                           self.split_character)
        return as_string

