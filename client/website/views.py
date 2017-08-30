
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf.urls import url
from rest_framework import status

import urllib2
import json

response = urllib2.urlopen('http://ijmondal.pythonanywhere.com/households/?format=json')
data = json.load(response)
response = urllib2.urlopen('http://ijmondal.pythonanywhere.com/points/?format=json')
pointsData = json.load(response)
response = urllib2.urlopen('http://ijmondal.pythonanywhere.com/members/?format=json')
membersData = json.load(response)
response = urllib2.urlopen('http://ijmondal.pythonanywhere.com/farms/?format=json')
data4 = json.load(response)
response = urllib2.urlopen('http://ijmondal.pythonanywhere.com/farmPoints/?format=json')
data5 = json.load(response)
response = urllib2.urlopen('http://ijmondal.pythonanywhere.com/cropping/?format=json')
data6 = json.load(response)
response = urllib2.urlopen('http://ijmondal.pythonanywhere.com/crops/?format=json')
data7 = json.load(response)
response = urllib2.urlopen('http://ijmondal.pythonanywhere.com/seasons/?format=json')
data8 = json.load(response)
response = urllib2.urlopen('http://ijmondal.pythonanywhere.com/wells?format=json')
data9 = json.load(response)
response = urllib2.urlopen('http://ijmondal.pythonanywhere.com/yields/?format=json')
data10 = json.load(response)



class HouseholdsList(APIView):

    def get(self, request):
        # households = HouseHolds.objects.all()
        # serializer = HouseHoldSerializer(households, many=True)
        return Response(data)

    def post(self):
        pass


class PointsList(APIView):

    def get(self, request):
        # points = Points.objects.all()
        # serializer = PointsSerializer(points, many=True)
        return Response(pointsData)

    def post(self):
        pass


class MembersList(APIView):

    def get(self, request):
        # members = Members.objects.all()
        # serializer = MembersSerializer(members, many=True)
        return Response(membersData)

    def post(self):
        pass



class FarmsList(APIView):

    def get(self, request):
        # farms = Farms.objects.all()
        # serializer = FarmsSerializer(farms, many=True)
        return Response(data4)

    def post(self):
        pass


class Farm_pointsList(APIView):

    def get(self, request):
        # farm_points = Farm_points.objects.all()
        # serializer = Farm_pointsSerializer(farm_points, many=True)
        return Response(data5)

    def post(self):
        pass


class CroppingList(APIView):

    def get(self, request):
        # cropping = Cropping.objects.all()
        # serializer = CroppingSerializer(cropping, many=True)
        return Response(data6)

    def post(self):
        pass


class CropsList(APIView):

    def get(self, request):
        # crops = Crops.objects.all()
        # serializer = CropsSerializer(crops, many=True)
        return Response(data7)

    def post(self):
        pass


class SeasonsList(APIView):

    def get(self, request):
        # seasons = Seasons.objects.all()
        # serializer = HouseHoldSerializer(seasons, many=True)
        return Response(data8)

    def post(self):
        pass


class WellsList(APIView):

    def get(self, request):
        # wells = Wells.objects.all()
        # serializer = WellsSerializer(wells, many=True)
        return Response(data9)

    def post(self):
        pass


class YieldsList(APIView):

    def get(self, request):
        # yields = Yields.objects.all()
        # serializer = HouseHoldSerializer(yields, many=True)
        return Response(data10)

    def post(self):
        pass



