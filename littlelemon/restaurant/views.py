from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import  generics
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class BookingViewSet (ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class MenuSingleView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
   

    