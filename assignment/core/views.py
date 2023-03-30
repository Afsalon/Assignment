from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializers import UserSerializer
from rest_framework import status


class UserAPI(APIView):
    serializer_class = UserSerializer
    def post(self, request, format = None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



