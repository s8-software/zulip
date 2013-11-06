from django.conf.urls import patterns, url
from django.views.generic import TemplateView, RedirectView

urlpatterns = patterns('',
    # Job postings
    url(r'^jobs/$', TemplateView.as_view(template_name='corporate/jobs/index.html')),
    url(r'^jobs/lead-designer/$', TemplateView.as_view(template_name='corporate/jobs/lead-designer.html')),

    # Zephyr/MIT
    url(r'^zephyr/$', TemplateView.as_view(template_name='corporate/zephyr.html')),
    url(r'^mit/$', TemplateView.as_view(template_name='corporate/mit.html')),
    url(r'^zephyr-mirror/$', TemplateView.as_view(template_name='corporate/zephyr-mirror.html')),

    # Marketing
    # Landing page, features pages, signup form, etc.
    url(r'^hello/$', TemplateView.as_view(template_name='corporate/hello.html'),
                                         name='landing-page'),
    url(r'^new-user/$', RedirectView.as_view(url='/hello')),
    url(r'^features/$', TemplateView.as_view(template_name='corporate/features.html')),
    url(r'^compare/$', TemplateView.as_view(template_name='corporate/compare.html')),

    url(r'^signup/$', TemplateView.as_view(template_name='corporate/signup.html'),
                                         name='signup'),
    # TODO: The beta signup view should probably be moved to corporate.
    url(r'^signup/sign-me-up$', 'zerver.views.beta_signup_submission', name='beta-signup-submission'),
)
