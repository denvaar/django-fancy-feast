from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class TagInput(TextInput):
    template_name = 'fancy_feast/widgets/_tag_input.html'

    class Media:
        css = {
            'all': ('fancy_feast/css/styles.css',)
        }

    def __init__(self, split_character, *args, **kwargs):
        self.split_character = split_character
        super(TagInput, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        if 'class' in attrs:
            attrs['class'] += ' tag-input'
        else:
            attrs['class'] = 'tag-input '
        context = { 
            'input': super(TagInput, self).render(name, value, attrs),
            'id': attrs['id'],
            'placeholder': 'Use enter key to create tags',
            'split_character': self.split_character
        }   
        return mark_safe(render_to_string(self.template_name, context))

    def value_from_datadict(self, data, files, name):
        return super(TagInput, self).value_from_datadict(data, files, name)

