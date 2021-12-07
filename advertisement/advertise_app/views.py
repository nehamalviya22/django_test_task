from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Username,Sdkversion

class GetAd(APIView):
    def get(self, request):

        SDK_version = request.query_params.get("SDK Version")
        sessionid = request.query_params.get("SessionId")
        platform = request.query_params.get("Platform")
        user_name = request.query_params.get("User name")
        country_code = request.query_params.get("Country code")

        if not SDK_version or not sessionid or not platform or not user_name or not country_code:
            return Response({"message": "Please provide all following parameters SDK Version,SessionId,Platform,User name,Country code"},status = 400)


        user, created = username.objects.get_or_create(username=user_name)
        if created:
            user.ad_count = 1
            user.save()
        else:
            user.ad_count = user.ad_count+1
            user.save()
        
        sdk, created = sdkversion.objects.get_or_create(sdkversion=SDK_version)
        if created:
            sdk.ad_count = 1
            sdk.save()
        else:
            sdk.ad_count = sdk.ad_count+1
            sdk.save()

        
        parameters = {"SDK Version":SDK_version,
        "SessionId":sessionid,
        "Platform":platform,
        "User name":user_name,
        "Country code":country_code,
        }
        r = requests.get(url = 'https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/ad/vast',
        params = parameters)

        return Response(r.text,content_type="text/xml; charset=utf-8")

