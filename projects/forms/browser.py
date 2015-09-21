from django.forms import ModelForm
from browsers.models import Browser


class BrowserResultForm(ModelForm):
    class Meta:
        model = Browser
        fields = ['result']
