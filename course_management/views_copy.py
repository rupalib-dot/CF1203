from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from course_management.serializers import UserSerializer 
from rest_framework.serializers import Serializer   
from django.urls import reverse 
from django.http.response import JsonResponse 
from datetime import datetime 
from django.db.models import Q
from django.contrib import messages  
from rest_framework.parsers import JSONParser   
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password,check_password
import random


# Create your views here.
@csrf_exempt
def user_register(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        email = request.POST.get('email') 
        password = request.POST.get('password')  
        phone = request.POST.get('phone')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_role = '3'
        about = request.POST.get('about')
        user_image = request.FILES["user_image"]
        # exit()
        users_serializer = UserSerializer(data=request.POST) 
        if users_serializer.is_valid():
            user = User.objects.create_user(username = username , email = email , password = password,first_name = first_name,user_image = user_image, about = about,user_role = user_role,phone = phone,last_name = last_name, )
            user.save()
            id = user.id
            users = User.objects.get(id=id) 
            users_serializer = UserSerializer(users)
            return JsonResponse({'message': 'User created successfully!','data':users_serializer.data}, status=status.HTTP_201_CREATED)  
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all().filter(~Q(user_role=1)) 
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse({'message': 'Users listed successfully!','data':users_serializer.data}, safe=False)
        # 'safe=False' for objects serialization
   
@csrf_exempt
def all_user_delete(request):
    if request.method == 'DELETE':
        count = User.objects.all().filter(~Q(user_role=1)).delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
def user_detail(request, pk):
    try: 
        userDetail = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        users_serializer = UserSerializer(userDetail)
    return JsonResponse({'message': 'User details get successfully!','data':users_serializer.data}, status=status.HTTP_201_CREATED) 

@csrf_exempt
def user_edit(request, pk):  
    try: 
        userDetail = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    # print(userDetail.password)
    if request.method == 'POST': 
        # exit()
        username = request.POST.get('username')
        email = request.POST.get('email') 
        password = make_password(request.POST.get('password')) 
        phone = request.POST.get('phone')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_role = request.POST.get('user_role')
        about = request.POST.get('about')
        user_image = request.FILES["user_image"]
        # exit()
        users_serializer = UserSerializer(data=request.POST) 
        if users_serializer.is_valid():
            user = User.objects.filter(pk=pk).update(username = username , email = email , password = password,first_name = first_name,user_image = user_image, about = about,user_role = user_role,phone = phone,last_name = last_name, )
            users = User.objects.get(pk=pk) 
            users_serializer = UserSerializer(users)
            return JsonResponse({'message': 'User update successfully!','data':users_serializer.data}, status=status.HTTP_201_CREATED)  
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@csrf_exempt
def user_delete(request, pk):
    try: 
        userDetail = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'DELETE': 
        userDetail.delete() 
    return JsonResponse({'message': 'User deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
         #logged in using username and password
        # username = request.POST.get('username')
        # password = request.POST.get('password')  
        # users = authenticate(username=username , password = password)

        #logged in using phone
        phone = request.POST.get('phone')
        users = User.objects.get(phone = phone)
 
        if users is not None:  
            users_serializer = UserSerializer(users)
            return JsonResponse({'message': 'User logged in successfully!','data':users_serializer.data,'otp':random.randint(1111,9999)}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': 'User not found!'}, status=status.HTTP_204_NO_CONTENT)

   