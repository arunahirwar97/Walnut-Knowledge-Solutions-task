from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
# Create your views here.

class ageAdvisorsView(APIView):
    def get(self, request, day,month,year):
        if day > 31 :
            return Response({"Please Enter correct  day with in 1 to 31 "})
        elif month > 12:
            return Response({"Please Enter correct  month with in 1 to 12 "})
        elif  year > datetime.now().year :
            return Response({"Please Enter correct  year"})
        else:
            currentDay = datetime.now().day
            currentMonth = datetime.now().month
            currentYear = datetime.now().year
            age_day = abs(currentDay-day)
            age_month = abs(currentMonth-month)
            age_year = abs(currentYear-year)
            return Response({"Total  : {} year {} Month {} Days".format(age_year,age_month,age_day)})
