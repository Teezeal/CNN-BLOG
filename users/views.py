from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer

# Create your views here.
@api_view(["POST"])
def api_register_view(request):
    if request.method == "POST":
        serializer = UserRegistrationSerializer(data=request.data)
        details = {}
        if serializer.is_valid():
            user = serializer.save()
            details["Succes"] = "Your account has been creaated"
            details["username"] = user.username
            details["email"] = user.email
            return Response(data=details, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)