from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Info
from .serializers import InfoSerializer

@api_view(['POST'])
def insert_data(request):
    serializer = InfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_data(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        info = Info.objects.get(username=username, password=password)
        if info is not None:
            serializer = InfoSerializer(info)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
    except Info.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
