from django import forms
from .models import Book
from app_accounts.models import User


class ParserForm(forms.Form):
    url = forms.URLField(label="URL")

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ParserForm, self).__init__(*args, **kwargs)

    def clean(self):
        form_data = self.cleaned_data
        if Book.objects.filter(url=form_data['url'], user=self.user):
            raise forms.ValidationError('У вас уже есть данная ссылка!')


