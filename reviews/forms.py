""" Review forms """

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ ReviewForm class """

    class Meta:
        """ Meta class for ReviewForm """
        model = Review
        fields = ['product', 'title', 'body', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
