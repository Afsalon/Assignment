from rest_framework.response import Response
from rest_framework.views import APIView
from content.serializers import ContentSerializer,ContentChangeSerializer
from content.models import Content
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class ContentAPI(APIView):
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request,format = None):
        try:
            current_user = request.user
            if (current_user.is_superuser):
                contents = Content.objects.all()
            else:
                contents = Content.objects.filter(user=request.user)
            serializer = self.serializer_class(contents,many=True)
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    def post(self, request, format = None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ContentChangeAPI(APIView):
    serializer_class = ContentChangeSerializer
    permission_classes = [IsAuthenticated]
    def put(self,request,pk, format = None):
        try:
            content = Content.objects.get(pk = pk)
            if request.user.email == content.user.email or request.user.is_superuser:
                serializer = self.serializer_class(content,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    serialized_data = serializer.data
                    return Response(serialized_data)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({"Object":"DoesNotExist"})
    
    def delete(self, request, pk=None, format = None):
        try:
            content = Content.objects.get(pk = pk)
            if request.user.email == content.user.email or request.user.is_superuser:
                content.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status =status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({"Object":"DoesNotExist"})