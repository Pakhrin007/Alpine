from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import ContactMessage
from .serializers import ContactMessageSerializer
import requests

# # Create your views here.

# def home(request):
#     url=f'http://127.0.0.1:8000/api/message/'
#     if request.method=="POST":
#         college_name=request.POST.get('college_name')
#         email=request.POST.get('email')
#         phone=request.POST.get('phone')
#         message=request.POST.get('message')
#         data={
#             'college_name':college_name,
#             'email':email,
#             'phone':phone,
#             'message':message,
#         }
#         response=requests.post(url,json=data)
#         return redirect('home')
#     return render(request,'index.html')



# class ContactMessageView(ListCreateAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = ContactMessage.objects.all()
#     serializer_class = ContactMessageSerializer



# class ContactMessageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     permission_classes=[IsAuthenticated]
#     queryset=ContactMessage.objects.all()
#     serializer_class=ContactMessageSerializer



from django.contrib import messages

def home(request):
    if request.method == "POST":
        college_name = request.POST.get('college_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        try:
            ContactMessage.objects.create(
                college_name=college_name,
                email=email,
                phone=phone,
                message=message
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
        return redirect('home')
    return render(request, 'index.html')