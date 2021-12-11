from django import forms
from .models import Review


class WriteReview(forms.ModelForm):
    """Write Review form to allow users to create their
    own reviews.
    """
    class Meta:
        model = Review
        fields = ('title', 'comments',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Review Title',
            'comments': 'Please write your review/feedback here',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:

            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False
