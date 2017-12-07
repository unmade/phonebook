from django.conf.urls import url

from . import views

app_name = 'companies'  # pylint: disable=invalid-name


urlpatterns = [
    url(r'^company/$', views.CompanyListAPIView.as_view(), name='company-list'),
    url(r'^company/(?P<pk>\d+)$', views.CompanyRetrieveAPIView.as_view(), name='company-detail'),

    url(r'^center/$', views.CenterListAPIView.as_view(), name='center-list'),
    url(r'^center/(?P<pk>\d+)$', views.CenterRetrieveAPIView.as_view(), name='center-detail'),

    url(r'^division/$', views.DivisionListAPIView.as_view(), name='division-list'),
    url(r'^division/(?P<pk>\d+)$', views.DivisionRetrieveAPIView.as_view(), name='division-detail'),
]
