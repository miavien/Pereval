from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import *
from django.http import Http404

# Create your views here.
class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_fields = ['user__email']

    #убираем нереализованные методы delete, put
    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        pass
    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        try:
            serializer = PerevalSerializer(data=request.data)
            if serializer.is_valid():
                instance = serializer.save()
                return Response({"status": 200, "message": "Отправлено успешно", "id": instance.id})
            else:
                return Response({"status": 400, "message": "Bad Request", "id": None})
        except Exception as e:
            return Response({"status": 500, "message": "Ошибка подключения к базе данных", "id": None})

    def retrieve(self, request, *args, **kwargs):
        try:
            pereval = self.get_object()
            serializer = PerevalSerializer(pereval)
            return Response(data=serializer.data)
        except Http404:
            return Response({"state": 0, "message": "Запись с таким id не найдена"})

    def partial_update(self, request, *args, **kwargs):
        try:
            pereval = self.get_object()
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