import json

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Series
from .serializer import SeriesSerializer
from rest_framework.response import Response


class SeriesView(APIView):
    def post(self, request):
        data = request.data
        new_series = Series(
            SeriesInstanceUID=data["SeriesInstanceUID"],
            PatientID=data["PatientID"],
            PatientName=data["PatientName"],
            StudyInstanceUID=data["StudyInstanceUID"],
            InstancesInSeries=data["InstancesInSeries"],
        )
        new_series.save()
        return Response("added to database successfully", status=200)

    def get(self, request):
        series = Series.objects.all()
        serializer = SeriesSerializer(series, many=True)
        return Response(serializer.data)
