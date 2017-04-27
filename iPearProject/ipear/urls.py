from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html' }, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^register/$', TemplateView.as_view(template_name='index_user_information.html'), name='signup'),
    url(r'^register/accountcreation/$', TemplateView.as_view(template_name='index_user_information.html'), name='user_reg_info'),
    url(r'^register/thankyou/$', TemplateView.as_view(template_name='index_thankyou.html'), name='thankyou'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
