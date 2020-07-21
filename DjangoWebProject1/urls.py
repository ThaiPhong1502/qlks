"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from app.models import LOAIPHONG
admin.site.register(LOAIPHONG)

from app.models import PHONG
admin.site.register(PHONG)

from app.models import LOAIKHACHHANG
admin.site.register(LOAIKHACHHANG)

from app.models import KHACHHANG
admin.site.register(KHACHHANG)

from app.models import PHIEUDATPHONG
admin.site.register(PHIEUDATPHONG)

from app.models import HOADON
admin.site.register(HOADON)

from app.models import THONGKEDOANHTHU
admin.site.register(THONGKEDOANHTHU)


urlpatterns = [
    path('',views.list),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
