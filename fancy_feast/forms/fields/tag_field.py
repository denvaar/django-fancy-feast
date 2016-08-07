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

