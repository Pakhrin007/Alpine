from django.shortcuts import render,redirect
from . models import ContactMessage
from .serializers import ContactMessageSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
import requests

# Create your views here.

def home(request):
    url=f'http://127.0.0.1:8000/api/message/'
    if request.method=="POST":
        college_name=request.POST.get('college_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        data={
            'college_name':college_name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        response=requests.post(url,json=data)
        return redirect('home')
    return render(request,'index.html')



class ContactMessageView(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=ContactMessage.objects.all()
    serializer_class=ContactMessageSerializer



class ContactMessageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset=ContactMessage.objects.all()
    serializer_class=ContactMessageSerializer