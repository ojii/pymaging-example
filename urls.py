from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'views.index'),
    url(r'^favicon\.ico$', 'views.favicon'),
)
