import csv
from datetime import date
# from genericpath import exists
from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from sahithi.settings import *
from django.core.files.storage import FileSystemStorage
import os
#import pandas as pd
from datetime import date
import calendar
import datetime

def index(request):
    return render(request, "index.html")



"""
class index(APIView):
    
    
    def post(self,request):
        name=request.data['student']
        return Response('post')
    def get(self,request):
        def get_user_birthday():
            year = 2022
            month = 3
            day = 11

            birthday = datetime.datetime(year,month,day)
            return birthday


        def calculate_dates(original_date, now):
            date1 = now
            date2 = datetime.datetime(now.year, original_date.month, original_date.day)
            delta = date2 - date1
            days = delta.total_seconds() / 60 /60 /24

            return days


        def show_info(self):
            pass



        bd = get_user_birthday()
        now = datetime.datetime.now()
        c = calculate_dates(bd,now)
        print(c)
        return HttpResponse('get sankeerth '+str(c))
"""
