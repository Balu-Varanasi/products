from django.conf.urls import patterns, url

urlpatterns = patterns('demo_app.views',
                       url(r'^$', 'home', name='home'))
