from django.http import HttpResponse
from django.shortcuts import render
from .models import Test, Test2
from rest_framework import viewsets,views
from .serializers import Test2Serializer
from rest_framework.permissions import AllowAny
from asgiref.sync import sync_to_async
import time
import asyncio
# Create your views here.

class Test2ViewSet(viewsets.ModelViewSet):
    serializer_class = Test2Serializer
    queryset = Test2.objects.all()
    permission_classes = [AllowAny]

@sync_to_async
def get_test2_async():
    return Test2.objects.all()

@sync_to_async
def get_test_async():
    return Test.objects.all()

async def async_main_view(request):
    start_time=time.time()
    task1=asyncio.ensure_future(get_test2_async())
    task2 = asyncio.ensure_future(get_test_async())
    await asyncio.wait([task1,task2])
    print(time.time()-start_time)
    return HttpResponse('async')