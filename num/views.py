from imaplib import _Authenticator
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView,CreateView
from urllib3 import HTTPResponse
from .models import Num
from django.db.models.query import QuerySet
from django.urls import reverse_lazy,reverse
from django.db.models import Q
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from hitcount.views import HitCountDetailView
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
import requests
import time

class NumDetailView(HitCountDetailView):
    model = Num
    template_name = 'num_detail.html'
    count_hit = True

class Numtg(DetailView):
    model = Num
    template_name = 'numtg_detail.html'

    def get(self, request, *args, **kwargs):
        num_instance = self.get_object()
        telegram_message = f"Menga shu: {num_instance.Hududiy_raqam}|{num_instance.Nomer} avtomobil raqami yoqdi, Bu raqamni auksionda yutub bering!"
        send_telegram_message(telegram_message)
        # Fix the redirect statement
        return redirect('https://t.me/Onl1ne_auksion')

def send_telegram_message(message):
    link = "https://t.me/sayfullayev_0204"
    admin_id = 1184615268
    text = f"{message}"
    url = f"https://api.telegram.org/bot{link}/sendMessage?chat_id={admin_id}&text={text}&parse_mode=HTML"
    requests.get(url)

    

class NumListView(ListView):
    
    template_name = 'num_list.html' 
    def get_queryset(self): 
        queryset = Num.objects.all()
        q = self.request.GET.get('q')
        if q:
            queryset=queryset.filter(Q(Nomer__contains=q))
        return queryset
    def get_queryset(self):
        queryset = Num.objects.all()
        q1 = self.request.GET.get('q1')
        if q1:
            queryset=queryset.filter(Q(Hududiy_raqam__contains=q1))
        return queryset
    
class NumCreateView(CreateView):
    model = Num
    template_name = 'num_new.html'
    fields = ['Hududiy_raqam','Nomer','Boshlanish_sanasi','Boshlanish_narxi','Malumot']
    success_url = reverse_lazy('num_list')
