from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.http import Http404

# Create your views here.
@api_view(['POST'])
def submitData(request):
    if request.method == 'POST':
        try:
            serializer = PerevalSerializer(data=request.data)
            if serializer.is_valid():
                instance = serializer.save()
                return Response({"status": 200, "message": "Отправлено успешно", "id": instance.id})
            else:
                return Response({"status": 400, "message": "Bad Request", "id": None})
        except Exception as e:
            return Response({"status": 500, "message": "Ошибка подключения к базе данных", "id": None})

@api_view(['GET'])
def get_submitData(request, id):
    try:
        pereval = Pereval.objects.get(id=id)
        serializer = PerevalSerializer(pereval)
        return Response(data=serializer.data)
    except Pereval.DoesNotExist:
        raise Http404('Не существует перевала с таким id')