from django.forms import CharField

class TagField(CharField):
    
    def __init__(self, model, max_length=None, min_length=None, strip=True,
                 *args, **kwargs):
        self.max_length = max_length
        self.min_length = min_length
        self.strip = strip
        self.model = model
        super(TagField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        tags = []
        for item in value.strip('|').split('|'):
            tag, was_created = self.model.objects.get_or_create(name=item)
            tags.append(tag)
        return tags

