from django.conf.urls import url

from companies import views as companies_views
from employees import views as employees_views
from feedback import views as feedback_views


urlpatterns = [
    url(r'^companies/company/$', companies_views.CompanyListAPIView.as_view(), name='company-list'),
    url(r'^companies/company/(?P<pk>\d+)$', companies_views.CompanyRetrieveAPIView.as_view(), name='company-detail'),
    url(r'^companies/center/$', companies_views.CenterListAPIView.as_view(), name='center-list'),
    url(r'^companies/center/(?P<pk>\d+)$', companies_views.CenterRetrieveAPIView.as_view(), name='center-detail'),
    url(r'^companies/division/$', companies_views.DivisionListAPIView.as_view(), name='division-list'),
    url(r'^companies/division/(?P<pk>\d+)$', companies_views.DivisionRetrieveAPIView.as_view(), name='division-detail'),

    url(r'^employees/employee/$', employees_views.EmployeeListAPIView.as_view(), name='employee-list'),
    url(r'^employees/employee/(?P<pk>\d+)/$', employees_views.EmployeeRetrieveAPIView.as_view(), name='employee-detail'),

    url(r'^feedback/feedback/$', feedback_views.FeedbackListAPIView.as_view(), name='feedback-list'),
    url(r'^feedback/feedback/add/$', feedback_views.FeedbackCreateAPIView.as_view(), name='feedback-add'),
]
