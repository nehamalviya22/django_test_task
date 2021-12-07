from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Information
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world")


def get_parameters(request):
    sdk_version = request.query_params.get("sdk_version")
    session_id = request.query_params.get("session_id")
    platform = request.query_params.get("platform")
    user_name = request.query_params.get("user_name")
    country_code = request.query_params.get("country_code")
    message = "please provide "

    if not sdk_version:
        message = message + "sdk_version, "
    if not session_id:
        message = message + "session_id, "
    if not platform:
        message = message + "platform, "
    if not user_name:
        message = message + "user_name, "
    if not country_code:
        message = message + "country_code"

    if not sdk_version or not session_id or not platform or not user_name or not country_code:
        return message
    else:
        para_dict = {"sdk_version":sdk_version,"session_id":session_id,"platform":platform,
        "user_name":user_name,"country_code":country_code}
        return para_dict


class GetAd(APIView):
    def get(self, request):
        parameters = get_parameters(request)
        if type(parameters) == str:
            return Response(parameters)

        r = requests.get(url = 'https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/ad/vast',
        params = parameters)

        if r.status_code != 200:
            return Response({"message":"xml is not available"})

        user = Information.objects.create(sdk_version = parameters["sdk_version"],session_id = parameters["session_id"],
        platform = parameters["platform"],username=parameters["user_name"],country_code = parameters["country_code"],media = 'Ad')

        return Response(r.text,content_type="text/xml; charset=utf-8")

class Impression(APIView):
    def get(self, request):
        parameters = get_parameters(request)

        if type(parameters) == str:
            return Response(parameters)

        user = Information.objects.create(sdk_version = parameters["sdk_version"],session_id = parameters["session_id"],
        platform = parameters["platform"],username=parameters["user_name"],country_code = parameters["country_code"],media = 'IMP')

        return Response(status = 200)

class Getstats(APIView):
    def get(self, request):
        filter_type = request.query_params.get("filter_type")
        data = request.query_params.get("data")

        print(filter_type)
        if not filter_type and not data :
            return Response({"message": "Please provide all following parameters filter_type,data"},status = 400)
        elif not filter_type:
            return Response({"message": "Please provide all following parameters filter_type"},status = 400)
        elif not data:
            return Response({"message": "Please provide all following parameters data"},status = 400)


        if filter_type.lower() == "user":
            ad_count = Information.objects.filter(username = data,media = 'Ad').count()
            impression_count = Information.objects.filter(username = data,media = 'IMP').count()
            if ad_count == 0 and impression_count == 0:
                return Response({"message": "no user found"},status=400)
            try:
                fill_rate = ad_count/impression_count
            except:
                fill_rate = "Not Available"
                    
            return Response({"ad_count":ad_count,"impression_count":impression_count,
            "fill_rate":fill_rate},status = 200)
            
        else:
            ad_count = Information.objects.filter(sdk_version = data,media = 'Ad').count()
            impression_count = Information.objects.filter(sdk_version = data,media = 'IMP').count()
            if ad_count == 0 and impression_count == 0:
                return Response({"message": "no sdk version found"},status=400)
            try:
                fill_rate = ad_count/impression_count
            except:
                fill_rate = "Not Available"
                    
            return Response({"ad_count":ad_count,"impression_count":impression_count,
            "fill_rate":fill_rate},status = 200)
