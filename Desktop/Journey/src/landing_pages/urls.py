from django.conf.urls import url

from .views import (
                 home_page,
                 golden_gate_bridge,
                 contact,
                 thank_you,
)

urlpatterns = [
    url(r'^$', home_page, name='home-page'),
    url(r'sf/golden-gate-bridge-tour/$', golden_gate_bridge, name='golden-gate-bridge'),
    url(r'contact/$', contact, name='contact-page'),
    url(r'thank-you/$', thank_you, name='thank-you'),
]