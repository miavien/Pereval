from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.http import Http404

# Create your views here.
class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_fields = ['user__email']

@api_view(['POST'])
def submitData(request):
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
        raise Http404('Запись с таким id не найдена')

@api_view(['PATCH'])
def patch_submitData(request, id):
    try:
        pereval = Pereval.objects.get(id=id)
    except Pereval.DoesNotExist:
        return Response({"state": 0, "message": "Запись с таким id не найдена"})
    if pereval.status != 'new':
        return Response({"state": 0, "message": "Можно редактировать записи только в статусе 'new'"})
    data = request.data.copy()
    for field in ['email', 'fam', 'name', 'otc', 'phone']:
        data.pop(field, None)

    serializer = PerevalSerializer(pereval, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"state": 1, "message": "Запись успешно обновлена"})
    else:
        return Response({"state": 0, "message": serializer.errors})