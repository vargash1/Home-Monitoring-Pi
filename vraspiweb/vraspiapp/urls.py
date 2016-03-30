from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^vraspiapp/$',views.home),
    # login
    url(r'^vraspiapp/login/$', login,
    {
        'template_name': 'vraspiapp/login.html'
    }),
    # logout
    url(r'^vraspiapp/logout/$', logout,
    {
        'template_name': 'vraspiapp/logout.html'
    }),

    url(r'^vraspiapp/signup/$', views.signup),
    url(r'^vraspiapp/signup_success/$', views.signup_success),
]
