from django.utils.encoding import force_text
from django.utils.html import format_html 
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.forms.widgets import TextInput, Select
from django.forms.utils import flatatt


class DataModelChoice(Select):

    def __init__(self, data_attribute=None, data_value=None, *args, **kwargs):
        super(DataModelChoice, self).__init__(*args, **kwargs)
        self.data_attribute = data_attribute
        self.data_value = data_value

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<select{}>', flatatt(final_attrs))]
        options = self.render_options([value])
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe('\n'.join(output)) 

    def render_option(self, selected_choices, option_value, option_label, **extra):
        if option_value is None:
            option_value = ''
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        
        data_attrs = ''
        for k,v in extra.items():
            data_attrs += ' data-{}="{}"'.format(k,v)
        return format_html('<option{} value="{}"{}>{}</option>',
                format_html(data_attrs), option_value, selected_html,
                force_text(option_label))
    
    def render_options(self, selected_choices):
        selected_choices = set(force_text(v) for v in selected_choices)
        output = []
        e = [*self.choices]
        for option_value, option_label, data in [*self.choices]:
            if isinstance(option_label, (list, tuple)):
                output.append(format_html('<optgroup label="{}">', force_text(option_value)))
                for option in option_label:
                    output.append(self.render_option(selected_choices, *option))
                output.append('</optgroup>')
            else:
                output.append(self.render_option(selected_choices,
                                                 option_value,
                                                 option_label,
                                                 **data))
        return '\n'.join(output)

