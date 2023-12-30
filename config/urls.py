from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('sayfullayev/', admin.site.urls),
    path('num/', include('num.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
