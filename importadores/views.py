from django.shortcuts import render
from .models import Importador
from .serializers import ImportadoresSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def ListarImportadores(request):
    importadores = Importador.objects.all()
    serializer = ImportadoresSerializer(importadores, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def FiltrarImportador(request, pk):
    importadores = Importador.objects.get(id_producto=pk)
    serializer = ImportadoresSerializer(importadores, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CrearImportador(request):
    serializer = ImportadoresSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['POST'])
def ActualizarImportador(request, pk):
    importadores = Importador.objects.get(id_importador=pk)
    serializer = ImportadoresSerializer(instance=importadores, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def EliminarImportador(request, pk):
    importadores = Importador.objects.get(id_importador=pk)
    importadores.delete()

    return Response('Importador eliminado')
