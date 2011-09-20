from django.conf.urls.defaults import *

urlpatterns = patterns('subscription.examples.yourlabs.views',
    url(
        r'^$',
        'list',
        name='subscription_list',
    ),
    url(
        r'^json/$',
        'json',
        name='subscription_json',
    ),
)
