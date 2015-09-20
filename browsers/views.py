from django.shortcuts import render
from .models import Browser
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    browsers = get_list_or_404(Browser)
    return render(
        request,
        'index.html',
        {
            'browsers': browsers
        }
    )


def update_result(request, browser_id):
    browser = get_object_or_404(Browser, pk=browser_id)
    try:
        result = request.POST['browser-result']
    except:
        return render(request, 'projects:test_case_detail', request.POST['project-id'], request.POST['feature-id'], request.POST['test-case-idd'])

    else:
        browser.result = result
        browser.save()
        return HttpResponseRedirect(reverse('projects:test_case_detail', args=(request.POST['project-id'], request.POST['feature-id'], request.POST['test-case-id'])))
