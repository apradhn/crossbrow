from django import template
from projects.forms.browser import BrowserResultForm

register = template.Library()


@register.inclusion_tag('browser_results.html')
def show_browsers(project, feature, testcase, request):
    browsers = project.browser_set.all()
    return {
        'browsers': browsers,
        'project': project,
        'feature': feature,
        'testcase': testcase,
        'request': request
    }


@register.inclusion_tag('browsers/browser_update_result_form.html')
def show_browser_update_result(project, feature, testcase, browser, request):
    # import pdb; pdb.set_trace()
    return {
        'form': BrowserResultForm(instance=browser),
        'browser_pk': browser.pk
    }
