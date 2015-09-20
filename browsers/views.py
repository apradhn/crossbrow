from django.shortcuts import render
from .models import Browser
from django.shortcuts import get_list_or_404


def index(request):
    browsers = get_list_or_404(Browser)
    return render(
        request,
        'index.html',
        {
            'browsers': browsers
        }
    )
