from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date
from .models import Device
from .serializers import DeviceSerializer,ReadingSerializer

class DeviceListView(APIView):
    def get(self,request):
        return Response(DeviceSerializer(Device.objects.all(),many=True).data)

class DeviceSummaryView(APIView):
    def get(self,request,id):
        device=get_object_or_404(Device,id=id)
        qs=device.readings.all()
        f,t=request.GET.get('from'),request.GET.get('to')
        if f and t:
            fd,td=parse_date(f),parse_date(t)
            if not fd or not td or fd>td:
                return Response({'error':'Invalid date range'},status=400)
            qs=qs.filter(timestamp__date__gte=fd,timestamp__date__lte=td)
        return Response({'device':device.name,'count':qs.count(),'readings':ReadingSerializer(qs,many=True).data})
