from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import NumListView,  NumDetailView, NumCreateView,Numtg

urlpatterns = [
    path('num/<int:pk>/', NumDetailView.as_view(), name='num_detail'),
    path('numtg/<int:pk>/', Numtg.as_view(), name='numtg_detail'),
    path('', NumListView.as_view(), name='num_list'),
    path('new/', NumCreateView.as_view(), name='num_new'),
]




